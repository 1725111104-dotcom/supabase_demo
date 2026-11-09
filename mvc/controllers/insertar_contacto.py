import web
from mvc.models.model_contactos import ModelContactos

render = web.template.render('mvc/views', base='template')

class InsertarContacto:

    # Renderizar el archivo insertar_contacto.html(ver la página)
    def GET(self):
        return render.insertar_contacto() #type: ignore

    # Recibe los input del formulario y accede a cada uno
    # utilizando el atributo 'name'
    def POST(self):
        # Accede a los datos del formulario 'contactos'
        formulario = web.input()
        #Obtiene el valor del input nombre
        nombre = formulario['nombre']
        #Obtiene el valor del input email
        email = formulario['email']
        #Obtiene el valor del input telefono
        telefono = formulario['telefono']

        # Imprime los datos para verificar que se obtienen los valores
        # de forma correcta
        #print(f"Nombre: {nombre}")
        #print(f"Email: {email}")
        #print(f"Teléfono: {telefono}")

        model_contactos = ModelContactos()

        datos = model_contactos.insertarContacto(nombre,email,telefono)

        # Línea agregada por mí para renderizar la página
        web.header('Content-Type', 'text/html')
        html = """
            <h1>Contacto almacenado correctamente</h1>
            <a href='/contactos'>Regresar</a>
        """
        return html

