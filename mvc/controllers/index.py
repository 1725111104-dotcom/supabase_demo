import web

render = web.template.render('mvc/views', base='template')
#Un programa en python debe de tener un salto de linea extra para que pueda leer el archivo (a eso se le llama cerrar una tubería)
class Index:
    def GET(self):
        return render.index()
