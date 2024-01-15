import flet as ft
import os

class FilesPage:
    def __init__(self, page, id_object):
        self.page      = page
        self.id_object = 1#id_object
        self.path_app  = os.path.abspath(os.curdir)
        self.get_content()
        self.get_list_file()
    
    
    def get_content(self):
        
        table_file = self.get_list_file()
        
        self.body = ft.Column(expand=True, 
                              controls=[ft.Row(
                                  alignment= ft.MainAxisAlignment.CENTER,
                                  controls=[table_file])])
        
        
    def get_list_file(self):
        
        current_path_object = self.path_app + f"/doc/{self.id_object}/"
        
        table = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("№"), numeric=True),
                ft.DataColumn(ft.Text("Имя"))
            ])
                 
        
        
        i = 1
         
        for file in os.listdir(current_path_object):
            if os.path.isfile(current_path_object + file):
                name_file , extantion_file = file.split(".")
                
                table.rows.append(
                    ft.DataRow(
                    cells=[ft.DataCell(ft.Text(i)),
                           ft.DataCell(
                               
                                 
                        ft.Row(controls=[
                            self.get_img_extantion(extantion_file),
                            ft.TextButton(text = name_file)
                            ])),
                        ]
                ))

            i +=1
            
        return table
    
    def get_img_extantion(self, extantion):
        ico = ft.icons.DEVICE_UNKNOWN_SHARP
        if extantion == "jpg":
            ico = ft.icons.IMAGE
        
        if extantion == "pdf":
            ico = ft.icons.PICTURE_AS_PDF
            
        if extantion.startswith("doc") \
                or extantion.startswith("odt") \
                or extantion.startswith("xls"):
            ico = ft.icons.EDIT_DOCUMENT    
            
        return ft.Icon(name=ico)