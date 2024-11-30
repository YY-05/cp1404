from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class MyApp(App):
    def build(self):
        # Red box 1
        main_layout = BoxLayout(orientation='horizontal')

        # Green box 2
        left_layout = BoxLayout(orientation='vertical')
        left_layout.add_widget(Button(text='Genesis'))
        left_layout.add_widget(Button(text='Exodus'))

        # Blue box 3
        right_button = Button(text='Leviticus')

        # Add left layout and right button to main layout
        main_layout.add_widget(left_layout)
        main_layout.add_widget(right_button)

        return main_layout

if __name__ == '__main__':
    MyApp().run()
