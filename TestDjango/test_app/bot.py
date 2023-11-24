import os
from decouple import config
from telebot import TeleBot

TELEGRAM_BOT_TOKEN = config('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = config('TELEGRAM_CHAT_ID')


bot = TeleBot((TELEGRAM_BOT_TOKEN), threaded=False)


def bot_save():
    bot.send_message(chat_id=TELEGRAM_CHAT_ID, text='Были добавлены данные')


def bot_delete():
    bot.send_message(chat_id=TELEGRAM_CHAT_ID, text='Были удалены данные')