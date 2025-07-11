import gspread
from oauth2client.service_account import ServiceAccountCredentials

SCOPE = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
CREDS_FILE = "/etc/secrets/service_account.json"
SHEET_NAME = "TelegramUsers"

def get_sheet():
    creds = ServiceAccountCredentials.from_json_keyfile_name(CREDS_FILE, SCOPE)
    client = gspread.authorize(creds)
    sheet = client.open(SHEET_NAME).sheet1
    return sheet

def guardar_chat_id(chat_id):
    sheet = get_sheet()
    existing_ids = sheet.col_values(1)
    if str(chat_id) not in existing_ids:
        sheet.append_row([str(chat_id)])
        print(f"✅ Nuevo usuario agregado: {chat_id}")
    else:
        print(f"🟡 Usuario ya registrado: {chat_id}")

def eliminar_chat_id(chat_id):
    sheet = get_sheet()
    values = sheet.col_values(1)
    for idx, val in enumerate(values, start=1):
        if val == str(chat_id):
            sheet.delete_rows(idx)
            print(f"❌ Usuario eliminado: {chat_id}")
            return
    print(f"🟡 Usuario no encontrado: {chat_id}")

def get_chat_ids():
    return get_sheet().col_values(1)