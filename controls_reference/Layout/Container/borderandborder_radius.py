from flet import *
import flet as ft
def main(page:Page):
    page.title="Border and Border Radius "
    c1=Container(
        content=ft.Text("Without Border",color=colors.RED),
        height=100,
        width=100,
        bgcolor="#FFD0EC"
    )
    c2=Container( 
        content=Column([ft.Text(" Border ",color=colors.RED),
                     Text("border.all(width,color)",color=colors.RED_ACCENT)])
        ,height=100,
        width=100,
        bgcolor="#FFD0EC",
        border=ft.border.all(6 ,colors.RED),
        )
    c3=Container(  content=Column([ft.Text(" Border ",color=colors.RED),
                     Text("border.symmetric(verticla:BorderSide,horizontal:BorderSide)",color=colors.RED_ACCENT)]),
        height=200,
        width=200,
        bgcolor="#FFD0EC",
        border=border.symmetric(vertical=BorderSide(15 ,colors.BLACK45),horizontal=BorderSide(15,colors.AMBER_50)),)
    c4=Container( 
         content=Column([ft.Text(" Border ",color=colors.RED),
                     Text("border.only(left:BorderSide,top:BoderSide,right:BorderSide,bottom:BorderSide)",color=colors.RED_ACCENT)]),
        height=200,
        width=200, 
        border=border.only(left=BorderSide(10, colors.GREEN),
                           right=BorderSide(10, colors.BLUE),
                           top=BorderSide(20,"black"),
                           bottom=BorderSide(20,"pink")),
        bgcolor="#FFD0EC")
    row=Row(
        [c1,
         c2,
         c3,
         c4,
         ],alignment=MainAxisAlignment.CENTER)
    
    # for border radius
    c11=Container(content=Text("border_radius.all(value)",color=colors.BLACK87), 
                  width=200,
                  height=200,
                  bgcolor="#FFD0EC",
                  )
    c12=Container(content=Text(" border Radius function use \n  border_radius.all(value)",color=colors.BLACK87),
                  width=200,
                  height=200,
                  bgcolor="#FFD0EC",
                  border_radius=border_radius.all(20))
    c13=Container(content=Text(" border Radius \n border_radius.horizontal(left float = 9, right float = 25.9)",color=colors.BLACK87),
                  width=200,
                  height=200,
                  bgcolor="#FFD0EC",
                  border_radius=border_radius.horizontal(left=9,right=80 ))
    c14=Container(content=Text(" border Radius\n border_radius.vertical(top: float = 0, bottom: float = 80)",color=colors.BLACK87),
                  width=200,
                  height=200,
                  bgcolor="#FFD0EC",
                  border_radius=border_radius.vertical(top=10,bottom=100))
    c15=Container(content=Text("No border Radius",color=colors.BLACK87),
                  width=200,
                  height=200,
                  bgcolor="#FFD0EC",
                  border_radius=border_radius.only(top_left=0,
                                                   top_right=30, 
                                                   bottom_left=30,
                                                   bottom_right=0 ))
    border_radius_figure=Row([
        c11,c12,c13,c14,c15 
        ],alignment=MainAxisAlignment.CENTER)

    page.add(row,border_radius_figure)
if __name__=="__main__":
    app(target=main)