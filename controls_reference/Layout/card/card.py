
from flet import *

def main(page:Page):
    page.title="card"
    def some(e):
        print("pressed button divyansh") # this is the function that will be called when the button is pressed
    # Row where "buy tickets", LIsten
    # Here we use TEXT Button
    
    # List Tile Learn futher chapter  10/24
    list_tile=ListTile(
        leading=Icon(icons.ALBUM),
        title=Text("The Enchanted Nightiangle"),
        subtitle=Text("Music by Julie. Lyrics by Sidney Stein. Orlando, Florida 1968."),
    )
    
    # Row  with image and title, subtitle
    # TextButton(label="anythiny")
    txt_button=TextButton("Buy Tickets",on_click=some)
    txt_button2=TextButton("Listen",on_click=some)
    row=Row([
        txt_button,
        txt_button2,
    ],
    alignment=MainAxisAlignment.END,)
    # Column s in card are like columns in table
    col=Column([
        list_tile,
        row,
    ])
    # container  is a box that contain all the elements inside it
    
    contents=Container(col,width=500,padding=10,)  
     
    # content where Care take , ROW,Column, Stack
     
    #ft.Card(content=,color=,elevation,margin,shadow_color,shape,surface_tint_color)
    
    card=Card(contents,
              color=colors.RED,
            elevation=1.0,margin=margin.symmetric(vertical=200,horizontal=200),
            shadow_color= colors.YELLOW,surface_tint_color=colors.RED 
            )     
    
    # Page update 
    page.add(
        card,
    )


if __name__=="__main__":
    app(target=main)      