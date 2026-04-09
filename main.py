import flet as ft
import os                      # Проверяет наличие файлов
import random                  # Импортируем random для выбора случайного имени
from datetime import datetime  # Импорт для работы со временем

# Имя файла для хранения данных
HISTORY_FILE = "history.txt"

def main_page(page: ft.Page):
    page.title = 'Мое первое приложение'
    page.theme_mode = ft.ThemeMode.LIGHT

    # 1. ЗАГРУЗКА ИЗ ФАЙЛА
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            greeting_history = [line.strip() for line in f.readlines()]
    else:
        greeting_history = []

    text_hello = ft.Text(value='Hello Geeks')
    history_text = ft.Text(value="История приветствий:\n" + '\n'.join(greeting_history))
    
    # Список имен для генерации
    names_list = [
    "Мирбек", "Анжелика", "Нурлан", "Гульнур", "Омар", 
    "Айпери", "Арсен", "Самара", "Данияр", "Асель", 
    "бекборби", "Айчүрөк", "Султан", "Юлия", "Ильяз", 
    "Каныкей", "Атай", "Чолпон", "Эдил", "Жийдеш"]
                  
    def on_button_click(_):
        name = name_input.value

        if name:
            # ЛОГИКА ВРЕМЕНИ
            # Получаем текущее время и форматируем его
            now = datetime.now().strftime("%Y:%m:%d - %H:%M:%S")
            full_message = f"{now} - Привет, {name}!"
            
            text_hello.color = None
            text_hello.value = full_message
            name_input.value = "" 

            # Добавляем в историю готовую строку со временем
            greeting_history.append(full_message)
            
            # 2. ОГРАНИЧЕНИЕ (последние 5 имён)
            current_history = greeting_history[-5:]

            # 3. СОХРАНЕНИЕ В ФАЙЛ
            with open(HISTORY_FILE, "w", encoding="utf-8") as f:
                for item in current_history:
                    f.write(f"{item}\n")

            greeting_history[:] = current_history 
            history_text.value = "История приветствий (последние 5):\n" + '\n'.join(greeting_history)
        else: 
            text_hello.color = ft.Colors.RED
            text_hello.value = 'Введите имя'
        
        page.update()
    
    # Функция для выбора случайного времени
    def set_random_name():
        random_name = random.choice(names_list)
        name_input.value = random_name
        page.update()

    def clear_history(_):
        greeting_history.clear()
        if os.path.exists(HISTORY_FILE):
            os.remove(HISTORY_FILE)
        history_text.value = 'История приветствий: '
        page.update()

    def toggle_theme(_):
        page.theme_mode = ft.ThemeMode.DARK if page.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT
        page.update()
    
    name_input = ft.TextField(on_submit=on_button_click, label='Введите имя', expand=True)
    
    elavated_button = ft.ElevatedButton(
        'Отправить', 
        icon=ft.Icons.SEND, 
        color=ft.Colors.BLUE, 
        icon_color=ft.Colors.BLUE, 
        on_click=on_button_click
    )
    
    # кнопка "случайное имя"
    random_button = ft.OutlinedButton(
        'Случайное имя',
        icon=ft.Icons.PERSON_ADD,
        on_click=set_random_name 
    )

    theme_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_6, on_click=toggle_theme)
    clear_button = ft.ElevatedButton('Очистить историю', on_click=clear_history)

    # Добавляем в кноку рандом в строку управления
    main_object = ft.Row([name_input, random_button, elavated_button, theme_button])
    history_row = ft.Column([history_text, clear_button])

    page.add(text_hello, main_object, history_row)

ft.app(main_page)