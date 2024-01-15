import flet as ft
import os

class ObjectStageImage:
    def __init__(self, page, id_object, id_stage):
        self.page = page
        self.id_object     = 1
        self.id_stage      = id_stage
        self.current_image = 1
        self.first         = True
        self.path_app      = os.path.abspath(os.curdir)
        self.get_content()    
    
    def change_big_image(self, e):
       
        self.current_image = int(e.control.data.split("/")[-1].split(".")[0])
        self.set_big_image()
        self.page.update()
        
    def set_current_id_image(self, action):
        if action == "+":
            current_image = self.current_image + 1
        else:
            current_image = self.current_image - 1
        
        path_image = f"{self.path_app}/assets/image/{self.id_object}/{self.id_stage}/{current_image}.jpg"

        if os.path.exists(path_image) == True:
            self.current_image = current_image
            self.set_big_image()
            self.page.update()
                
    def click_back(self, e):
        self.set_current_id_image("-")
           
    def click_forward(self, e):
        self.set_current_id_image("+")
        
    def set_big_image(self):
        
        if self.first:
            self.big_image = ft.Image(expand=11,
                src=f"image/{self.id_object}/{self.id_stage}/{self.current_image}.jpg",
                fit=ft.ImageFit.CONTAIN,
                repeat=ft.ImageRepeat.NO_REPEAT,
                border_radius=ft.border_radius.all(10),
                #col = 10
            )
            self.first = False
        else:
            self.body.controls[0].controls[0].content.controls[0].controls[1]= ft.Image(expand=11,
                src=f"image/{self.id_object}/{self.id_stage}/{self.current_image}.jpg",
                fit=ft.ImageFit.CONTAIN,
                repeat=ft.ImageRepeat.NO_REPEAT,
                border_radius=ft.border_radius.all(10),
                #col = 10
            )
            
        self.page.update()
        
    def get_list_image(self):
        container = ft.Row(wrap=False, scroll=ft.ScrollMode.ALWAYS)
        
        path = os.path.abspath(os.curdir)
        full_path = f"{path}/assets/image/{self.id_object}/{self.id_stage}/"
        
        files = os.listdir(full_path)
        for file in files:
            
            container.controls.append(
                    ft.Container(        
                        on_click=self.change_big_image,
                        data = f"image/{self.id_object}/{self.id_stage}/{file}",
                        content= ft.Image(
                            src=f"image/{self.id_object}/{self.id_stage}/{file}",
                            fit=ft.ImageFit.CONTAIN,
                            repeat=ft.ImageRepeat.NO_REPEAT,
                            border_radius=ft.border_radius.all(10))
                        
                    )
            )    
        
        
        return container
    
    def get_content(self):
        plus = "+"
        minus = "-"
        self.set_big_image()
        self.body = ft.Column(expand=True,
                              controls=[
                                  ft.ResponsiveRow(
                                      expand=8, controls=[
                                    ft.Container(
                                    #bgcolor=ft.colors.RED,
                                    expand=8,
                                    content=ft.Column(controls=[
                                                        ft.Row(expand=True,controls=[
                                                        ft.IconButton(expand=1, icon=ft.icons.ARROW_BACK_IOS_SHARP,on_click= self.click_back),
                                                            self.big_image,
                                                        ft.IconButton(expand=1, icon=ft.icons.ARROW_FORWARD_IOS_SHARP,on_click= self.click_forward)])        
                                                        ])
                                                     )]),
                                ft.Container(
                                             #gcolor = ft.colors.RED, 
                                             expand=2,
                                             alignment = ft.alignment.center,  content=self.get_list_image())
                              ])
        
        #self.body = ft.Column(expand=True,
        #                      controls=[
        #                          ft.ResponsiveRow([
        #                              ft.Container(expand=10, content=
        #                                       ft.Row(alignment = ft.MainAxisAlignment.CENTER,
        #                                            controls = [
        #                                            ft.IconButton(icon=ft.icons.ARROW_BACK_IOS_SHARP
        #                                            ,on_click= self.click_back),
        #                                            self.big_image,
        #                                            ft.IconButton(icon=ft.icons.ARROW_FORWARD_IOS_SHARP,on_click= self.click_forward)
        #                                            ])
        #                                           ,
        #                                            col={"sm": 10, "md": 10, "xl": 10}
        #                                            )]),
        #                          
        #                          ft.ResponsiveRow([ft.Container(expand=2, content=ft.Row(
        #                                       alignment = ft.MainAxisAlignment.CENTER,
        #                                        controls = [self.get_list_image()]) 
        #                                       ,col={"sm": 2, "md": 2, "xl": 2})
        #                          ])])