# Fires when a user clicks the container : Event Object e is an instance of ContainerTapEvent : class;
import flet as ft
def main(page:ft.Page):
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    t=ft.Text()
    
    page.title="on_click"
    
    def container_click(e:ft.ContainerTapEvent):
        t.value=f"local_x:{e.local_x}\nlocal_y:{e.local_y}\nglobal_x: {e.global_x},\nglobal_y: {e.global_y}"
        t.update()
    page.add(
        ft.Column([
            ft.Container(
                content=ft.Text("Clickable inside container"),
                alignment=ft.alignment.center,
                bgcolor=ft.colors.GREEN_200,
                width=200,
                height=200,
                border_radius=10,
                on_click=container_click,
            ),
        ],horizontal_alignment=ft.CrossAxisAlignment.CENTER,),t
    )
    
    
if __name__=="__main__":
    ft.app(target=main)