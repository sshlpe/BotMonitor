import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from telegram.ext import CommandHandler
from dotenv import load_dotenv

from users import guardar_chat_id, eliminar_chat_id
from scrapper import scrapper

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
INTERVALO_MINUTOS = 10

async def registrar_usuario(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    guardar_chat_id(chat_id)
    await context.bot.send_message(chat_id=chat_id, text="¡Te has registrado para recibir alertas!")

async def eliminar_usuario(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    eliminar_chat_id(chat_id)
    await context.bot.send_message(chat_id=chat_id, text="¡Te has eliminado de la lista de alertas! Envia cualquier cosa para volver a registrarte.")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", registrar_usuario))
    app.add_handler(CommandHandler("stop", eliminar_usuario))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, registrar_usuario))

    app.job_queue.run_repeating(scrapper, interval=INTERVALO_MINUTOS * 60)

    print("🤖 Bot activo y scrapper en marcha...")
    app.run_polling()


if __name__ == "__main__":
    main() 