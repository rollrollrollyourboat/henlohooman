from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import joke_teller as jokes
import joke_filter as jokeFilter
import image_filter as images

import logging

updater = Updater(token='780805165:AAEdreGeX_G1ECiU6dWo2cF9UHrk545agAw')

dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)

joke_teller = jokes.JokeTeller();

def start(bot, update):
  bot.send_message(chat_id=update.message.chat_id, text="Henlo hooman! Tell me how are you feeling today! 😌")

def imageMesg(bot, update):
  bot.send_photo(chat_id=update.message.chat_id, photo=open('Images/corgi.jpg', 'rb'))  
  
def getJoke(bot, update):
  bot.send_message(chat_id=update.message.chat_id, text=joke_teller.pollJoke())
  
#initialise the class
image_filter = images.ImageFilter()
joke_filter = jokeFilter.JokeFilter();

start_handler = CommandHandler('start', start)
getJoke_handler = MessageHandler(joke_filter, getJoke)
image_handler = MessageHandler(image_filter, imageMesg)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(getJoke_handler)
dispatcher.add_handler(image_handler)

updater.start_polling()