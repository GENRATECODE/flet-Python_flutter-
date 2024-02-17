from flet import  *
import flet as ft 
import threading
class state:
    i=0
s=state()
sem=threading.Semaphore()   
def main(page:Page):
    page.title="scolling"
    page.icon
    def  on_scroll(e:ft.OnScrollEvent):
        if e.pixel >= e.max_scroll_extent-100:
            if sem.acquire(blocking=False):
                try:
                    for i in range(0,10):
                        cl.controls.append(Text(f"Text line{s.i}",key=str(s.i)))
                        s.i+=1
                    c1.update()
                finally: 
                    sem.release()
    cl=Column( spacing=10,
               height=200,
        width=200,
        scroll=ft.ScrollMode.ALWAYS,
        on_scroll_interval=0,
        on_scroll=on_scroll, 
        horizontal_alignment=CrossAxisAlignment.CENTER,
        alignment=MainAxisAlignment.CENTER
        )       
    for i in range(0,5000):
        cl.controls.append(Text(f"Text line{s.i}",key=str(s.i)))
        s.i+=1
    page.add(Text("Scroll down to see the text change"),Container(cl,border=ft.border.all(1)))
    
if __name__=="__main__":
    app(target=main)