import os
from datetime import time, timedelta
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from telegram.ext import CommandHandler
from dotenv import load_dotenv

from users import guardar_chat_id, eliminar_chat_id, get_chat_ids
from scrapper import scrapper

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
INTERVALO_MINUTOS = 5

async def registrar_usuario(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    guardar_chat_id(chat_id)
    await context.bot.send_message(chat_id=chat_id, text="¡Te has registrado para recibir alertas!")

async def eliminar_usuario(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    eliminar_chat_id(chat_id)
    await context.bot.send_message(chat_id=chat_id, text="¡Te has eliminado de la lista de alertas! Envia cualquier cosa para volver a registrarte.")

async def keepalive(context: ContextTypes.DEFAULT_TYPE):
    print("⏳ Keepalive ping...")

async def keepnotice(context: ContextTypes.DEFAULT_TYPE):
    for chat_id in get_chat_ids():
        await context.bot.send_message(chat_id=chat_id, text="¡Buenos días! El bot está activo monitoreando cambios. Te avisaremos si detectamos novedades.")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", registrar_usuario))
    app.add_handler(CommandHandler("stop", eliminar_usuario))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, registrar_usuario))

    app.job_queue.run_repeating(scrapper, interval=INTERVALO_MINUTOS * 60, first=0, name="scrapper")
    app.job_queue.run_repeating(keepalive, interval=60, first=10, name="keepalive")
    app.job_queue.run_daily(keepnotice, time=time(13, 0), name="keepnotice")

    print("🤖 Bot activo y scrapper en marcha...")
    app.run_polling()

if __name__ == "__main__":
    main()