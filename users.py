import os 

ARCHIVO_USUARIOS = "users.txt"

def guardar_chat_id(chat_id):
    if not os.path.exists(ARCHIVO_USUARIOS):
        with open(ARCHIVO_USUARIOS, "w") as f:
            pass
    with open(ARCHIVO_USUARIOS, "r") as f:
        ids_existentes = {line.strip() for line in f if line.strip()}

    if str(chat_id) not in ids_existentes:
        with open(ARCHIVO_USUARIOS, "a") as f:
            f.write(f"{chat_id}\n")
        print(f"✅ Nuevo usuario registrado: {chat_id}")
    else:
        print(f"🟡 Usuario ya registrado: {chat_id}")

def eliminar_chat_id(chat_id):
    if not os.path.exists(ARCHIVO_USUARIOS):
        return
    with open(ARCHIVO_USUARIOS, "r") as f:
        ids_existentes = {line.strip() for line in f if line.strip()}
    
    if str(chat_id) in ids_existentes:
        with open(ARCHIVO_USUARIOS, "w") as f:
            for id in ids_existentes:
                if id != str(chat_id):
                    f.write(f"{id}\n")
        print(f"❌ Usuario eliminado: {chat_id}")
    else:
        print(f"🟡 Usuario no registrado: {chat_id}")

def get_chat_ids():
    if not os.path.exists(ARCHIVO_USUARIOS):
        return []
    with open(ARCHIVO_USUARIOS, "r") as f:
        return [line.strip() for line in f if line.strip()]