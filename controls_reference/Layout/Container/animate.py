import flet as ft

def main(page:ft.Page):
    page.title="animate"
    def animate_container(e):
        c.width=100 if c.width==200 else 200
        c.height=100 if c.height==200 else 200
        c.bgcolor = "blue" if c.bgcolor=="red"  else "red"
        c.update()
         
    # create a container with id 'c' and add an onclick event to it
    c=ft.Container(
        width=200,
        height=200,
        bgcolor="red",  
        animate=ft.animation.Animation(1000,"elasticInOut",)               
        # bounceOut,bounceIn,bounceInOut  
        # decelerate
        # ease,easeIn,easeInSine,easeInCubic,easeInQuint,easeInExpo
        #easeInCirc,easeInBack,easeInOut,easeInOut,easeInOutQuad,easeInOutCubic
        # easeInOutCubic,easeInOutQuart,easeInOutQuint,easeInOutExpo,easeInOutCirc
        #  easeOut,easeOutSine,easeOutCubic,easeOutQuart,easeOutQuint,easeOutExpo
        # easeOutCirc,easeOutBack,easeOutBounce,easeOutElastic,easeOutElastic
        #easeOutElasticAlt,easeOutElasticIn,
        #elasticIn,elasticOut,elasticDur,slowMiddle,Linear
    )
    btn=ft.ElevatedButton("Animate Container",on_click=animate_container)
    page.add(c,btn)

if __name__=="__main__":
    ft.app(target=main)  