from telegram.ext import BaseFilter

class GifFilter(BaseFilter): 
	def filter(self, message): 
		for word in ['gif', 'GIF']:
			if word in message.text.lower():
				return True

		return False