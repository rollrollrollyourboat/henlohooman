from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters, CallbackQueryHandler
import joke_giver as jokes
import image_giver as images
import gif_giver as gifs
import sticker_giver as stickers
import joke_filter as jokeFilter
import image_filter as imageFilter
import gif_filter as gifFilter
import sticker_filter as stickerFilter
import small_talk as smallTalk
import unglamSticker_filter as unglamStickerFilter 
import unglamsticker_giver as unglamstickers
import short_sentence_response as shortSentenceResponse

import logging

updater = Updater(token='780805165:AAEdreGeX_G1ECiU6dWo2cF9UHrk545agAw')

dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)

joke_giver = jokes.JokeGiver();
image_giver = images.ImageGiver();
gif_giver = gifs.GifGiver();
sticker_giver = stickers.StickerGiver();
small_talk = smallTalk.SmallTalkSender();
unglamsticker_giver = unglamstickers.UnglamStickerGiver();

def start(bot, update):
  keyboard = [[InlineKeyboardButton("Happy", callback_data='happy'),
               InlineKeyboardButton("Sad", callback_data='sad')],
               [InlineKeyboardButton("Feel like a doggo", callback_data='doggo')]];

  reply_markup = InlineKeyboardMarkup(keyboard);

  bot.send_message(chat_id=update.message.chat_id, text="Henlo hooman {}! 😌".format(update.message.from_user.first_name))
  update.message.reply_text('Tell me how are you feeling todayz!',
                            reply_markup=reply_markup);

def response(bot, update):
  query = update.callback_query

  small_talk.setMood(query.data);

  if query.data == 'doggo':
    bot.edit_message_text(text="doggo am unsure if hoOman is doggo or doggo is hOoman\nBut doggo can gives stickers / Gifs / Jokes / piktares upaw request\nSo let doggo knows what hoOman(or doggo) wants!",
                        chat_id=query.message.chat_id,
                        message_id=query.message.message_id);
  elif query.data == 'happy':
    bot.edit_message_text(text="Even if hOoman is happy, doggo am here to make it better!\ndoggo can gives stickers / Gifs / Jokes / piktares upaw request\nSo let doggo knows what hoOman wants!",
                        chat_id=query.message.chat_id,
                        message_id=query.message.message_id);
  else:
    bot.edit_message_text(text="OH NO! doggo am sed hoOman is sad\nBork is okay! Doggo am here to make it better!\ndoggo can gives stickers / Gifs / Jokes / piktares upaw request\nSo let doggo knows what hoOman wants!",
                        chat_id=query.message.chat_id,
                        message_id=query.message.message_id);

def getImage(bot, update):
  bot.send_photo(chat_id=update.message.chat_id, photo=open(image_giver.pollImage(), 'rb'))  
  bot.send_message(chat_id=update.message.chat_id, text=small_talk.pollSmallTalk())
  
def getJoke(bot, update):
  bot.send_message(chat_id=update.message.chat_id, text=joke_giver.pollJoke())
  bot.send_message(chat_id=update.message.chat_id, text=small_talk.pollSmallTalk())

def getGif(bot, update):
  bot.send_animation(chat_id=update.message.chat_id, animation=gif_giver.pollGif())
  bot.send_message(chat_id=update.message.chat_id, text=small_talk.pollSmallTalk())

def getSticker(bot, update):
  bot.send_sticker(chat_id=update.message.chat_id, sticker=sticker_giver.pollSticker())
  bot.send_message(chat_id=update.message.chat_id, text=small_talk.pollSmallTalk())

def getUnglamSticker(bot, update):
  bot.send_sticker(chat_id=update.message.chat_id, sticker=unglamsticker_giver.pollUnglamSticker())
  bot.send_message(chat_id=update.message.chat_id, text="here is unglam for hOOman")

def getShortSentenceResponse(bot, update):
  bot.send_message(chat_id=update.message.chat_id, text="doggo unsure what hOOman wans\nhOoman pls tolk in smol sentences\nIf hoOman is unsure, doggo can gives stickers / Gifs / Jokes / piktares upaw request")
  
def default(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="doggo am no undstands hoOoman\nIf hoOman is unsure, doggo can gives stickers / Gifs / Jokes / piktares upaw request")

#initialise the class
image_filter = imageFilter.ImageFilter()
joke_filter = jokeFilter.JokeFilter();
gif_filter = gifFilter.GifFilter()
sticker_filter = stickerFilter.StickerFilter();
unglamSticker_filter = unglamStickerFilter.UnglamStickerFilter()
shortSentence_filter = shortSentenceResponse.ShortSentenceResponse()


start_handler = CommandHandler('start', start)
response_handler = CallbackQueryHandler(response)
joke_handler = MessageHandler(joke_filter, getJoke)
image_handler = MessageHandler(image_filter, getImage)
gif_handler = MessageHandler(gif_filter, getGif)
sticker_handler = MessageHandler(sticker_filter, getSticker)
unglamSticker_handler = MessageHandler(unglamSticker_filter, getUnglamSticker)
shortSentence_handler = MessageHandler(shortSentence_filter, getShortSentenceResponse)
default_handler = MessageHandler(Filters.text, default)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(response_handler)
dispatcher.add_handler(joke_handler)
dispatcher.add_handler(image_handler)
dispatcher.add_handler(gif_handler)
dispatcher.add_handler(sticker_handler)
dispatcher.add_handler(unglamSticker_handler)
dispatcher.add_handler(shortSentence_handler)
dispatcher.add_handler(default_handler)

updater.start_polling()