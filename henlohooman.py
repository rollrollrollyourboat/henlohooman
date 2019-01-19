from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import joke_giver as jokes
import image_giver as images
import gif_giver as gifs
import sticker_giver as stickers
import joke_filter as jokeFilter
import image_filter as imageFilter
import gif_filter as gifFilter
import sticker_filter as stickerFilter


import logging

updater = Updater(token='780805165:AAEdreGeX_G1ECiU6dWo2cF9UHrk545agAw')

dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)

joke_giver = jokes.JokeGiver();
image_giver = images.ImageGiver();
gif_giver = gifs.GifGiver();
sticker_sender = stickers.StickerGiver();

def start(bot, update):
  bot.send_message(chat_id=update.message.chat_id, text="Henlo hooman! Tell me how are you feeling today! 😌")

def getImage(bot, update):
  bot.send_photo(chat_id=update.message.chat_id, photo=open(image_giver.pollImage(), 'rb'))  
  
def getJoke(bot, update):
  bot.send_message(chat_id=update.message.chat_id, text=joke_giver.pollJoke())

def getGif(bot, update):
  bot.send_animation(chat_id=update.message.chat_id, animation=gif_giver.pollGif())
  
def getSticker(bot, update):
  bot.send_sticker(chat_id=update.message.chat_id, sticker=sticker_giver.pollSticker())
  
#initialise the class
image_filter = imageFilter.ImageFilter()
joke_filter = jokeFilter.JokeFilter();
gif_filter = gifFilter.GifFilter()
sticker_filter = stickerFilter.StickerFilter();


start_handler = CommandHandler('start', start)
joke_handler = MessageHandler(joke_filter, getJoke)
image_handler = MessageHandler(image_filter, getImage)
gif_handler = MessageHandler(gif_filter, getGif)
sticker_handler = MessageHandler(sticker_filter, getSticker)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(joke_handler)
dispatcher.add_handler(image_handler)
dispatcher.add_handler(gif_handler)
dispatcher.add_handler(sticker_handler)

updater.start_polling()