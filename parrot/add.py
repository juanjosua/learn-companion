from telegram.ext import CallbackContext
from telegram import Update

def new_word(update: Update, context: CallbackContext) -> None:

	# Use this function to submit new word
	word = str(context.args[0]).lower()

	reply = "Please add the translation of the new word."
	update.message.reply_text(reply)