from flet import *
import flet as ft

def main(page: Page):
    page.title="Scollering column prorammatically"
    page.theme=ft.Theme(
        scrollbar_theme=ft.ScrollbarTheme(
            track_color={
                MaterialState.HOVERED:"#3C3633",
                MaterialState.DEFAULT:"#EEEDEB",
            },
            track_visibility=True,
            track_border_color="#FF8911",
            thumb_visibility=True,
            thumb_color={
                MaterialState.HOVERED: "#F5D193",
                MaterialState.DEFAULT: "red",
            },
            thickness=30,
            radius=15,
            main_axis_margin=5,
            cross_axis_margin=10,
            interactive=True,
        )
    )
    

    cl=Column(
        spacing=10,   
        height=200,
        width=float("inf"),
        scroll=ScrollMode.ALWAYS,
    )    
    for i in range(0,100):  
        cl.controls.append(Text(f"Text Line {i}",key=str(i)))
    def scroll_to_offset(e):
        cl.scroll_to(offset=100,duration=1000)
    def scroll_to_start(e):
        cl.scroll_to(offset=0,duration=1000)
    def  scroll_to_end(e):
        cl.scroll_to(offset=-1,duration=2000,curve=ft.AnimationCurve.EASE_IN_OUT)
    def scroll_to_key(e):
        cl.scroll_to(key="20",duration=100)
    def scroll_to_minus_delta(e):
        cl.scroll_to(delta=40,duration=200)
    def scroll_to_delta(e):
        cl.scroll_to(delta=-40,duration=200)
    row=Row([ElevatedButton("Scroll to start",on_click=scroll_to_start),
            ElevatedButton("Scroll to end",on_click=scroll_to_end),
            ])
    row2=Row([
        ElevatedButton("Scroll -40",on_click=scroll_to_minus_delta),
        ElevatedButton("Scroll +40",on_click=scroll_to_delta)
        ])
    page.add(Container(cl, border=border.all(1)),
            ElevatedButton("Scroll to offset 100",
                        on_click=scroll_to_offset),
            row, 
            ElevatedButton("Scoroll to key 20",on_click=scroll_to_key),
            row2,
            )
if __name__=="__main__":
    app(target=main)
