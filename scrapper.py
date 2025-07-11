from telegram.ext import ContextTypes
import requests
from bs4 import BeautifulSoup

from users import get_chat_ids

URL = "https://www.mifuturo.cl/bases-de-datos-de-matriculados/"
TEXTO_BUSCADO = "2025"

def obtener_html():
    try:
        response = requests.get(URL, timeout=10)
        response.raise_for_status()  # lanza excepción si hay error HTTP
        return response.text
    except Exception as e:
        print(f"Error al obtener la página: {e}")
        return None

def analizar_html(html, texto_buscado="2025"):
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text()
    return texto_buscado in text


async def scrapper(context: ContextTypes.DEFAULT_TYPE):
    print("🔍 Ejecutando scrapper...")
    try:
        html = obtener_html()
        if html and analizar_html(html):
            print(f"✅ ¡Texto '{TEXTO_BUSCADO}' encontrado!")
            for chat_id in get_chat_ids():
                await context.bot.send_message(
                    chat_id=chat_id,
                    text=f"📢 Alerta: se encontró '{TEXTO_BUSCADO}' en {URL}"
                )
        else:
            print(f"🟡 Texto '{TEXTO_BUSCADO}' no encontrado en {URL}")
    except Exception as e:
        print(f"❌ Error en el scrapper: {e}")



if __name__ == "__main__":
    html = obtener_html()
    if html:
        print(analizar_html(html))
