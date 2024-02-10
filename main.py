# Импорт необходимых модулей Kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


# Словарь с данными о цветах
colors_data = {
    '#ff0000': 'красный',
    '#ff8800': 'оранжевый',
    '#ffff00': 'желтый',
    '#00ff00': 'зеленый',
    '#00ffff': 'голубой',
    '#0000ff': 'синий',
    '#ff00ff': 'фиолетовый'
}
colors_mapping = {tuple((str(x*255) for x in color)): name for name, color in colors_data.items()}


# Главный класс приложения
class RainbowApp(App):

    def build(self):
        # Создание основного макета
        layout = BoxLayout(orientation='vertical')

        # Создание метки для отображения названия цвета
        color_label = Label(text='Выберите цвет', size_hint=(1, 0.2))
        layout.add_widget(color_label)

        # Создание текстового поля для отображения кода цвета
        color_code_input = TextInput(multiline=False, size_hint=(1, 0.1))
        layout.add_widget(color_code_input)

        # Функция для обработки нажатия кнопок
        def on_button_click(instance):
            color_code = [int(x * 255) for x in instance.background_color[:3]]  # Получаем RGB цвет
            color_code_str = '#' + ''.join(format(c, '02x') for c in color_code)  # Преобразуем в строку кода цвета
            color_name = colors_mapping.get(tuple(color_code), color_code_str)
            color_label.text = color_name
            instance.text = color_code_str

            # Создание кнопок для каждого цвета и привязка функции к их событию нажатия
        for color_code, color_name in colors_data.items():
            color_button = Button(text=color_name, background_color=color_code)
            color_button.bind(on_press=on_button_click)
            layout.add_widget(color_button)

        return layout


# Запуск приложения
if __name__ == '__main__':
    RainbowApp().run()
