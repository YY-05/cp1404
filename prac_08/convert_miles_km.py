"""
CP1404 Week 11 Workshop - GUI program to convert miles to kilometres
Lindsay Ward, IT@JCU
06/10/2015
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

__author__ = 'Lindsay Ward'

MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    """ MilesConverterApp is a Kivy App for converting miles to kilometres """
    output_km = StringProperty()

    def build(self):
        """ Build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        try:
            self.root = Builder.load_file('convert_miles_km.kv')
        except FileNotFoundError:
            print("Error: The .kv file 'convert_miles_km.kv' was not found.")
            return None
        return self.root

    def handle_calculate(self, text):
        """ Handle calculation, output result to label widget """
        miles = self.convert_to_number(text)
        self.update_result(miles)

    def handle_increment(self, text, change):
        """
        Handle up/down button press, update the text input with new value, call calculation function
        :param text: current text in the input field
        :param change: the amount to change the miles by
        """
        miles = self.convert_to_number(text) + change
        self.root.ids.input_miles.text = str(miles)
        self.update_result(miles)

    def update_result(self, miles):
        """ Update the output label with kilometers value """
        self.output_km = str(miles * MILES_TO_KM)

    @staticmethod
    def convert_to_number(text):
        """Convert text to float or 0.0 if invalid."""
        try:
            return float(text)
        except ValueError:
            return 0.0


MilesConverterApp().run()
