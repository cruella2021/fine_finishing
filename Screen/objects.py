import flet as ft
from core import list_object

class ObjectsPage:
    def __init__(self, page):
        self.page = page
    

    def return_list_object(self):
        
        def go_to(e):
            self.page.go(e.control.data)
                
        main_colum = ft.Column(expand=True)
        
        
        for item in list_object:
            main_colum.controls.append(
                    ft.ResponsiveRow(alignment=ft.MainAxisAlignment.CENTER,
                        controls= [
                    ft.Card(
                        col={"sm": 12, "md": 12, "xl": 6},
                        #expand=10,
                        content=ft.Column( controls=
                            [
                                ft.ListTile(
                                    leading=ft.Icon(ft.icons.ALBUM),
                                    title=ft.Text(f'Поселок: {item["vilage"]} .\n№: {item["number"]}'),
                                    subtitle=ft.Text("Адрес:" + item["addres"] + "\nПокупатель: " + item["buyer"]),
                                ),
                                ft.Row(
                                    [
                                        ft.TextButton("Список задач", on_click=go_to, data=f"/object/{item['id']}"),
                                        ft.TextButton("Список файлов", on_click=go_to, data=f"/object_file/{item['id']}")
                                                      ],
                                    alignment=ft.MainAxisAlignment.END,
                                ),
                            ]
                        )
            )]))
        
        return main_colum
    
    def body(self):
        self.body = self.return_list_object()
        
    def get_content_page(self):
        self.body()