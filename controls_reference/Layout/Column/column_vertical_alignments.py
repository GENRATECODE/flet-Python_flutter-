from flet import *
import flet as ft
def main(page:Page):
    page.title="colum vertical alignments"
    def item(count):
        items=[]
        for i in range(1,count+1):
            items.append(Container(
                content=Text(str(i)),
                alignment=alignment.center,
                width=50,  
                height=20,
                bgcolor=colors.AMBER_500,
                )
            )
        return items 
    def column_with_alginment(align:MainAxisAlignment,txt:str):
        return  Column([
            Text(str(align),size=10),
            Text(str(txt),size=10),
            Container(
                content=Column(item(3),alignment=align),
                bgcolor=colors.AMBER_100,
                height=400,
            ), 
        ])
     
      
    page.add(
        Row([ 
            column_with_alginment(ft.MainAxisAlignment.START,"start"), # start
            column_with_alginment(ft.MainAxisAlignment.CENTER,"center"),
            column_with_alginment(ft.MainAxisAlignment.END,"end"),
            column_with_alginment(ft.MainAxisAlignment.SPACE_BETWEEN,"Space Between"),
            column_with_alginment(ft.MainAxisAlignment.SPACE_AROUND,"space around"),
            column_with_alginment(ft.MainAxisAlignment.SPACE_EVENLY,"space evenly"),
        ],
        spacing=30,
        alignment=MainAxisAlignment.START,)
    )

if __name__=="__main__":
    app(target=main)  
