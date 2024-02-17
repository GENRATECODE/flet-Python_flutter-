#Divider
# A thin horizontal line, with padding on either side.
# in The material design language, this represents a divider.

import flet as ft

def  main(page: ft.Page):
    page.title="Divider"
    page.add(
        ft.Column(
            [
                ft.Container(
                    bgcolor=ft.colors.AMBER,
                    alignment=ft.alignment.center,
                    expand=True,
                ),
                ft.Divider(),
                ft.Container(
                    bgcolor=ft.colors.BLUE_300,
                    alignment=ft.alignment.center,
                    expand=True
                ),
                ft.Divider(height=1,color="white"),
                ft.Container(
                    bgcolor=ft.colors.BLUE_300,
                    alignment=ft.alignment.center,
                    expand=True,
                ),
                ft.Divider(height=9,thickness=3),
                ft.Container(bgcolor=ft.colors.DEEP_PURPLE_200,
                            alignment=ft.alignment.center,
                            expand=True,
                            ),
            ],
            spacing=2,
            expand=True,
        ),
    
    )
ft.app(target=main)
    
    
    
     