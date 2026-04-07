import flet as ft
import os

# Имя файла для хранения данных
HISTORY_FILE = "history.txt"

def main_page(page: ft.Page):
    page.title = 'Мое первое приложение'
    page.theme_mode = ft.ThemeMode.LIGHT

    #1. ЗАГРУЗКА ИЗ ФАЙЛА (Вариант 1) 
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            # Читаем имена и убираем лишние переносы строк
            greeting_history = [line.strip() for line in f.readlines()]
    else:
        greeting_history = []

    # Элементы интерфейса
    text_hello = ft.Text(value='Hello Geeks')
    # Показываем историю сразу при запуске
    history_text = ft.Text(value="История приветствий:\n" + '\n'.join(greeting_history))

    def on_button_click(_):
        name = name_input.value

        if name:
            text_hello.color = None
            text_hello.value = f"Hello {name}"
            name_input.value = "" # Очищаем поле ввода

            greeting_history.append(name)
            
            #2. ОГРАНИЧЕНИЕ ЧЕРЕЗ СРЕЗЫ (Вариант 4) 
            current_history = greeting_history[-5:]

            #3. СОХРАНЕНИЕ В ФАЙЛ (Вариант 1)
            with open(HISTORY_FILE, "w", encoding="utf-8") as f:
                for item in current_history:
                    f.write(f"{item}\n")

            # Обновляем текст на экране и сам список
            greeting_history[:] = current_history 
            history_text.value = "История приветствий (последние 5):\n" + '\n'.join(greeting_history)
        else: 
            text_hello.color = ft.Colors.RED
            text_hello.value = 'Введите имя'
            print('Ничего не ввели')
        
        page.update()
    
    def clear_history(_):
        greeting_history.clear()
        # Удаляем файл, чтобы история не восстановилась после перезапуска
        if os.path.exists(HISTORY_FILE):
            os.remove(HISTORY_FILE)
        history_text.value = 'История приветствий: '
        page.update()

    def toggle_theme(_):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
        page.update()
    
    # Контроллеры
    name_input = ft.TextField(on_submit=on_button_click, label='Введите имя', expand=True)
    elavated_button = ft.ElevatedButton(
        'send', 
        icon=ft.Icons.SEND, 
        color=ft.Colors.RED, 
        icon_color=ft.Colors.GREEN, 
        on_click=on_button_click
    )
    
    theme_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_6, on_click=toggle_theme)
    clear_button = ft.ElevatedButton('Очистить историю', on_click=clear_history)

    main_object = ft.Row([name_input, elavated_button, theme_button])
    # Используем Column, чтобы история росла вниз, а не вбок
    history_row = ft.Column([history_text, clear_button])

    page.add(text_hello, main_object, history_row)

ft.app(main_page)