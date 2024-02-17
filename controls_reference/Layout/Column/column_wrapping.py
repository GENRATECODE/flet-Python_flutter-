from flet import *

def main(page:Page):
    page.title="Column Wrapping"
    
    def items(count):
        items=[]
        for i in range(1,count+1):
            items.append(
                Container(
                    content=Text(value=str(i)),
                    alignment=alignment.center,
                    width=30,
                    height=30,
                    bgcolor=colors.AMBER,
                    border_radius=border_radius.all(4)
                ) 
            ) 
        return items 
    def slider_change(e):
        col1.height=float(e.control.value)
        col1.update()
    col1=Column(
        wrap=True,
        spacing=20,
        run_spacing=10,
        controls=items(10),
        height=400,
        # width=800
    )
    sclider=Slider(
        min=1,
        max=400, 
        divisions=20,
        value=400,
        label="{value}",
        width=500, 
        on_change=slider_change,
    )
    col=Column([Text("Change the column height to see how child item wrap onto multiple columns:",color=colors.RED),
                sclider,])
    container=Container(content=col1,bgcolor=colors.AMBER_100)
    page.add(col,container,)
if __name__=="__main__":
    app(target=main) 