import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

# Замени 'YOUR_TELEGRAM_BOT_TOKEN' на токен, который ты получил от @BotFather.
TOKEN = "8340939566:AAGIE4OpH5zAvJKdlUcjyi5_PoBJpV9RieM"

# Включим логирование, чтобы видеть, что происходит.
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)

# Это функция, которая будет запускаться, когда пользователь отправит команду /start.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Теперь мы используем адрес нашего локального сервера
    url = "http://127.0.0.1:8000"
    
    keyboard = [
        [
            InlineKeyboardButton("Открыть мою ферму 🚜", web_app=WebAppInfo(url=url))
        ]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Привет! Нажми на кнопку, чтобы начать управлять своей фермой.", reply_markup=reply_markup)
def main() -> None:
    """Запускаем бота."""
    # Создаём объект Application и передаём ему токен нашего бота.
    application = Application.builder().token(TOKEN).build()

    # Добавляем обработчик для команды /start.
    application.add_handler(CommandHandler("start", start))

    # Запускаем бота. Он будет работать, пока ты его не остановишь.
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()