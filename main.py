import flet as ft
#import os

from Screen.login import LoginPage
from Screen.objects import ObjectsPage
from Screen.object import ObjectPage
from Screen.test import ObjectsTest
from Screen.stage_image import  ObjectStageImage
from Screen.files import FilesPage
from Screen.tasks import TasksPage

DEFAULT_PORT  = 8787

class MenuApp:
    def __init__(self, page):
        self.page = page
        self.left_menu()
        self.app_bar()
    
    def show_drawer(self, e):
        self.drawer.open = True
        self.drawer.update()    
    
    def left_menu(self):
        
        def on_logout():
            self.page.session.remove("id_session")
            self.page.go("/")
            
        def item_selected_left(e):
            if e.control.selected_index == 0: #Объекты
                self.page.go("/objects")
                
            elif e.control.selected_index == 1: #Задачи
                self.page.go("/tasks")
                
            elif e.control.selected_index == 2: #Выход
                on_logout()   
            elif e.control.selected_index == 3: #Выход
                  self.page.go("/test")
            
        self.drawer = ft.NavigationDrawer(
            on_change=item_selected_left,
            controls=[ft.Container(height=12),
                ft.NavigationDrawerDestination(
                    label="Объекты",
                    icon=ft.icons.HOME_OUTLINED,
                    selected_icon_content=ft.Icon(ft.icons.HOUSE_ROUNDED),
                ),
            
                ft.NavigationDrawerDestination(
                    icon_content=ft.Icon(ft.icons.TASK_OUTLINED),
                    label="Задачи",
                    selected_icon=ft.icons.TASK_ROUNDED,
                ),
                
                ft.Divider(thickness=2),
                
                ft.NavigationDrawerDestination(
                    icon_content=ft.Icon(ft.icons.EXIT_TO_APP),
                    label="Выход"
                ),
                ft.NavigationDrawerDestination(
                    icon_content=ft.Icon(ft.icons.TELEGRAM),
                    label="Тест"
                )
            
            ],)
    
    def app_bar(self):
        self.appbar = ft.AppBar(
                        leading=ft.IconButton(icon=ft.icons.MENU,
                            icon_color="blue400",
                            icon_size=20,on_click=self.show_drawer),
                        leading_width=40,
                        title=ft.Text("Задачи по объектам"),
                        center_title=False,
                        bgcolor=ft.colors.SURFACE_VARIANT,
                    )
    
class MainPage:

    def __init__(self, page):
        self.page = page
        self.get_content_page()

    def get_content_page(self):
        self.left_menu()    
        self.body()
        
    def left_menu(self):
        
        def on_logout():
            self.page.session.remove("id_session")
            self.page.go("/")
            
        def item_selected_left(e):
            if e.control.selected_index == 0: #Объекты
                self.page.go("/objects")
                
            elif e.control.selected_index == 1: #Задачи
                self.page.go("/task")
                
            elif e.control.selected_index == 2: #Выход
                on_logout()   
            
        self.drawer = ft.NavigationDrawer(
            on_change=item_selected_left,
            controls=[ft.Container(height=12),
                ft.NavigationDrawerDestination(
                    label="Объекты",
                    icon=ft.icons.HOME_OUTLINED,
                    selected_icon_content=ft.Icon(ft.icons.HOUSE_ROUNDED),
                ),
            
                ft.NavigationDrawerDestination(
                    icon_content=ft.Icon(ft.icons.TASK_OUTLINED),
                    label="Задачи",
                    selected_icon=ft.icons.TASK_ROUNDED,
                ),
                
                ft.Divider(thickness=2),
                
                ft.NavigationDrawerDestination(
                    icon_content=ft.Icon(ft.icons.EXIT_TO_APP),
                    label="Выход"
                ),
            
            ],)

    def body(self):
        self.body = ft.BarChart(
            bar_groups=[
                ft.BarChartGroup(
                    x=0,
                    bar_rods=[
                        ft.BarChartRod(
                            from_y=0,
                            to_y=40,
                            width=40,
                            color=ft.colors.AMBER,
                            tooltip="Январь(40)",
                            border_radius=0,
                        ),
                    ],
                ),
                ft.BarChartGroup(
                x=1,
                bar_rods=[
                    ft.BarChartRod(
                        from_y=0,
                        to_y=20,
                        width=40,
                        color=ft.colors.RED_500,
                        tooltip="Февраль(20)",
                        border_radius=0,
                    ),
                ],
            ),
                ft.BarChartGroup(
                x=2,
                bar_rods=[
                    ft.BarChartRod(
                        from_y=0,
                        to_y=66,
                        width=40,
                        color=ft.colors.GREEN_300,
                        tooltip="Март(66)",
                        border_radius=0,
                    ),
                ],
            ),
                ft.BarChartGroup(
                x=3,
                bar_rods=[
                    ft.BarChartRod(
                        from_y=0,
                        to_y=15,
                        width=40,
                        color=ft.colors.GREEN_300,
                        tooltip="Закрытые(15)",
                        border_radius=0,
                    ),
                    ft.BarChartRod(
                        from_y=0,
                        to_y=7,
                        width=40,
                        color=ft.colors.RED_100,
                        tooltip="Открытые(7)",
                        border_radius=0,
                    )
                ],
            ),
            ]
            ,
            border=ft.border.all(1, ft.colors.GREY_400),
            left_axis=ft.ChartAxis(labels_size=40, title=ft.Text("Кол-во выполненых задач по месяцам"), title_size=40),
            bottom_axis=ft.ChartAxis(
            labels=[
                ft.ChartAxisLabel(
                    value=0, label=ft.Container(ft.Text("Январь"), padding=10)
                ),
                ft.ChartAxisLabel(
                    value=1, label=ft.Container(ft.Text("Февраль"), padding=10)
                ),
                ft.ChartAxisLabel(
                    value=2, label=ft.Container(ft.Text("Март"), padding=10)
                ),
                ft.ChartAxisLabel(
                    value=3, label=ft.Container(ft.Text("Апрель"), padding=10)
                ),
            ],
            labels_size=40,
        ),
            horizontal_grid_lines=ft.ChartGridLines(
            color=ft.colors.GREY_300, width=1, dash_pattern=[3, 3]
        ),
        tooltip_bgcolor=ft.colors.with_opacity(0.5, ft.colors.GREY_300),
        max_y=110,
        interactive=True,
        #expand=True,
        )

                        
