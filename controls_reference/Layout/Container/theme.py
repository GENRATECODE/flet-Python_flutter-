import flet as ft 

def main(page:ft.Page):
    page.theme=ft.Theme(color_scheme_seed=ft.colors.YELLOW)
    
    page.add(
        # Page Theme
          ft.Container(content=ft.ElevatedButton("Page theme button"),
                bgcolor=ft.colors.SURFACE_VARIANT,
                padding=20,
                width=300,
                ) ,
        # Inherited theme with primary color overriden
        ft.Container(theme=ft.Theme(color_scheme=ft.ColorScheme(primary=ft.colors.PINK)),
                    content=ft.ElevatedButton("Inherited time button"),
                    bgcolor=ft.colors.SURFACE_VARIANT,
                    padding=20,
                    width=300,
                    ),
        # unique always dark theme
        ft.Container(
            theme=ft.Theme(color_scheme_seed=ft.colors.INDIGO),
            theme_mode=ft.ThemeMode.DARK,
            content=ft.ElevatedButton("Unique theme button"),
            bgcolor=ft.colors.SURFACE_VARIANT,
            padding=20,
            width=300, 
        )
        
    )
if __name__=="__main__":
    #page theme
    
    ft.app(target=main)   

    
