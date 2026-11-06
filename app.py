import web
from mvc.controllers.index import Index
from mvc.controllers.contactos import Contactos

#Evita que nos muestre la página de error
web.config.debug = False

#**Importación explicita (es más recomendada)
#Este archivo app esta utilizado como un router en este proyecto
urls = (
    '/', 'Index',
    '/contactos', 'Contactos',
    #**Otra forma de importar ('/contactos', 'mvc.controllers.contactos.Contactos',)
)
app = web.application(urls, globals())


if __name__ == "__main__":
    app.run()