def main(page: ft.Page):
    
    def route_change(e):
        
        page.views.clear()
    
        id_user = page.session.get("id_session")
        
        
        if id_user is None:
            login_page = LoginPage(page)
            page.views.append(
                ft.View(
                    "/login",
                    [
                        login_page.body
                    ],
                    horizontal_alignment = ft.CrossAxisAlignment.CENTER
                )
            )
        else:
            app_menu = MenuApp(page)
                
            if page.route == "/" or page.route == "":
                main_page = MainPage(page)
                
                page.views.append(
                    ft.View(
                        "/",
                        appbar = app_menu.appbar,
                        drawer = app_menu.drawer,
                        controls = [
                            main_page.body
                        ]
                    )
                )
            
            if page.route == "/objects":
                objects_page = ObjectsPage(page)
                objects_page.get_content_page()
                
                page.views.append(
                    ft.View(
                        "/objects",
                        appbar = app_menu.appbar,
                        drawer = app_menu.drawer,
                        controls = [
                            objects_page.body
                        ]
                        , horizontal_alignment = ft.CrossAxisAlignment.CENTER
                        , scroll = True
                    )
                )
            
            if page.route.startswith("/object/"):

                id_object = page.route.replace("/object/","")
                object_page = ObjectPage(page, id_object)
                
                page.views.append(ft.View(
                        f"{page.route}",
                        appbar = app_menu.appbar,
                        drawer = app_menu.drawer,
                        controls = [
                            object_page.body
                        ]
                        , horizontal_alignment = ft.CrossAxisAlignment.CENTER
                ))
            if page.route == "/tasks":
                tasks_page = TasksPage(page)
                
                
                page.views.append(
                    ft.View(
                        "/tasks",
                        appbar = app_menu.appbar,
                        drawer = app_menu.drawer,
                        controls = [
                            tasks_page.body
                        ]
                        , horizontal_alignment = ft.CrossAxisAlignment.CENTER
                        , scroll = True
                    )
                )
                   
            if page.route.startswith("/stage_image/"):

                tmp_param = page.route.replace("/stage_image/","").split("/")
                id_object = tmp_param[0]
                id_stage = tmp_param[1]
                
                image_stage_page = ObjectStageImage(page, id_object, id_stage)
                
                page.views.append(ft.View(
                        f"{page.route}",
                        appbar = app_menu.appbar,
                        drawer = app_menu.drawer,
                        controls = [
                            image_stage_page.body
                        ]
                        #, horizontal_alignment = ft.CrossAxisAlignment.CENTER
                
                ))
            if page.route.startswith("/object_file/"):

                tmp_param = page.route.replace("/object_file/","").split("/")
                id_object = tmp_param[0]
                
                
                file_page = FilesPage(page, id_object)
                
                page.views.append(ft.View(
                        f"{page.route}",
                        appbar = app_menu.appbar,
                        drawer = app_menu.drawer,
                        controls = [
                            file_page.body
                        ]
                ))
     
            if page.route == "/test":
                objects_page = ObjectsTest(page)
                objects_page.get_content_page()
                
                page.views.append(
                    ft.View(
                        "/test",
                        appbar = app_menu.appbar,
                        drawer = app_menu.drawer,
                        controls = [
                            objects_page.body
                        ]
                    )
                )
        page.update()

    def view_pop(e):
        page.views.pop()
        top_view = page.views[-1]
        print(top_view.route)
        page.go(top_view.route)
        
    def on_resize(e):
        page.update()
        print("Изменение размера")
        
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
    
    page.on_resize = on_resize
    
    
if __name__ == "__main__":
    ft.app(target=main, view=ft.WEB_BROWSER, port=DEFAULT_PORT, upload_dir="assets/uploads")