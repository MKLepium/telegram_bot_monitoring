import telebot
import dotenv
import os
import logging

dotenv.load_dotenv()

token = os.getenv('TELEGRAM_TOKEN')
if token is None:
    raise Exception('TELEGRAM_TOKEN not found in .env file')
bot = telebot.TeleBot(token)

# Enable logging
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	logger.info("start command received")
	logger.debug(message.chat.id)
	logger.debug(message.chat.type)
	logger.debug(message.chat)

    if message.chat.type == 'private':
        bot.reply_to(message, "Why are you here? This is private")
    else:
        bot.reply_to(message, "Hello, I'm here!")

@bot.message_handler(commands=['stop'])
def stop(message):
	logger.info("stop command received")
	logger.debug(message.chat.id)
	logger.debug(message.chat.type)
	logger.debug(message.chat)
    bot.reply_to(message, "Bye!")
	exit()


# print the group id
@bot.message_handler(commands=['groupid']) 
def send_groupid(message):
    bot.reply_to(message, message.chat.id)

bot.infinity_polling()
