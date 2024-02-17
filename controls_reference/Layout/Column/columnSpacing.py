# A control that display its children is a vertical array
# To Cause a child control to expand and fill the available vertical space set its expand property.abs

# Examples
# ===============



from flet import *

def main(page:Page):
    def item(count):
        items=[]
        for i in range(1,count+1):
            items.append(
                Container(
                    content=Text(value=str(i)),
                                alignment=alignment.center,
                                width=50,
                                height=50,
                                bgcolor=colors.AMBER,
                                border_radius=border_radius.all(5),# ft.border_radius.all(5)
                                
                          
                                
                ) 
            )
        
        return items 
        
    def spacing_slider_change(e):
        col.spacing = e.control.value 
        col.update()
    page.title="column Spacing"
    # gap_slider =ft.Slider(min=int,max=int,divisions=int,value=int,label="{value}",width=500,on_change=function)
    gap_slider=Slider(min=0,
                max=100,
                divisions=10,
                value=0,
                width=500,
                on_change=spacing_slider_change,
                )
        
    col1=Column([
        Text("Spacing Between Items"),
        gap_slider
    ],spacing=20)
    
    col=Column(spacing=0,controls=item(10))
    page.add(col1,col)  






if __name__=="__main__":
    app(target=main)