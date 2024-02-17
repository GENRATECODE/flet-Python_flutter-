from flet import *
import flet as ft 

def main(page:Page):
    shadow=Container(
        border_radius=10,
        width=100,
        height=100,
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=15,
            color=ft.colors.BLUE_300,
            offset=ft.Offset(2,1),  
            blur_style=ShadowBlurStyle.OUTER,
        ),
        shape=BoxShape.CIRCLE
    )
    page.add(shadow)
    
if __name__=="__main__":
    app(target=main)