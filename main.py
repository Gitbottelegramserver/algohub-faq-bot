from telegram.ext import Application
from final_telegram_bot import get_handlers  # импортируем обработчики из final_telegram_bot.py

import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")  # или замени на прямую строку: TOKEN = "твой_токен"

def main():
    app = Application.builder().token(TOKEN).build()

    for handler in get_handlers():
        app.add_handler(handler)

    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()
