import flet as ft


def main_page(page: ft.Page):
    page.title = 'Мое первое приложение'
    page.theme_mode = ft.ThemeMode.LIGHT

    text_hello = ft.Text(value='Hello world')

    text_hello.value = 'Hello Geeks'
    # text_hello = 'Hello world'

    name_input = ft.TextField()

    def on_button_click(_):
        print(name_input.value)
    
    elavated_button = ft.ElevatedButton('send', icon=ft.Icons.SEND, color=ft.Colors.RED, 
                                        icon_color=ft.Colors.GREEN, on_click=on_button_click)



    page.add(text_hello, name_input, elavated_button)



ft.app(main_page)
# ft.app(main_page, view=ft.AppView.WEB_BROWSER)
