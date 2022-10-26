import PySimpleGUI as sg
from src.consts.font import *


sg.theme('SystemDefault')

def build():

    imagen = sg.Image("src/resources/images/pysimplegui.png")

    layout = [
        [sg.Text('Acerca de...', font=(font_name, font_size_2))],
        [sg.HorizontalSeparator()],
        [sg.Column([[imagen]], justification='center')],
        [sg.Text("""lorem ipsum dolor sit amet, consectetur adipiscing elit, sed""", font=(font_name, font_size_1))]
    ]

    window = sg.Window('Acerca de Recetas 0.1a', layout, font=(font_name,font_size_3), modal=True)
    return window