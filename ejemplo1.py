from fastapi import FastAPI
from reactpy import component, html
from reactpy.backend.fastapi import configure

app = FastAPI()

@component
def App():
    return html.section(
       html.h1("My Tasks List"),
       html.ul(
        html.li("Aprende ReactPy"),
        html.li("Aprende FastApi"),
        html.li("Crea Interfaces Graficas con Python")        
       ),
       html.img({
           "src": "https://fastly.picsum.photos/id/866/200/300.jpg?hmac=rcadCENKh4rD6MAp6V_ma-AyWv641M4iiOpe1RyFHeI",
           "style": {
               "width": "300px",
               "height": "500px"
           }
       })
    )

configure(app, App)

