import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

green = [0, 3, 0, 1]

Window.size = (700, 600)


class MyApp(App):
    def build(self):
        self.title = "X-FIT"
        self.flag = False
        self.layoutosn = BoxLayout(orientation='vertical')
        self.layout = BoxLayout(orientation='horizontal', padding=10, size_hint=(1, .30))
        self.layoutosn.add_widget(self.layout)
        btn1 = Button(text="Медиа", size_hint=(.20, .1), pos_hint={'center_x': 1.1, 'center_y': 0.85},
                      background_color=green,
                      on_press=self.show_label1)
        btn2 = Button(text="Тарифы", size_hint=(.20, .1), pos_hint={'center_x': 1.1, 'center_y': 0.85},
                      background_color=green,
                      on_press=self.show_label2)
        btn3 = Button(text="Фитнес-счетчики", size_hint=(.35, .1), pos_hint={'center_x': 1.1, 'center_y': 0.85},
                      background_color=green,
                      on_press=self.show_label3)
        btn4 = Button(text="О клубе", size_hint=(.20, .1), pos_hint={'center_x': 1.1, 'center_y': 0.85},
                      background_color=green,
                      on_press=self.show_label4)
        btn5 = Button(text="Контакты", size_hint=(.22, .1), pos_hint={'center_x': 1.1, 'center_y': 0.85},
                      background_color=green,
                      on_press=self.show_label5)

        self.layout.add_widget(btn1)
        self.layout.add_widget(btn2)
        self.layout.add_widget(btn3)
        self.layout.add_widget(btn4)
        self.layout.add_widget(btn5)

        self.image = Image(source='imagestart.jpg', pos_hint={'x': 0, 'y': 0.2})
        self.layoutosn.add_widget(self.image)

        return self.layoutosn

    def show_label1(self, instance):
        if self.flag:
            self.layoutosn.remove_widget(self.textinrost)
            self.layoutosn.remove_widget(self.name_fitnes_schetchika)
            self.layoutosn.remove_widget(self.bmi_label)
            self.layoutosn.remove_widget(self.textinves)
            self.layoutosn.remove_widget(self.txtout1)
            self.layoutosn.remove_widget(self.txtout2)
            self.layoutosn.remove_widget(self.submit)
            self.image = Image(source='image1.jpg', pos_hint={'x': 0, 'y': 0.2})
            self.layoutosn.add_widget(self.image)
            self.flag = False
        else:
            self.image.source = 'image1.jpg'

    def show_label2(self, instance):
        if self.flag:
            self.layoutosn.remove_widget(self.textinrost)
            self.layoutosn.remove_widget(self.name_fitnes_schetchika)
            self.layoutosn.remove_widget(self.textinves)
            self.layoutosn.remove_widget(self.txtout1)
            self.layoutosn.remove_widget(self.bmi_label)
            self.layoutosn.remove_widget(self.txtout2)
            self.layoutosn.remove_widget(self.submit)
            self.image = Image(source='image2.jpg', pos_hint={'x': 0, 'y': 0.2})
            self.layoutosn.add_widget(self.image)
            self.flag = False
        else:
            self.image.source = 'image2.jpg'

    def show_label3(self, instance):
        self.layoutosn.remove_widget(self.image)
        self.flag = True
        self.name_fitnes_schetchika = Label(text="Расчет индекса массы тела", size_hint=(.99, .05))
        self.layoutosn.add_widget(self.name_fitnes_schetchika)
        self.txtout1 = Label(text="Введите рост(в см):", size_hint=(.99, .05))
        self.layoutosn.add_widget(self.txtout1)
        self.textinrost = TextInput(multiline=False, size_hint=(.99, .05))
        self.layoutosn.add_widget(self.textinrost)
        self.txtout2 = Label(text="Введите массу тела(в кг):", size_hint=(.99, .05))
        self.layoutosn.add_widget(self.txtout2)
        self.textinves = TextInput(multiline=False, size_hint=(.99, .05))
        self.layoutosn.add_widget(self.textinves)
        self.submit = Button(text="Расчитать ИМТ", font_size=20, size_hint=(.99, .05),
                             on_press=self.calculation_of_body_mass_index)
        self.layoutosn.add_widget(self.submit)
        self.bmi_label = Label(text="Ваш индекс массы тела:", size_hint=(.32, .05))
        self.layoutosn.add_widget(self.bmi_label)

    def show_label4(self, instance):
        if self.flag:
            self.layoutosn.remove_widget(self.textinrost)
            self.layoutosn.remove_widget(self.name_fitnes_schetchika)
            self.layoutosn.remove_widget(self.textinves)
            self.layoutosn.remove_widget(self.bmi_label)
            self.layoutosn.remove_widget(self.txtout1)
            self.layoutosn.remove_widget(self.txtout2)
            self.layoutosn.remove_widget(self.submit)
            self.image = Image(source='image4.jpg', pos_hint={'x': 0, 'y': 0.2})
            self.layoutosn.add_widget(self.image)
            self.flag = False
        else:
            self.image.source = 'image4.jpg'

    def show_label5(self, instance):
        if self.flag:
            self.layoutosn.remove_widget(self.textinrost)
            self.layoutosn.remove_widget(self.name_fitnes_schetchika)
            self.layoutosn.remove_widget(self.bmi_label)
            self.layoutosn.remove_widget(self.textinves)
            self.layoutosn.remove_widget(self.txtout1)
            self.layoutosn.remove_widget(self.txtout2)
            self.layoutosn.remove_widget(self.submit)
            self.image = Image(source='image5.jpg', pos_hint={'x': 0, 'y': 0.2})
            self.layoutosn.add_widget(self.image)
            self.flag = False
        else:
            self.image.source = 'image5.jpg'

    def calculation_of_body_mass_index(self, *args):
        weight = float(self.textinves.text)
        height = float(self.textinrost.text) / 100
        bmi = str(weight / (height ** 2))[:5]
        self.bmi_label.text = f"Ваш индекс массы тела: {bmi}"


if __name__ == "__main__":
    MyApp().run()
