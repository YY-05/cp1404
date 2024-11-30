from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """A Kivy application that demonstrates BoxLayout functionality."""
    def build(self):
        """Sets up the application UI and returns the root widget."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_great(self):
        """Handles the 'Great' button press, updating the output label."""
        print("test")
        self.root.ids.output_label.text = "Hello "
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        """Handles the 'Clear' button press, resetting input and output fields."""
        self.root.ids.input_name.text = ''
        self.root.ids.output_label.text = ''


BoxLayoutDemo().run()
