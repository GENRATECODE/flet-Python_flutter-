import flet as ft
from flet import *

def main(page:Page):
    page.title="margin and Padding"
    
    c0=Container(
        content=Text("Withour Margin  "), 
        height=200,
        width=200,
        bgcolor=colors.RED_ACCENT)
    c1=Container(
        content=Text("Margin with simple value "), 
        height=200,
        width=200,
        margin=10,
        bgcolor=colors.RED_ACCENT)
    c2=Container(content=Text("Margin.all(value)"),
                height=200,
                margin=margin.all(50),
        width=200,
        bgcolor=colors.AMBER)
    c3=Container( content=Text("margin.symmetric(vertical,horizontal)"),
        height=200,
        width=200,
        margin=margin.symmetric(vertical=40, horizontal=40), 
        bgcolor=colors.BLUE)
    c4=Container(     content=Text("margin.only(left,top,right,bottom)"),
                margin=margin.only(left=10,right=5,top=10,bottom=15),  
        height=200,
        width=200,
        bgcolor=colors.PURPLE)
    
    c01=Container(content=Text("Withour Padding"),
                               height=200,
                               width=200,
                               
                bgcolor=colors.GREEN)
    c11=Container(     content=Text("Padding with simple value"),
                  padding=20,   
        height=200,
        width=200,
        bgcolor=colors.PURPLE)
    c12=Container(       content=Text("paddin.all(15)"), 
                  padding=padding.all(15),
        height=200,
        width=200,bgcolor=colors.BLUE)
    c13=Container(        content=Text("padding.symmetric(vertical=40,horizonal=)"),
                  padding=padding.symmetric(vertical=8,horizontal=30),
        height=200,
        width=200,bgcolor=colors.AMBER)
    c14=Container(        
                  content=Text("Padding only(left,top,right,bottom)"),
                  padding=padding.only(left=16, top=19, right=16, bottom=9),
        height=200,
        width=200,bgcolor=colors.RED_ACCENT)
    
    
    row1=Row([c0,c1,c2,c3,c4],alignment=MainAxisAlignment.CENTER)
    row2=Row([c01,c11,c12,c13,c14],alignment=MainAxisAlignment.CENTER)
    page.add(Column([row1,row2]))
if __name__=="__main__":
    app(target=main)   