from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import joke_teller as jokes
import image_giver as images
import joke_filter as jokeFilter
import image_filter as imageFilter
import gif_filter as gifFilter

import logging

updater = Updater(token='780805165:AAEdreGeX_G1ECiU6dWo2cF9UHrk545agAw')

dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)

joke_teller = jokes.JokeTeller();
image_giver = images.ImageGiver();

def start(bot, update):
  bot.send_message(chat_id=update.message.chat_id, text="Henlo hooman! Tell me how are you feeling today! 😌")

def imageMesg(bot, update):
  bot.send_photo(chat_id=update.message.chat_id, photo=open(image_giver.pollImage(), 'rb'))  
  
def getJoke(bot, update):
  bot.send_message(chat_id=update.message.chat_id, text=joke_teller.pollJoke())

def getGifs(bot, update):
  link = "https://media.tenor.com/images/6f61d7cc7cecb9c2046f4baf0e71d006/tenor.gif"
  bot.send_animation(chat_id=update.message.chat_id, animation=link)
  
#initialise the class
image_filter = imageFilter.ImageFilter()
joke_filter = jokeFilter.JokeFilter();
gif_filter = gifFilter.GIFFilter()


start_handler = CommandHandler('start', start)
getJoke_handler = MessageHandler(joke_filter, getJoke)
image_handler = MessageHandler(image_filter, imageMesg)
gif_handler = MessageHandler(gif_filter, getGifs)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(getJoke_handler)
dispatcher.add_handler(image_handler)
dispatcher.add_handler(gif_handler)

updater.start_polling()