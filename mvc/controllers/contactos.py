import web
from mvc.models.model_contactos import ModelContactos

render = web.template.render('mvc/views', base='template')

class Contactos:

    def GET(self):

        model_contactos = ModelContactos()

        #Almacena en datos los registros recibidos en Supabase
        datos = model_contactos.obtenerContactos()
        
        print(datos)
        # el print es la linea que imprime los datos que se reciben de la base de datos

        return render.contactos(datos) # type: ignore
        #Envía a contactos.html los datos de Supabase