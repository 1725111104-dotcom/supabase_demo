import os
from supabase import create_client, Client
from dotenv import load_dotenv
import logging 

#Lee las variables de entorno del archivo .env
load_dotenv()

# Configura los sistemas de logging para capturar errores y eventos importantes
logger = logging.getLogger(__name__)

class AuthUsers:

    # Inicializa la clase AuthUsers y establece la conexión con Supabase
    def __init__(self) -> None:
        try:
            self.supabase: Client = create_client(
                os.environ.get("SUPABASE_URL" , ""),
                os.environ.get("SUPABASE_KEY" , "")
            )

        except Exception as error:
            logger.error("ERROR 100: %s", error)
            print(f"ERROR 100: {str(error)}")

    # Método para iniciar sesión en Supabase utilizando correo electrónico y contraseña
    def iniciarSesion(self, email: str, password: str)->str | None:
        try:
            # Inicia sesión en Supabase utilizando el correo electrónico y la contraseña creados en supabase
            response = self.supabase.auth.sign_in_with_password(
                {
                    "email": email,
                    "password": password
                }
            )

            return response.session.access_token #type: ignore
        # Si ocurre un error durante el inicio de sesión, se captura la excepción y se registra en el sistema de logging
        except Exception as error:
            logger.error("ERROR 101: %s", error)
            print(f"ERROR 101: {str(error)}")
            return None


    def registrarUsuario(self, email: str, password: str) -> str | None:
        try:
            # Registra un nuevo usuario en Supabase utilizando el correo electrónico y la contraseña
            response = self.supabase.auth.sign_up(
                {
                    "email": email,
                    "password": password
                }
            )
            print(f"Usuario creado exitosamente")
            print(response) #type: ignore
            return response.user.id #type: ignore
        except Exception as error:
            logger.error(f"ERROR 102: {str(error)}")
            print(f"ERROR 102: {str(error)}")
            return None

if __name__ == "__main__":
    #print("Autenticación de usuarios")
    print("Registrar nuevos usuarios")
    objeto = AuthUsers()
    #print(objeto.iniciarSesion("lalito@gmail.com", "12345678"))
    print(objeto.registrarUsuario("lalona@gmail.com", "87654321"))
