#!/usr/bin/env python3
import datetime
import logging
import pytz
import os

from telegram import Update, ForceReply, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler

from db import DB
from i1337 import *

bot_token = os.getenv('BOT_TOKEN')
bot_name = os.getenv('BOT_NAME')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

connection_string = os.getenv('MONGODB_STRING')
database = DB(connection_string)

def start(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat.id
    name = ''
    try:
        name = update.message.chat.title
    except:
        pass
    if not name:
        try:
            name = update.message.chat.first_name + ' ' + update.message.chat.last_name
        except:
            try:
                name = update.message.chat.username
            except:
                pass
    logger.info(f'Start in chat {chat_id}, title {name}')
    if database.add_chat(chat_id):
        context.bot.send_message(chat_id=chat_id, text='wazzup hackers\nThe bot is started')
    else:
        context.bot.send_message(chat_id=chat_id, text='Something went wrong')

def stop(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat.id
    name = ''
    try:
        name = update.message.chat.title
    except:
        pass
    if not name:
        try:
            name = update.message.chat.first_name + ' ' + update.message.chat.last_name
        except:
            try:
                name = update.message.chat.username
            except:
                pass
    logger.info(f'Stop in chat {chat_id}, title {name}')
    if database.del_chat(chat_id):
        context.bot.send_message(chat_id=chat_id, text='bot stopped')
    else:
        context.bot.send_message(chat_id=chat_id, text='Something went wrong')

def one_three_three_seven(context: CallbackContext):
    chats = database.get_chats()
    logger.info(f'1337 call in {len(chats)} chats')
    t = get_text()
    for c in chats:
        context.bot.send_message(chat_id=c, text=t)


def main() -> None:
    updater = Updater(bot_token)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("stop", stop))

    j = updater.job_queue
    job_daily = j.run_daily(one_three_three_seven, days=(0, 1, 2, 3, 4, 5, 6), time=datetime.time(hour=13, minute=37, tzinfo=pytz.timezone('Europe/Moscow')))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
