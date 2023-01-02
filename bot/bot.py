from aiogram import Bot, Dispatcher, executor
from aiogram import types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

import time

import bot.handlers as handlers

API_TOKEN = open('bot/token', 'r')

bot = Bot(token=API_TOKEN.read())
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


dp.register_callback_query_handler(handlers.start_new_game, text='button_new_game', state=handlers.user_session.load_game)
dp.register_callback_query_handler(handlers.load_game, text='button_load_game', state=handlers.user_session.load_game)
dp.register_callback_query_handler(handlers.print_rules, text='button_rules', state=handlers.user_session.load_game)

dp.register_callback_query_handler(handlers.print_info_about_user, text='button_about_me')
dp.register_callback_query_handler(handlers.print_info_about_location, text='button_wereami')

dp.register_callback_query_handler(handlers.get_action, state=handlers.user_session.choice_action)
dp.register_callback_query_handler(handlers.get_direction, state=handlers.user_session.change_location)
dp.register_callback_query_handler(handlers.talk_to_npc, state=handlers.user_session.talk_to)
dp.register_callback_query_handler(handlers.attack_enemy, state=handlers.user_session.start_battle)
dp.register_callback_query_handler(handlers.is_battle_continue, state=handlers.user_session.is_continue_battle)
dp.register_message_handler(handlers.start, commands=["start"])
dp.register_message_handler(handlers.start)


def start_bot():
    executor.start_polling(dp, skip_updates=True)

