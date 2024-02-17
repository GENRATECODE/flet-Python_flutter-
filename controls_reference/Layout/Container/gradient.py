from flet import *
import flet as ft
import math 
def main(page:Page):
    page.title="Gradient" 
    c1=Container(content=Column([Text("Linear Gradient",color=colors.PINK)
                                 ,Container(
        width=150,
        height=150,
        border_radius=border_radius.all(10),
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_center,
            colors=[colors.AMBER_ACCENT_100,colors.DEEP_ORANGE_400] , 
            rotation=30,
            tile_mode=GradientTileMode.MIRROR
        )),]
    ),bgcolor=colors.CYAN_ACCENT_200)
    
    c2 =Container(content=Column([Text("Radial Gradient",color=colors.PINK)
                                 ,Container(
        width=150,
        height=150,
        border_radius=border_radius.all(10),
        gradient=ft.RadialGradient(
            center=ft.alignment.Alignment(2.8,0.9),
            stops=[0.2,0.9,0.2], 
            radius=5,     
            focal=ft.alignment.center_left, 
            focal_radius=0.5, 
            tile_mode=GradientTileMode.REPEATED,  
            rotation=9,
            colors=[colors.YELLOW_800, colors.GREEN_500,colors.BLUE_ACCENT_700]  
        )),]  
    ),bgcolor=colors.CYAN_ACCENT_200) 
    
    
    c3 =Container(content=Column([Text("sweep Gradient",color=colors.PINK)
        ,Container(
        width=150,
        height=150,
        border_radius=border_radius.all(10),
        gradient=ft.SweepGradient(
            center=alignment.bottom_left,  
            start_angle=0.0,
            end_angle=math.pi*3,  
            stops=[0.4,0.9],
            colors=[colors.YELLOW_500,colors.BLUE],
            tile_mode=ft.GradientTileMode.DECAL) 
        ),  
        ]
    ),bgcolor=colors.CYAN_ACCENT_200)
    row=Row([c1,c2,c3],alignment=MainAxisAlignment.CENTER)
    
    # full parameter function 
    final_row=Row([],MainAxisAlignment.CENTER)
    page.add(row,final_row)

if __name__=="__main__":
    app(target=main)