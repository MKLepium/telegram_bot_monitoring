import telebot
import dotenv
import os
import logging

import subprocess

# Define the command you want to run
command = "docker ps"

# Run the command using subprocess
try:
    output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
    print("Docker PS Output:")
    print(output)
except subprocess.CalledProcessError as e:
    print(f"Error running command: {e.returncode}")
    print(e.output)


dotenv.load_dotenv()

token = os.getenv('TELEGRAM_TOKEN')
if token is None:
    raise Exception('TELEGRAM_TOKEN not found in .env file')
bot = telebot.TeleBot(token)

# Enable logging
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

@bot.message_handler(commands=['start'], func=lambda message: message.chat.type == 'group')
def send_welcome(message):
    logger.info("start command received")
    logger.debug(message.chat.id)
    logger.debug(message.chat.type)
    logger.debug(message.chat)

    if message.chat.type == 'private':
        bot.reply_to(message, "Why are you here? This is private")
    else:
        bot.reply_to(message, "Hello, I'm here!")

@bot.message_handler(commands=['stop'], func=lambda message: message.chat.type == 'group')
def stop(message):
    logger.info("stop command received")
    logger.debug(message.chat.id)
    logger.debug(message.chat.type)
    logger.debug(message.chat)
    bot.reply_to(message, "Bye!")
    bot.stop_polling()
    exit()


# print the group id
@bot.message_handler(commands=['groupid']) 
def send_groupid(message):
    bot.reply_to(message, message.chat.id)

# bot.infinity_polling(skip_pending=True)
