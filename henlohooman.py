from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import joke_teller as jokes
import joke_filter as jokeFilter
import logging

updater = Updater(token='780805165:AAEdreGeX_G1ECiU6dWo2cF9UHrk545agAw')

dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)

joke_teller = jokes.JokeTeller();
joke_filter = jokeFilter.JokeFilter();

def start(bot, update):
  bot.send_message(chat_id=update.message.chat_id, text="Henlo hooman! Tell me how are you feeling today! 😌")

def getJoke(bot, update):
  bot.send_message(chat_id=update.message.chat_id, text=joke_teller.pollJoke())

start_handler = CommandHandler('start', start)
getJoke_handler = MessageHandler(joke_filter, getJoke)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(getJoke_handler)

updater.start_polling()
