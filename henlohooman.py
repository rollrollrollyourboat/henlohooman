from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import joke_teller as jokes
import joke_filter as jokeFilter
import image_filter as images
import sticker_filter as stickerFilter
import send_sticker as stickers

import logging

updater = Updater(token='780805165:AAEdreGeX_G1ECiU6dWo2cF9UHrk545agAw')

dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)

joke_teller = jokes.JokeTeller();
joke_filter = jokeFilter.JokeFilter();
sticker_sender = stickers.StickerSender();
sticker_filter = stickerFilter.StickerFilter();

def start(bot, update):
  bot.send_message(chat_id=update.message.chat_id, text="Henlo hooman! Tell me how are you feeling today! 😌")

def imageMesg(bot, update):
  # bot.send_message(chat_id=update.message.chat_id, text = "Image Detected :D")
  bot.send_photo(chat_id=update.message.chat_id, photo=open('Images/corgi.jpg', 'rb'))  
  
def getJoke(bot, update):
  bot.send_message(chat_id=update.message.chat_id, text=joke_teller.pollJoke())

def sendSticker(bot, update):
  bot.send_sticker(chat_id=update.message.chat_id, sticker=sticker_sender.pollSticker())
  
#initialise the class
image_filter = images.ImageFilter()

start_handler = CommandHandler('start', start)
getJoke_handler = MessageHandler(joke_filter, getJoke)
image_handler = MessageHandler(image_filter, imageMesg)
sticker_handler = MessageHandler(sticker_filter, sendSticker)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(getJoke_handler)
dispatcher.add_handler(image_handler)
dispatcher.add_handler(sticker_handler)

updater.start_polling()