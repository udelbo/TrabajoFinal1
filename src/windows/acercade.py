import sys, os
import PySimpleGUI as sg
from src.consts.font import *
from src.component.img_ruta_absoluta import resource_path

def resource_path(relative_path):
    """ Obtiene la ruta absoluta a un recurso, funciona para dev y para PyInstaller """
    try:
        # PyInstaller crea una carpeta temporal y guarda la ruta en _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


sg.theme('SystemDefault')

def build():

    imagen = sg.Image(resource_path("src/resources/images/pysimplegui.png"))

    layout = [
        [sg.Text('Acerca de...', font=(font_name, font_size_2))],
        [sg.HorizontalSeparator()],
        [sg.Column([[imagen]], justification='center')],
        [sg.Text("""lorem ipsum dolor sit amet, consectetur adipiscing elit, sed""", font=(font_name, font_size_1))]
    ]

    window = sg.Window('Acerca de Recetas 0.1a', layout, font=(font_name,font_size_3), modal=True, icon=r'src/resources/images/Recetas.ico')
    return window