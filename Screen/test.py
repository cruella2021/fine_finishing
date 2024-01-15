import flet as ft

class ObjectsTest:
    def __init__(self, page):
        self.page = page

    def get_content_page(self):
        self.body = ft.Column(expand=1, 
                              controls=[
            ft.Container(expand=2, content=ft.Text("2"), bgcolor= ft.colors.RED),
            ft.Container(expand=10, content=ft.Column(scroll=True,
                controls=[
                    ft.ListView(
                        controls=[
                            ft.ListTile(title = ft.Text("1")),
                            ft.ListTile(title = ft.Text("1")),
                            ft.ListTile(title = ft.Text("1")),
                            ft.ListTile(title = ft.Text("1")),
                            ft.ListTile(title = ft.Text("1")),
                            ft.ListTile(title = ft.Text("1")),
                            ft.ListTile(title = ft.Text("1")),
                            ft.ListTile(title = ft.Text("1")),
                            ft.ListTile(title = ft.Text("1")),
                            ft.ListTile(title = ft.Text("1")),
                            ft.ListTile(title = ft.Text("1")),
                            ft.ListTile(title = ft.Text("1")),
                            ft.ListTile(title = ft.Text("1")),
                            ft.ListTile(title = ft.Text("1")),
                             ft.ListTile(title = ft.Text("1")),
                            ft.ListTile(title = ft.Text("1")),
                            ft.ListTile(title = ft.Text("1")),
                            ft.ListTile(title = ft.Text("1")),
                            ft.ListTile(title = ft.Text("1")),
                            ft.ListTile(title = ft.Text("1")),
                            ft.ListTile(title = ft.Text("1")),
                             ft.ListTile(title = ft.Text("1")),
                            ft.ListTile(title = ft.Text("1")),
                            ft.ListTile(title = ft.Text("1")),
                            ft.ListTile(title = ft.Text("1")),
                            ft.ListTile(title = ft.Text("1")),
                            ft.ListTile(title = ft.Text("1")),
                            ft.ListTile(title = ft.Text("1")),
                             ft.ListTile(title = ft.Text("1")),
                            ft.ListTile(title = ft.Text("1")),
                            ft.ListTile(title = ft.Text("1")),
                            ft.ListTile(title = ft.Text("1")),
                            ft.ListTile(title = ft.Text("1")),
                            ft.ListTile(title = ft.Text("1")),
                            ft.ListTile(title = ft.Text("1")),
                        ]
                    )
                ]
                
                ), bgcolor= ft.colors.YELLOW)
        ])