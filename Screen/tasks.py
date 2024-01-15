import flet as ft

class TasksPage:
    def __init__(self, page):
        self.page = page
        self.body = self.get_content()
        
        
    def get_content(self):
        return ft.Text("Тут будут этапы строительства")