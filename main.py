from fastapi import FastAPI
from reactpy import component, html
from reactpy.backend.fastapi import configure

app = FastAPI()


@component
def Task(task):

    def handle_click():
        print("Borrado")

    if task["Priority"] == 1:
        return html.li({
            "key": task["id"],
            "style": {
                "background": "blue",
                "padding": "1rem",
                "border": "1px solid black",
                "margin": "1rem",
                "color": "white"
            }
        },
            f"⚠️ {task['text']} - {task['Priority']}")
    else:
        return html.li({
            "key": task["id"],
            "style": {
                "background": "green",
                "padding": "1rem",
                "border": "1px solid black",
                "margin": "1rem",
                "color": "white"
            }
        },
             html.div(
            {"style": {
                "display": "flex",
                "justify-content": "space-between"
            }},
            f"{task['text']} - {task['Priority']}",
            " ",
            html.button(
            {"style" : {
                "background": "red",
                "color": "white",
            }},
            
            "Borrar")
            )
             )
             


@component
def TasksList():
    tasks = [
        {"id": 0, "text": "Make Breakfast", "Priority": 1},
        {"id": 1, "text": "Make Dinner", "Priority": 2},
        {"id": 2, "text": "Make Bed", "Priority": 3},
        {"id": 3, "text": "Do Homework", "Priority": 1},
    ]

    # Recorre la lista, es como si fuera un map de javascript.
    lis = [Task(task) for task in tasks]
    return html.ul(lis)


@component
def App():
    return html.main(
        {"style": {
            "text-align": "center"
        }},
        html.h1(
        {"style": {
            "color": "lightblue"
        }},
        "Lista de Tareas"),
        html.div(TasksList())
    )


configure(app, App)
