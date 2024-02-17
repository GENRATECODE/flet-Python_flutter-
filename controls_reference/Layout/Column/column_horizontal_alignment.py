from flet import *

def main(page:Page):
    page.title= "Column horizontal alignments"
    def item(count):
        items=[]
        for i in range(count+1):
            items.append(
                Container(
                    content=Text("Item "+str(i)),
                    alignment=alignment.center,
                    width=50,
                    height=50,
                    bgcolor=colors.AMBER_500
                )
            )
        return items 
    def column_with_horizontal(align:CrossAxisAlignment):
        return Column(
            [  Text(str(align),size=16,bgcolor=colors.RED),  
            Container(
                content=Column(item(3),
                alignment=MainAxisAlignment.START, # verticle align
                horizontal_alignment=align, # horizontal alignment ke lia
                ),
                bgcolor=colors.BLUE,
                width=100,
            ),
                ]
            
            )
        
    
    page.add(
        Row(
            [
                column_with_horizontal(CrossAxisAlignment.START),
                column_with_horizontal(CrossAxisAlignment.CENTER),
                column_with_horizontal(CrossAxisAlignment.END),
            ],
            spacing=30,
            alignment=MainAxisAlignment.START,
        )
    )
    
if __name__=="__main__":
    app(target=main) 