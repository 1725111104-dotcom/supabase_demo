import web
from mvc.models.model_contactos import ModelContactos

render = web.template.render('mvc/views', base='template')

class BorrarContacto:

    def GET(self, id_contacto):

        model_contactos = ModelContactos()

        contacto = model_contactos.buscarContacto(id_contacto)

        print(contacto)

        return render.borrar_contacto(contacto) #type: ignore