import flet as ft


class About(ft.AlertDialog):

    def __init__(self):
        super().__init__()
        self.content = ft.Text("图片查看器\n版本: 0.1.0\n作者: ejir")
