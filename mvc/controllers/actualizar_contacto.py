import web
from mvc.models.model_contactos import ModelContactos

render = web.template.render('mvc/views', base='template')

class ActualizarContacto:

    def GET(self, id_contacto):

        model_contactos = ModelContactos()

        contacto = model_contactos.buscarContacto(id_contacto)

        print(contacto)

        return render.actualizar_contacto(contacto) #type: ignore