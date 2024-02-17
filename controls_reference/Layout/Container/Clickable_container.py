import flet as ft
from flet import *
"""
    container introduction types container 
    with alignment of different types with help of row
    
"""
def main(page:Page):
    page.title="container-Clickable and not"
    page.vertical_alignment=MainAxisAlignment.CENTER
    page.horizontal_alignment=CrossAxisAlignment.CENTER
    
    row=Row([
        Container(
            content=Text("Non Clickable"),
            margin=10,
            padding=10,
            alignment=ft.alignment.center,
            bgcolor="#FFA500", #Orange color
            width=150,
            height=150,
            border_radius=100, # round corner 
        ),
        Container(
            content=ft.Text("Clickable without Ink"),
            margin=10,
            padding=10,
            alignment=ft.alignment.center,
            bgcolor="#59B4C3",
            width=150,
            height=150,
            border_radius=10,
            on_click= lambda e: print("Clickable without Ink Clicked!"),
        ),
        Container(
            content=ft.Text("CLickable with Ink"),
            margin=10,
            padding=10,
            alignment=ft.alignment.center,
            bgcolor="#74E291",
            width=150,
            height=150,
            border_radius=10,
            ink=True, 
            on_click=lambda e: print("Clickable with Ink Clicked!"), 
            
        ),
        ft.Container(
            content=Text("Clickable Blurred  with Ink"),
            margin=10,
            padding=10,
            alignment=ft.alignment.center,
            width=150,
            height=150,
            blur=ft.Blur(1011,10,ft.BlurTileMode.MIRROR),
            opacity=0.8,
            ink=True, 
            on_click=lambda e: print("Transparent clickable clicked!")
        ),
        ft.Container(
            content=Text("Clickable Transparent with Ink"),
            margin=10,
            padding=10, 
            alignment=ft.alignment.center,
            width=150,
            height=150, 
            opacity=0.8,
            ink=True, 
            on_click=lambda e: print("tRANSPARENT clickable clicked!"),
            key= "transparent",
        ) 
    ]
        , alignment=MainAxisAlignment.CENTER
    )
    
    # for alignment test
    row_align=Row(
        [  Container(content=Text("Center(0,0)",color="pink"),
                     margin=10,
                     padding=10,
                     alignment=alignment.center,
                     width=150,
                     height=150,
                     border_radius=10,
                     bgcolor="#59B4C3"
                     ),
        Container(content=Text("top_left",color="pink"),
                      margin=10,
                     padding=10,
                     alignment=alignment.top_left,
                     width=150,
                     height=150,
                     border_radius=10,
                     bgcolor="#59B4C3"),
        
        Container(content=Text("top_center",color="pink"),
                   margin=10,
                     padding=10,
                     alignment=alignment.top_center,
                     width=150,
                     height=150,
                     border_radius=10,
                     bgcolor="#59B4C3"),
        Container(content=Text("top_right",color="pink"),
                   margin=10,
                     padding=10,
                     alignment=alignment.top_right,
                     width=150,
                     height=150,
                     border_radius=10,
                     bgcolor="#59B4C3"),
        Container(content=Text("center_left",color="pink"),
                   margin=10,
                     padding=10,
                     alignment=alignment.center_left,
                     width=150,
                     height=150,
                     border_radius=10,
                     bgcolor="#59B4C3"),
        Container(content=Text("center_right",color="pink"),
                   margin=10,
                     padding=10,
                     alignment=alignment.center_right,
                     width=150,
                     height=150,
                     border_radius=10,
                     bgcolor="#59B4C3"),
        Container(content=Text("bottom_left",color="pink"),
                   margin=10,
                     padding=10,
                     alignment=alignment.bottom_left,
                     width=150,
                     height=150,
                     border_radius=10,
                     bgcolor="#59B4C3"),

         ],
       
       alignment=MainAxisAlignment.CENTER
    )
    row3=Row([  Container(content=Text("Bottom_center",color="pink"),
                   margin=10,
                     padding=10, 
                     alignment=alignment.bottom_center,
                     width=150,
                     height=150,
                     border_radius=10,
                     bgcolor="#59B4C3"),
        Container(content=Text("bottom_right",color="pink"),
                   margin=10,
                     padding=10,
                     alignment=alignment.bottom_right,
                     width=150,
                     height=150,
                     border_radius=10,
                     bgcolor="#59B4C3"),
         Container(content=Text("Custmization alignment",size=10,color="pink"),
                    margin=10,
                     padding=10, 
                     alignment=alignment.Alignment(1,0), 
                     width=150,
                     height=150,
                     border_radius=10,
                     bgcolor="#59B4C3"),
          Container(content=Text("Custmization alignment",size=20,color="pink"),
                    margin=10,
                     padding=10, 
                     alignment=alignment.Alignment(5,2),
                     width=150,
                     height=150,
                     border_radius=10,
                     bgcolor="#59B4C3")],alignment=MainAxisAlignment.CENTER)
    page.add( 
        row_align, row3,row
    )
if __name__ =="__main__":
    app(target=main)