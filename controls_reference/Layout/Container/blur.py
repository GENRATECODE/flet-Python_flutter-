from flet import *
import flet as ft
def main(page:Page):
    page.title="Blur_method on  FLET"
    stack=ft.Stack(
        [
            ft.Container(content=ft.Text("hello",size=40,color="#1F2544"),
                         image_src="https://picsum.photos/100/100",
                         width=100,
                         height=100), 
            ft.Container(
                width=20,
                height=20,  
                blur=2 , #with number
                bgcolor="#6CCCC00",
                alignment=alignment.center
            ),
            ft.Container(
                width=50, 
                height=50,
                left=10,
                top=60,   #with tuple
                bottom=10,
                right=10, 
                blur=(0,10),
            ),
            ft.Container(
                top=10,
                left=60,
                blur=ft.Blur(10,0,ft.BlurTileMode.REPEATED ), # with Blur object
                width=60,
                bgcolor="#474F7A",
                height=60,
                ),
            

        ]
    )
    page.add(stack)
if __name__=="__main__":
    app(target=main) 