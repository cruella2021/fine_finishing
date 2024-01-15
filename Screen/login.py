import flet as ft

class LoginPage:
    
    def __init__(self, page):
        self.page     = page
        self.login    =  ft.TextField(label="Имя",col={"sm": 12, "md": 8, "xl": 6})
        self.password =  ft.TextField(label="Пароль", password=True,col={"sm": 12, "md": 8, "xl": 6})
        self.bt_auth  =  ft.ElevatedButton(text="Вход", on_click=self.bt_click_auth,col={"sm": 12, "md": 6, "xl": 4})
        self.body_page()
   
    
        
    def body_page(self):
        self.body = ft.Column(expand=True, 
                             alignment= ft.MainAxisAlignment.CENTER,
                                     controls=[
                                         ft.ResponsiveRow(alignment= ft.MainAxisAlignment.CENTER, controls=[self.login]),
                                         ft.ResponsiveRow(alignment= ft.MainAxisAlignment.CENTER, controls=[self.password]),
                                          ft.ResponsiveRow(alignment= ft.MainAxisAlignment.CENTER, controls=[self.bt_auth])
                                     ]
                                 )

    def bt_click_auth(self, e):
        
        if self.login.value == "":
            dlg = ft.AlertDialog(title=ft.Text("Поля должны быть заполнены"), on_dismiss=lambda e: print("Dialog dismissed!"))
            self.page.dialog = dlg
            dlg.open = True
            self.page.update()
            return 
        
        if self.login.value == self.password.value:
            self.page.session.set("id_session",self.login.value)
            self.page.go("")
        else:
            dlg = ft.AlertDialog(title=ft.Text("Ошибка авторизации"), on_dismiss=lambda e: print("Dialog dismissed!"))
            self.page.dialog = dlg
            dlg.open = True
            self.page.update()
    
    #def close_banner(self):
    #        self.page.banner.open = False
    #        self.page.update()        
            
    
    def return_content_page(self):
        return self.content
        