import bot.bot as bot
from loading.load_map import load_map
from loading.load_data import load_data

if __name__ == '__main__':
    load_map()
    load_data()
    bot.start_bot()