import telebot
import os

BOT_TOKEN = os.getenv("BOT_TOKEN", "8161027017:AAEJMtVQqepwUoHsPlRYn7UAsV3wFCfj4Qc")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hola, soy LumiBot y estoy online 💫")

if __name__ == "__main__":
    print("✅ LumiBot corriendo en modo producción...")
    try:
        bot.infinity_polling()
    except Exception as e:
        print(f"⛔ Error al iniciar LumiBot: {e}")
