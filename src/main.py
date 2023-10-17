import telebot
import dotenv
import os

dotenv.load_dotenv()

token = os.getenv('TELEGRAM_TOKEN')
if token is None:
    raise Exception('TELEGRAM_TOKEN not found in .env file')
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    if message.chat.type == 'private':
        bot.reply_to(message, "Why are you here? This is private")
    else:
        bot.reply_to(message, "Hello, I'm here!")

@bot.message_handler(commands=['stop'])
def stop(message):
	bot.reply_to(message, "Bye!")
	bot.stop_polling()

# print the group id
@bot.message_handler(commands=['groupid'])
def send_groupid(message):
	bot.reply_to(message, message.chat.id)



bot.infinity_polling()
