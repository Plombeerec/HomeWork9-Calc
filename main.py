
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, ConversationHandler, Filters
from config import TOKEN
# from file_work import *
from commands import *
from play import lets_play

bot = Bot(token=TOKEN)
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

TITLE, TASK = 'title', 'task'

one_task = {
    'title': None,
    'description': None
}


start_handler = CommandHandler('start', start)
help_handler = CommandHandler('help', helper)
float_calculate_handler = CommandHandler('float', float_calculate)
complex_calculate_handler = CommandHandler('complex', complex_calculate)
play_handler = CommandHandler('play', lets_play)


dispatcher.add_handler(start_handler)
dispatcher.add_handler(float_calculate_handler)
dispatcher.add_handler(complex_calculate_handler)
dispatcher.add_handler(lets_play)

print('server started')
updater.start_polling()
updater.idle()