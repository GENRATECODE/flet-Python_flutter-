# Dismissible
# A control that can be dismissed by dragging in the indicated  `dismiss_direction`. When drgaged or flung in the specified ~dismiss_direction, it's content smoothly slides out of view.

import flet as ft


def main(page:ft.Page):
    page.title="Dismissible"
    page.window_height,page.window_width=500,400
    
    def close_yes_dlg(e):
        page.close_dialog()
        dlg.data.on_confirm_dismiss(True)
    def close_no_dlg(e):
        page.close_dialog()
        dlg.data.confirm_dismiss(False)
    dlg=ft.AlertDialog(
        modal=True,
        title=ft.Text("Please confirm"),
        content=ft.Text("Do you really want to delte this item?"),
        actions=[
            ft.TextButton("yes",on_click=close_yes_dlg),
            ft.TextButton("no",on_click=close_no_dlg),],
        actions_alignment=ft.MainAxisAlignment.CENTER,
    
    )
    
    def handle_confirm_dismiss(e:ft.DismissibleDismissEvent):
        if e.direction==ft.DismissDirection.END_TO_START:
            dlg.data=e.control
            page.show_dialog(dlg)
        else:
            e.control.handl_confirm_dismiss(True)
    def handle_dismiss(e):
        lv.controls.remove(e.control)
        page.update()
    def handle_update(e:ft.DismissibleUpdateEvent): 
        print(f"update-direction:{e.direction}, Progress:{e.rogress},reached:{e.reached},previous_reached:{e.previous_reached}")
        
    lv=ft.ListView(controls=[
        ft.Dismissible(
            content=ft.ListTile(title=ft.Text(f"Item{i}")),
            dismiss_direction=ft.DismissDirection.HORIZONTAL,
            background=ft.Container(bgcolor=ft.colors.GREEN),
            secondary_background=ft.Container(bgcolor=ft.colors.RED),
            on_dismiss=handle_dismiss,
            on_update=handle_update,
            on_confirm_dismiss=handle_confirm_dismiss,
            dismiss_thresholds={
                ft.DismissDirection.END_TO_START:0.2,
                ft.DismissDirection.START_TO_END:0.2,
            },
        )
        for i in range(10)
    ],
            expand=True,)  
    page.add(lv)

if __name__=="__main__":
    ft.app(target=main)