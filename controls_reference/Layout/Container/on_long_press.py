import flet as ft
def main(page:ft.Page):
    page.title="on Hover"  
    t=ft.Column([ft.Text("Backend action only"),])     
    def on_hover(e):
        print("backend action only")
    page.add(
            ft.Container(width=100,height=100,bgcolor="red",ink=False,
                         on_long_press=on_hover),t
        
        )
if __name__=="__main__":
    ft.app(target=main) 