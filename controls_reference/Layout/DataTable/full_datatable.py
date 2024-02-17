import flet as ft

def main(page:ft.Page):
    page.title="DataTable full property 1"
    
    datatable=ft.DataTable(
        width=700,
        bgcolor="blue",
        border=ft.border.all(2,"red"),
        border_radius=20,  
        vertical_lines=ft.border.BorderSide(3,"yellow"),
        horizontal_lines=ft.border.BorderSide(1,"green"),
        sort_column_index=0,
        sort_ascending=True,
        heading_row_color=ft.colors.BLACK12,
        heading_row_height=100,
        data_row_color={"hovered":"0x30FF0000"},
        show_checkbox_column=True,
        divider_thickness=0,
        column_spacing=200,
        columns=[
            ft.DataColumn(ft.Text("Column 1"),
                            on_sort=lambda e: print(f"{e.column_index}, {e.ascending}")),
            ft.DataColumn(ft.Text("Column 2"),
                          on_sort=lambda e: print(f"{e.column_index}, {e.ascending}")),
        ],
        rows=[
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("A")), 
                    ft.DataCell(ft.Text("1")),
                    
                ],
                selected=True,
                on_select_changed=lambda e: print(f"selected row index = {e.data}"),
            ),
             
            ft.DataRow([ft.DataCell(ft.Text("B")),
                            ft.DataCell(ft.Text("2"))],
                      )
        ]
        
    )
    
    page.add(datatable)

if __name__=="__main__":
    ft.app(main)