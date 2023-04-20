from telegram import Bot

# replace <BOT_TOKEN> with your bot token
bot = Bot(token="<BOT_TOKEN>")

# replace <NUMERIC_USER_ID> with the actual numeric user ID
user_id = "<NUMERIC_USER_ID>"

# replace <MESSAGE_TEXT> with the message you want to send
message_text = "Hi, @" + user_id + " - this is a message for you!"

# send the message to the user
bot.send_message(chat_id=user_id, text=message_text)

from telegram.ext import Updater, MessageHandler, Filters

# replace <BOT_TOKEN> with your bot token
updater = Updater(token="<BOT_TOKEN>", use_context=True)

def replace_word(update, context):
    # get the user input message
    message = update.message.text

    # replace the word "old_word" with "new_word"
    new_message = message.replace("old_word", "new_word")

    # send the new message back to the user
    update.message.reply_text(new_message)

# define a MessageHandler with the "Filters.text" filter to handle text messages
message_handler = MessageHandler(Filters.text, replace_word)
