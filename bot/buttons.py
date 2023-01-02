from aiogram import types

new_game = types.InlineKeyboardButton(text='New game', callback_data='button_new_game')
load_game = types.InlineKeyboardButton(text='Load game', callback_data='button_load_game')
rules = types.InlineKeyboardButton(text='Rules', callback_data='button_rules')

go = types.InlineKeyboardButton(text='Go to...', callback_data='button_go')

talk_to = types.InlineKeyboardButton(text='Talk to...', callback_data='button_talk_to')

start_battle = types.InlineKeyboardButton(text='Fight with...', callback_data='button_start_battle')
continue_battle = types.InlineKeyboardButton(text='Continue fight...', callback_data='button_continue')
end_battle = types.InlineKeyboardButton(text='Run away', callback_data='button_end_battle')

go_to_choose_action = types.InlineKeyboardButton(text='Back', callback_data='button_go_to_choose_action')
go_to_main_menu = types.InlineKeyboardButton(text="To main menu", callback_data='button_go_to_main_menu')

info_buttons = []
info_buttons.append(types.InlineKeyboardButton(text='Who am I', callback_data='button_about_me'))
info_buttons.append(types.InlineKeyboardButton(text='Where I am', callback_data='button_wereami'))
info_buttons.append(types.InlineKeyboardButton(text='Who is there', callback_data='button_whothere'))
