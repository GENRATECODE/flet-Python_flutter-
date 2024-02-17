import backend_to as bt
import flet as ft 
import asyncio
def main(page:ft.Page):
    page.title="Make Data Table using Container row column btn"
    #dataTableDefine
    datatable=ft.DataTable()   
    columns_table=[ ft.DataColumn(ft.Text("S.No")),
                    ft.DataColumn(ft.Text("Name")),
                    ft.DataColumn(ft.Text("Age"),numeric=True),
                    ft.DataColumn(ft.Text("Address")),
                    ft.DataColumn(ft.Text("Phone Number"))
                    ]
    datatable.columns=columns_table
    row_table=[]
    datatable.rows=row_table
    
    
    Name=ft.TextField(label="Name")
    agee=ft.TextField(label="Age")
    address=ft.TextField(label="Address")
    phone_number=ft.TextField(label="Phone Number") 
    count=0
    def action(e):  
        if not Name.value :
            Name.error_text="Please enter your name"
            page.update()  
        elif not agee.value:
            agee.error_text="Please enter your age"
            page.update()
        elif not address.value:
            address.error_text="please enter your address"
            page.update() 
        elif not phone_number.value:
            phone_number.error_text="Please enter a valid "   
            page.update()  
        else:
            print(Name.value,agee.value,address.value,phone_number.value)
            datatable.rows.append(       
                ft.DataRow( 
                    cells= [
                        ft.DataCell(ft.Text(str(1))),
                        ft.DataCell(ft.Text(Name.value)),
                            ft.DataCell(ft.Text(agee.value)),
                            ft.DataCell(ft.Text(address.value)),
                            ft.DataCell(ft.Text(phone_number.value)),   
                            ],
                )  
            )
            page.update() 

    # output data for table  
    output=ft.Container(bgcolor=ft.colors.AMBER_800,height=600,width=600,content=datatable) 
    # inpurt  data for table
    btn=ft.ElevatedButton("Add in Data Table",on_click=action) 
    row1=ft.Row([Name,agee],vertical_alignment=ft.CrossAxisAlignment.CENTER) 
    row2=ft.Row([phone_number,address])
    row3=ft.Row([btn])
    col=ft.Column([row1,row2,row3])
    box=ft.Container(bgcolor=ft.colors.BLUE_900,content=col,margin=8,padding=15,ink=True,height=300,width=650) 
    form=ft.Column(alignment=ft.MainAxisAlignment.CENTER,
                   horizontal_alignment=ft.CrossAxisAlignment.CENTER,controls=[box,output,])
    
    
     
    page.add(    
        form,
    )
if __name__=="__main__":
    ft.app(target=main)