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
        except Exception as error:
            logger.error(f"ERROR 100: {str(error)}")
            print(f"ERROR 100: {error.args[0]}")

    #Devuelve todos los contactos de la tabla contactos
    def obtenerContactos(self):
        try:
            #SELECT * FROM contactos;
            response = self.supabase.table("contactos").select("*").execute()
            return response.data

        except Exception as error:
            logger.error(f"ERROR 101: {str(error)}")
            print(f"ERROR 101:{error.args[0]}")

    #Devuelve un contacto específico de la tabla de contactos según el id del contacto proporcionado
    def buscarContacto(self, id_contacto:int):
        try:
            response = self.supabase.table("contactos").select("*").eq("id_contacto", id_contacto).execute()
            return response.data

        except Exception as error:
            logger.error(f"ERROR 102: {str(error)}")
            print(f"ERROR 102:{error.args[0]}")

    #Inserta un nuevo contacto en la tabla de contactos
    #El try y el except sirve para ver errores de manera más facil. Podemos ponerle cualquier número pero conviene hacerlos desde el 100
    def insertarContacto(self, nombre:str,telefono:str,email:str):
        try:
            nuevo_contacto = {
            "nombre": nombre,
            "telefono": telefono,
            "email": email
            }
            response = self.supabase.table("contactos").insert(nuevo_contacto).execute()
            return response.data
        except Exception as error:
            logger.error(f"ERROR 103: {str(error)}")
            print(f"ERROR 103:{error.args[0]}")
    
    #Borrar a un contacto
    def borrarContacto(self, id_contacto:int):
        try:
            response = self.supabase.table("contactos").delete().eq("id_contacto", id_contacto).execute()
            return response.data
        except Exception as error:
            logger.error(f"ERROR 104: {str(error)}")
            print(f"ERROR 104:{error.args[0]}")

    #Editar la información de un contacto
    def actualizarContacto(self, id_contacto,nombre:str,email:str,telefono:str):
        try:
            editar_contacto = {
                "nombre": nombre,
                "email": email,
                "telefono": telefono
            }
            response = self.supabase.table("contactos").update(editar_contacto).eq("id_contacto", id_contacto).execute()
            return response.data
        except Exception as error:
            logger.error("ERROR 105: {str(error)}")
            print(f"ERROR 105:{error.args[0]}")

if __name__ == "__main__":
    model_contactos = ModelContactos()
    #print(model_contactos.obtenerContactos())
    #print(model_contactos.buscarContacto(2))
    print(model_contactos.insertarContacto("Emi", "emi@email.com", "1414141414"))
    #print(model_contactos.borrarContacto(1))
    #print(model_contactos.actualizarContacto(2, "Ramiro", "rami@email.com", "121212121212"))