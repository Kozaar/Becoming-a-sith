from aiogram import Bot, Dispatcher, executor
from aiogram import types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

import time

import bot.buttons as buttons
import controller.Controller as ctrl

controller = {}


class user_session(StatesGroup):
    load_game = State()
    choice_action = State()
    change_location = State()
    talk_to = State()
    start_battle = State()
    is_continue_battle = State()

async def start(message: types.Message):
    print('user id ', message.chat.id)
    if not controller.get(message.chat.id):
        controller[message.chat.id] = ctrl.Controller('game.db')
    
    main_menu = types.InlineKeyboardMarkup(row_width=2)
    main_menu.add(buttons.new_game)
    '''Проверка существования юзера'''
    if controller[message.chat.id].get_protagonist_info(message.chat.id) != None:
        main_menu.insert(buttons.load_game)
    main_menu.insert(buttons.rules)
    await message.answer('Main menu', reply_markup=main_menu)
    await user_session.load_game.set()


async def start_new_game(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.delete()
    await callback.message.answer('Start new game')
    await user_session.choice_action.set()
    controller[callback.message.chat.id].start_game(callback.message.chat.id, True)
    await print_info_about_user(callback.message)
    await show_possible_actions(callback.message)
    

async def load_game(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.delete()
    await callback.message.answer('Loading game...')
    controller[callback.message.chat.id].start_game(callback.message.chat.id, False)
    await callback.message.answer('Loading is complete')
    await print_info_about_user(callback.message)
    await show_possible_actions(callback.message)
    await user_session.choice_action.set()

async def print_rules(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.delete()
    await callback.message.answer('You are a Jedi who has turned to the dark side. You have a task from the Captain, it must be completed\n\
During battle, you and your opponent roll a die and add your level to the result. The one with the most points wins.\
If you win, the enemy will die. If you are defeated, you lose 1 HP.\n\
To restore health, return to the starting location and talk to the Medic.')
    main_menu = types.InlineKeyboardMarkup(row_width=2)
    main_menu.insert(buttons.new_game)
    if controller[callback.message.chat.id].get_protagonist_info(callback.message.chat.id) != None:
        main_menu.insert(buttons.load_game)
    main_menu.insert(buttons.rules)
    await callback.message.answer('Main menu', reply_markup=main_menu)

async def print_info_about_user(message: types.Message):
    await message.answer('You:')
    await message.answer("Name: " + controller[message.chat.id].protagonist.name + '\n'\
    + "Level: " + str(controller[message.chat.id].protagonist.level) + '\n'\
    + "Health: " + str(controller[message.chat.id].protagonist.hp))

async def print_info_about_location(message: types.Message):
    msg = controller[message.chat.id].protagonist.whereami()
    for i in msg:
        await message.answer(i)

async def print_info_about_ai_in_location(message: types.Message):
    npc = controller[message.chat.id].get_npc_in_location(controller[message.chat.id].protagonist.locations.id)
    enemy = controller[message.chat.id].get_enemy_in_location(controller[message.chat.id].protagonist.locations.id)
    npc_message = 'NPC:'
    for i in npc:
        npc_message += '\n' + i.name
    await message.answer(npc_message)
    enemy_message = "Enemies:"
    for i in enemy:
        enemy_message += '\n' + i.name
    await message.answer(enemy_message)
    

async def show_possible_actions(message: types.Message):
    actions = types.InlineKeyboardMarkup(row_width=2)
    actions.insert(buttons.go)
    try:
        if len(controller[message.chat.id].get_npc_in_location(controller[message.chat.id].protagonist.locations.id)):
            actions.insert(buttons.talk_to)
    except Exception as e:
        print(e, 'in show possible actions when get npc')
    try:
        if len(controller[message.chat.id].get_enemy_in_location(controller[message.chat.id].protagonist.locations.id)):
            actions.insert(buttons.start_battle)
    except Exception as e:
        print(e, 'in show possible actions when get enemys')
    actions.add(buttons.go_to_main_menu)
    actions.add(*buttons.info_buttons)
    await message.answer('You can:', reply_markup=actions)


async def get_action(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.delete()
    if callback.data == 'button_go':
        await user_session.change_location.set()
        await show_available_directions(callback.message)
    elif callback.data == 'button_talk_to':
        await user_session.talk_to.set()
        await choose_npc(callback)
    elif callback.data == 'button_start_battle' or callback.data == 'button_continue':
        await user_session.start_battle.set()
        await choose_enemy(callback)
    elif callback.data == 'button_about_me':
        await print_info_about_user(callback.message)
        await show_possible_actions(callback.message)
    elif callback.data == 'button_wereami':
        await print_info_about_location(callback.message)
        await show_possible_actions(callback.message)
    elif callback.data == 'button_whothere':
        await print_info_about_ai_in_location(callback.message)
        await show_possible_actions(callback.message)
    elif callback.data == 'button_go_to_main_menu':
        await state.finish()
        await start(callback.message)
    else:
        await callback.message.answer('Not now ╮(︶︿︶)╭')

async def get_direction(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.delete()
    is_correct = True
    if 'button' in callback.data:
        is_correct = False
        if callback.data == 'button_about_me':
            await print_info_about_user(callback.message)
        elif callback.data == 'button_wereami':
            await print_info_about_location(callback.message)
        elif callback.data == 'button_whothere':
            await print_info_about_ai_in_location(callback.message)
        elif callback.data == 'button_go_to_choose_action':
            is_correct = True
    else:
        locations = controller[callback.message.chat.id].get_locations_to_go()
        if locations != None:
            try:
                for i in locations:
                    print(callback.data)
                    if i.id == int(callback.data):
                        controller[callback.message.chat.id].go(i)
                        loc = controller[callback.message.chat.id].get_current_location()
                        await callback.message.answer("Moved to location " + loc.name)
                        await callback.message.answer(loc.description)
                        break
            except Exception as e:
                print(e)
                await callback.message.answer('Not now (・人・)')
    if is_correct:
        await user_session.choice_action.set()
        await show_possible_actions(callback.message)
    else:
        await show_available_directions(callback.message)

async def show_available_directions(message: types.Message):
    # получение доступных напрвлений
    directions = types.InlineKeyboardMarkup(row_width=2)
    locations = controller[message.chat.id].get_locations_to_go()
    if locations != None:
        for i in locations:
            directions.insert(types.InlineKeyboardButton(text=i.name, callback_data=i.id))
    directions.insert(buttons.go_to_choose_action)
    for i in buttons.info_buttons:
        directions.insert(i)
    await message.answer('Go to...', reply_markup=directions)

async def choose_npc(callback: types.CallbackQuery):
    btns = types.InlineKeyboardMarkup(row_width=2)
    for i in controller[callback.message.chat.id].get_npc_in_location(controller[callback.message.chat.id].protagonist.locations.id):
        btns.insert(types.InlineKeyboardButton(text=i.name, callback_data=str(i.id)))
    for i in buttons.info_buttons:
        btns.insert(i)
    btns.insert(buttons.go_to_choose_action)
    await callback.message.answer('Talk to...', reply_markup=btns)


async def talk_to_npc(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.delete()
    if 'button' in callback.data:
        is_cancle = False
        if callback.data == 'button_about_me':
            await print_info_about_user(callback.message)
        elif callback.data == 'button_wereami':
            await print_info_about_location(callback.message)
        elif callback.data == 'button_whothere':
            await print_info_about_ai_in_location(callback.message)
        elif callback.data == 'button_go_to_choose_action':
            is_cancle = True
        if is_cancle:
            await user_session.choice_action.set()
            await show_possible_actions(callback.message)
        else:
            await choose_npc(callback)
    else:
        npc = controller[callback.message.chat.id].get_npc(callback.data)
        npc_phrases = controller[callback.message.chat.id].interact(npc.id)
        is_end_game = npc_phrases[0]
        await callback.message.answer(npc.name + ' says: "' + npc_phrases[1] + '"')
        if is_end_game:
            controller[callback.message.chat.id].end_game()
            await state.finish()
            await start(callback.message)
        else:
            await user_session.choice_action.set()
            await show_possible_actions(callback.message)


async def choose_enemy(callback: types.CallbackQuery):
    btns = types.InlineKeyboardMarkup(row_width=2)
    for i in controller[callback.message.chat.id].get_enemy_in_location(controller[callback.message.chat.id].protagonist.locations.id):
        # await callback.message.answer(i.name)
        btns.insert(types.InlineKeyboardButton(text=i.name + ' lvl:' + str(i.level), callback_data=str(i.id)))
    for i in buttons.info_buttons:
        btns.insert(i)
    btns.insert(buttons.go_to_choose_action)
    await callback.message.answer('Fight with...', reply_markup=btns)


async def attack_enemy(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.delete()
    if 'button' in callback.data:
        is_cancle = False
        if callback.data == 'button_about_me':
            await print_info_about_user(callback.message)
            # await show_available_directions(callback.message)
        elif callback.data == 'button_wereami':
            await print_info_about_location(callback.message)
            # await show_available_directions(callback.message)
        elif callback.data == 'button_whothere':
            await print_info_about_ai_in_location(callback.message)
            # await show_available_directions(callback.message)
        elif callback.data == 'button_go_to_choose_action':
            is_cancle = True
        if is_cancle:
            await user_session.choice_action.set()
            await show_possible_actions(callback.message)
        else:
            await choose_npc(callback)
    else:
        try:
            kill_enemy, phrases = controller[callback.message.chat.id].attack_enemy(int(callback.data))
            if phrases != None:
                await callback.message.answer('Q(`⌒´Q)')
                for i in phrases:
                    await callback.message.answer(i)
                if kill_enemy:
                    await user_session.choice_action.set()
                    await show_possible_actions(callback.message)
                else:
                    await user_session.is_continue_battle.set()
                    await callback.message.answer('Continue fight?', reply_markup=types.InlineKeyboardMarkup(row_width=1).add(buttons.continue_battle, buttons.end_battle))
            else:
                await callback.message.answer('ヽ(ˇヘˇ)ノ')
                await callback.message.answer('You have ' + str(controller[callback.message.chat.id].protagonist.hp) + ' hp left')
                await user_session.choice_action.set()
                await show_possible_actions(callback.message)
        except Exception as e:
            print(e)
            controller[callback.message.chat.id].end_game()
            await callback.message.answer('Younglings kicked you. Not ashamed?')
            await state.finish()
            await start(callback.message)


async def is_battle_continue(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.delete()
    if callback.data == 'button_continue':
        await user_session.start_battle.set()
        await choose_enemy(callback)
    elif callback.data == 'button_end_battle':
        await callback.message.answer('w(°ｏ°)w')
        await user_session.choice_action.set()
        await show_possible_actions(callback.message)
    elif callback.data == 'button_about_me':
        await print_info_about_user(callback.message)
        await callback.message.answer('Continue fight?', reply_markup=types.InlineKeyboardMarkup(row_width=1).add(buttons.continue_battle, buttons.end_battle))
    elif callback.data == 'button_wereami':
        await print_info_about_location(callback.message)
        await callback.message.answer('Continue fight?', reply_markup=types.InlineKeyboardMarkup(row_width=1).add(buttons.continue_battle, buttons.end_battle))
    elif callback.data == 'button_whothere':
        await print_info_about_ai_in_location(callback.message)
        await callback.message.answer('Continue fight?', reply_markup=types.InlineKeyboardMarkup(row_width=1).add(buttons.continue_battle, buttons.end_battle))
    else:
        await callback.message.answer('Not now (・人・)')
        await user_session.choice_action.set()
        await show_possible_actions(callback.message)
