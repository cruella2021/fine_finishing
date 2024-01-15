import flet as ft
from core import list_object
import os
import shutil

class ObjectPage:
    
    def __init__(self, page, id):
        self.page = page
        self.id_object        = id
        self.data             = self.get_data_by_id()
        self.current_path_img = ""
        self.take_data_object()
        self.dialog_file = ft.FilePicker(on_result=self.pick_files_result)
        
        self.page.overlay.append(self.dialog_file) 
        
        
    def go_to_image_stage(self, e):
        self.page.go(e.control.data)
    
    def go_to_file(self, e):
        self.page.go(f"/object_file/{self.id_object}")
    
    
    def load_image(self, e):
        self.current_path_img = "/image/" + e.control.data + "/"
        
        self.dialog_file.pick_files(
                                allow_multiple=True, 
                                file_type = ft.FilePickerFileType.IMAGE)
        
    def pick_files_result(self, e):
        list_files = list()
        list_movi = list()
        
        for  file in e.files:
            list_files.append(ft.FilePickerUploadFile(
                    file.name,
                    upload_url=self.page.get_upload_url(file.name, 600)
                ))
            
            list_movi.append(file.name)
            
        self.dialog_file.upload(list_files)
        
        self.move_image(list_movi)    
        
    def move_image(self, list_movi):
        dir_assets = os.path.abspath(os.curdir) + "/assets/"
        
        last_number = len(os.listdir(dir_assets + self.current_path_img)) + 1
        
        
        for file in list_movi:
            if os.path.exists(dir_assets + "/uploads/" + file):
                
                print(dir_assets + "/uploads/" + file)
                print(dir_assets + self.current_path_img + file)
                
                shutil.copyfile(dir_assets + "/uploads/" + file, dir_assets + self.current_path_img + f"{last_number}.jpg")
                last_number += 1
            
    def add_image(self, e):
        pass
        
    def head_task(self):
        return ft.Card(col = {"sm":12, "md":12, "xl":6},
                content=ft.Column(controls=[
                            ft.ListTile(
                                leading=ft.Icon(ft.icons.ALBUM),
                                title=ft.Text(f'Поселок: {self.data["vilage"]} .\n№: {self.data["number"]}'),
                                subtitle=ft.Text("Адрес:" + self.data["addres"] + "\nПокупатель: " + self.data["buyer"]),
                            ),
                            ft.Row(
                                [
                                    ft.TextButton("Список файлов", on_click=self.go_to_file)],
                                alignment=ft.MainAxisAlignment.END,
                            ),
                        ]
                    )
                 
                 
                )
        
    def table_task(self):
        return ft.Row(scroll=True, controls=[ft.DataTable(col={"sm": 12, "md": 12, "xl": 6},
            columns=[
                ft.DataColumn(ft.Text("№")),
                ft.DataColumn(ft.Text("Задача")),
                ft.DataColumn(ft.Text("Дата начало")),
                ft.DataColumn(ft.Text("Дата окончания")),
                ft.DataColumn(ft.Text("Картинки")),
                ft.DataColumn(ft.Text("Добавить карнитки"))
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("1")),
                        ft.DataCell(ft.Text("Замер помещений дизайнером")),
                        ft.DataCell(ft.Text("01.01.2023")),
                        ft.DataCell(ft.Text("15.01.2023")),
                        ft.DataCell(ft.TextButton(text="Открыть(4)", data= f"/stage_image/{self.id_object}/1", on_click=self.go_to_image_stage)),
                        ft.DataCell(ft.TextButton(text="Добавить", data= f"/{self.id_object}/1", on_click = self.load_image))
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("2")),
                        ft.DataCell(ft.Text("Подбор декоративных материалов(ДМ) в офисе")),
                        ft.DataCell(ft.Text("16.01.2023")),
                        ft.DataCell(ft.Text("20.01.2023")),
                        ft.DataCell(ft.TextButton(text="Открыть(2)", data= f"/stage_image/{self.id_object}/2", on_click=self.go_to_image_stage)),
                        ft.DataCell(ft.TextButton(text="Добавить", data= f"/{self.id_object}/2", on_click = self.load_image))
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("3")),
                        ft.DataCell(ft.Text("Согласование с заказчиком доп.опций и спецификации")),
                        ft.DataCell(ft.Text("17.01.2023")),
                        ft.DataCell(ft.Text("30.01.2023")),
                        ft.DataCell(ft.TextButton(text="Открыть(3)", data= f"/stage_image/{self.id_object}/3", on_click=self.go_to_image_stage)),
                        ft.DataCell(ft.TextButton(text="Добавить", data= f"/{self.id_object}/3", on_click = self.load_image))
                    ],
                ),
            ],
        )])

   
        
        
    def take_data_object(self):
        main_colum = ft.Column(expand=True, scroll=True)
        
        head = ft.ResponsiveRow(alignment=ft.MainAxisAlignment.CENTER, controls=[self.head_task()])
        table = ft.ResponsiveRow(alignment=ft.MainAxisAlignment.CENTER, controls=[self.table_task()])
        
        main_colum.controls.append(head)
        main_colum.controls.append(table)
        

        
        self.body = main_colum
                
    def get_data_by_id(self):
        for object in list_object:
            if object["id"] == self.id_object:
                return object
