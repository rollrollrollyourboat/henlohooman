from telegram.ext import BaseFilter

class ImageFilter(BaseFilter): 
	def filter(self, message): 
		for word in ['image', 'pic', 'photo']:
			if word in message.text:
				return True

		return False