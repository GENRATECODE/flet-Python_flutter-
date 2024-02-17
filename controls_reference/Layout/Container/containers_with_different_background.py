import flet as ft
from flet import *

def main(page: Page):
    page.title = "Hello, Azure!"

    # Add a simple text part to the body of the email.
    container_first=ft.Container(
        content=ElevatedButton("Elevated Button in Container",),
        bgcolor="#C499F3",
        padding=10,
    )
    c2=ft.Container(
        content=ft.ElevatedButton(
            "Elevated Button with opcity=0.5 in container",opacity=0.5
        ),
        bgcolor="#739072",
        padding=10,
        width="30%",
        
    )
    c3=Container( content=ElevatedButton("Outlined Button in Container"),
        bgcolor= "#D6DBDF",
        padding=5,
    )
    
    
    page.add(container_first,c2,c3)
    
if __name__ =="__main__":
    app(target=main)