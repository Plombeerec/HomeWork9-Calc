from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, ConversationHandler, Filters
from operation import *
import operation as oper

def start(update, context):
    arg = context.args
    context.bot.send_message(update.effective_chat.id, f"Привет, {update.effective_user.first_name}")
    context.bot.send_message(update.effective_chat.id, f"Этот бот знает следующие команды /hi\n/float\n/complex\n/play")
    # await update.message.reply_text(f'Hello /hi\n/time\n/help\n/sum')


def helper(update, context):
    arg = context.args
    if not arg:
        context.bot.send_message(update.effective_chat.id, "Привет")
    else:
        context.bot.send_message(update.effective_chat.id, f"{' '.join(arg)}")

def float_calculate(update, context):
    arg = context.args
    print(arg)

    a = float(arg[0])
    operator = arg[1]
    b = float(arg[2])
    if operator == '*':
        result = oper.mult(a, b)
    elif operator == '/':
        result = oper.div(a, b)
    elif operator == '+':
        result = oper.sum(a, b)
    elif operator == '-':
        result = oper.diff(a, b)

    context.bot.send_message(update.effective_chat.id, f"Result = {result}")

def complex_calculate(update, context):
    arg = context.args
    print(arg)

    a = complex(arg[0])
    operator = arg[1]
    b = complex(arg[2])
    if operator == '*':
        result = oper.mult(a, b)
    elif operator == '/':
        result = oper.div(a, b)
    elif operator == '+':
        result = oper.sum(a, b)
    elif operator == '-':
        result = oper.diff(a, b)

    context.bot.send_message(update.effective_chat.id, f"Result = {result}")

