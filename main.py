import flet as ft
from about import About


class ThemeSwitcher(ft.IconButton):

    def __init__(self, page):
        super().__init__()
        self.icon = ft.icons.WB_SUNNY_OUTLINED
        self.on_click = self.toggle_theme
        self.theme_mode = ft.ThemeMode.LIGHT
        self.page = page

    def toggle_theme(self, e):
        self.theme_mode = (ft.ThemeMode.DARK if self.theme_mode
                           == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT)
        self.page.theme_mode = self.theme_mode
        self.icon = (ft.icons.WB_SUNNY_OUTLINED if self.theme_mode
                     == ft.ThemeMode.LIGHT else ft.icons.NIGHTLIGHT_OUTLINED)
        self.page.update()


def main(page: ft.Page):
    page.title = "图片查看器"

    def pickFIleResult(e):
        path = e.files[0].path
        print(e.files[0].path)
        image.src = path
        page.update()

    def ZoomIN(e):
        image.width += 50
        image.height += 50
        page.update()

    def ZoomOUT(e):
        image.width -= 50
        image.height -= 50
        page.update()

    at = About()
    themeSwitcher = ThemeSwitcher(page)
    page.padding = 10
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.adaptive = True
    page.window.max_width = 600
    page.window.min_width = 500
    page.theme_mode = themeSwitcher.theme_mode
    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.IMAGE),
        leading_width=40,
        title=ft.Text("图片查看器"),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            themeSwitcher,
            ft.PopupMenuButton(items=[
                ft.PopupMenuItem(text="设置"),
                ft.PopupMenuItem(),  # 分割
                ft.PopupMenuItem(
                    text="关于",
                    on_click=lambda _: page.open(at),
                ),
            ]),
        ],
    )
    image = ft.Image(src="https://s2.loli.net/2024/07/14/19iMKSpjfsUGXQl.jpg",
                     fit=ft.ImageFit.CONTAIN,
                     width=800,
                     height=400)
    filePicker = ft.FilePicker(on_result=pickFIleResult)
    page.add(
        ft.SafeArea(
            ft.CupertinoContextMenu(
                enable_haptic_feedback=True,
                content=ft.Column([
                    image,
                ]),
                actions=[
                    ft.CupertinoContextMenuAction(
                        text="放大",
                        trailing_icon=ft.icons.ZOOM_IN,
                        on_click=ZoomIN,
                    ),
                    ft.CupertinoContextMenuAction(
                        text="缩小",
                        trailing_icon=ft.icons.ZOOM_OUT,
                        on_click=ZoomOUT),
                    ft.CupertinoContextMenuAction(
                        text="打开新文件",
                        trailing_icon=ft.icons.FILE_OPEN_OUTLINED,
                        on_click=lambda _: filePicker.pick_files())
                ])))
    page.add(
        ft.ElevatedButton(
            "选择文件",
            on_click=lambda _: filePicker.pick_files(),
        ))
    page.overlay.append(filePicker)
    page.update()


ft.app(target=main)
