import telebot

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
API_TOKEN = '7853315027:AAFy10-jl25Rz2UJV7fkL55HCTBw8AH_GMY'

bot = telebot.TeleBot(API_TOKEN)

# Command handler for the /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! I'm your simple bot. Type /help to see available commands.")

# Command handler for the /help command
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Available commands:\n/start - Start the bot\n/help - Show help information")

# Command handler for text messages (default handler)
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"You said: {message.text}")

# Start polling
if __name__ == "__main__":
    bot.polling()
