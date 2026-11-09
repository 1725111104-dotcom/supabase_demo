import web
from mvc.controllers.index import Index
from mvc.controllers.contactos import Contactos
from mvc.controllers.insertar_contacto import InsertarContacto
from mvc.controllers.ver_contacto import VerContacto
from mvc.controllers.borrar_contacto import BorrarContacto

#Evita que nos muestre la página de error
web.config.debug = False

#**Importación explicita (es más recomendada)
#Este archivo app esta utilizado como un router en este proyecto
urls = (
    '/', 'Index',
    '/contactos', 'Contactos',
    #**Otra forma de importar ('/contactos', 'mvc.controllers.contactos.Contactos',)
    '/insertar_contacto', 'InsertarContacto',
    '/ver_contacto/(.*)', 'VerContacto',
    # Con /(.*) Ayuda a poder recibir los valores de los ID
    '/borrar_contacto/(.*)', 'BorrarContacto'
    '/actualizar_contacto/(.*)', 'ActualizarContacto'
)
app = web.application(urls, globals())


if __name__ == "__main__":
    app.run()