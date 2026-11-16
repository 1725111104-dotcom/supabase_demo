import os
from supabase import create_client, Client
from dotenv import load_dotenv
import hashlib
import hmac
from typing import Any, cast
import logging

load_dotenv()
logger = logging.getLogger(__name__)

class ModelContactos:

    def __init__(self) -> None:
        try:
            self.supabase: Client = create_client(
                os.environ.get("SUPABASE_URL" , ""),
                os.environ.get("SUPABASE_KEY" , "")
            )
            # Clave secreta para firmar los ID (se guarda en el archivo .env)
            self.SECRET_KEY = os.environ.get("SECRET_KEY", "").encode("utf-8")
        except Exception as error:
            logger.error("ERROR 100: %s", error)
            print(f"ERROR 100: {error}")

    # Genera un hash único a partir del ID. Convierte 5 en '5:<firma>'
    def generar_hash(self, id: int) -> str:
        try:
            mensaje = str(id).encode("utf-8")
            firma = hmac.new(self.SECRET_KEY, mensaje, hashlib.sha256).hexdigest()
            # Concatena el id:firma
            return f"{id}:{firma}"
        except Exception as error:
            logger.error("ERROR 106: %s", error)
            print(f"ERROR 106: {error}")
            return ""

    # Valida el hash recibido. Devuelve el id si la firma es válida; si no, None
    def validar_hash(self, hash_a_validar: str) -> int | None:
        try:
            # Separa el id, el separador y la firma
            id_str, sep, _ = hash_a_validar.partition(":")

            # Solo calculamos el hash si la estructura básica es válida
            if sep and id_str.isdigit():
                token_esperado = self.generar_hash(int(id_str))
                if hmac.compare_digest(token_esperado, hash_a_validar):
                    return int(id_str)
            return None
        except Exception as error:
            logger.error("ERROR 107: %s", error)
            print(f"ERROR 107: {error}")
            return None

    #Devuelve todos los contactos de la tabla contactos
    def obtenerContactos(self):
        try:
            #SELECT * FROM contactos;
            response = self.supabase.table("contactos").select("*").execute()
            registros = response.data or []
            # Cambia cada id real por su hash firmado antes de enviarlo a la vista
            for registro in registros:
                registro["id_contacto"] = self.generar_hash(int(registro["id_contacto"])) # type: ignore
            return registros

        except Exception as error:
            logger.error("ERROR 101: %s", error)
            print(f"ERROR 101: {error}")
            return []

    #Devuelve un contacto específico de la tabla de contactos según el id del contacto proporcionado
    def buscarContacto(self, id_contacto:str):
        try:
            id = self.validar_hash(id_contacto)
            # Si la firma no es válida (ID manipulado) no consultamos la base de datos
            if id is None:
                return []
            response = self.supabase.table("contactos").select("*").eq("id_contacto", id).execute()
            return response.data

        except Exception as error:
            logger.error("ERROR 102: %s", error)
            print(f"ERROR 102: {error}")
            return []

    #Inserta un nuevo contacto en la tabla de contactos
    #El try y el except sirve para ver errores de manera más facil. Podemos ponerle cualquier número pero conviene hacerlos desde el 100
    def insertarContacto(self, nombre:str,  telefono:str, email:str):
        try:
            nuevo_contacto = {
            "nombre": nombre,
            "telefono": telefono,
            "email": email
            }
            response = self.supabase.table("contactos").insert(nuevo_contacto).execute()
            return response.data
        except Exception as error:
            logger.error("ERROR 103: %s", error)
            print(f"ERROR 103: {error}")

    #Borrar a un contacto
    def borrarContacto(self, id_contacto:str):
        try:
            id = self.validar_hash(id_contacto)
            if id is None:
                return []
            response = self.supabase.table("contactos").delete().eq("id_contacto", id).execute()
            return response.data
        except Exception as error:
            logger.error("ERROR 104: %s", error)
            print(f"ERROR 104: {error}")

    #Editar la información de un contacto
    def actualizarContacto(self, id_contacto:str, nombre:str, telefono:str, email:str):
        try:
            id = self.validar_hash(id_contacto)
            if id is None:
                return []
            editar_contacto = {
                "nombre": nombre,
                "telefono": telefono,
                "email": email
            }
            response = self.supabase.table("contactos").update(editar_contacto).eq("id_contacto", id).execute()
            return response.data
        except Exception as error:
            logger.error("ERROR 105: %s", error)
            print(f"ERROR 105: {error}")

if __name__ == "__main__":
    model_contactos = ModelContactos()
    #print(model_contactos.obtenerContactos())
    #print(model_contactos.buscarContacto(2))
    print(model_contactos.insertarContacto("Emi", "emi@email.com", "1414141414"))
    #print(model_contactos.borrarContacto(1))
    #print(model_contactos.actualizarContacto(2, "Ramiro", "rami@email.com", "121212121212"))
