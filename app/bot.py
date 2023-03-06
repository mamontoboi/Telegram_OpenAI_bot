import os
import telebot
from dotenv import load_dotenv
from .ai.ai_chat import interaction

load_dotenv()

telebot_token = os.getenv('TELEGRAM_TOKEN')

bot = telebot.TeleBot(token=telebot_token, parse_mode=None)


@bot.message_handler(commands=['ai', 'start'])
def ai_handler(message):
    if message.text == '/ai':
        bot.reply_to(message, 'Start your question with /ai.')
    elif message.text == '/start':
        bot.reply_to(message, 'Hi! Write you question after /ai')
    else:
        clear_message = message.text.replace('/ai', '')
        response = interaction(clear_message)
        data = response['choices'][0]['text']
        bot.reply_to(message, data)
