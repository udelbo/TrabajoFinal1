import PySimpleGUI as sg
from src.consts.font import *

def build():
    sg.theme('SystemDefault')
    
    categorias = [ "Aperitivos y tapas", "Arroces y cereales", "Aves y caza", "Carne", "Cócteles y bebidas", "Consejos de cocina", "Ensaladas", "Guisos y Potajes", "Huevos y lácteos", "Legumbres", "Mariscos", "Pan y bollería", "Pasta", "Pescado", "Postres", "Salsas", "Sopas y cremas", "Verduras"]
    
    layout = [
        [sg.Text('Agregar Receta', font=(font_size_3))],
        [sg.HorizontalSeparator()],
        [sg.Text("Titulo", size=(15, 1)), sg.Input(size=(30, 1), key='-TITULO-')],
        [sg.Text("Categoria", size=(15, 1)), sg.Combo(categorias, default_value=categorias[0], size=(24, 1), key='-CATEGORIA-', readonly=True)],
        [sg.Text("Complejidad", size=(15, 1)), sg.Input(size=(30, 1), key='-COMPLEJIDAD-')],
        [sg.Text("Tiempo", size=(15, 1)), sg.Spin(list(range(99999)), size=(10,1), key='-TIEMPO-')],
        [sg.Text("Ingredientes", size=(15, 1)), sg.Multiline(size=(30, 3), key='-INGREDIENTES-')],
        [sg.Text("Receta", size=(15, 1)), sg.Multiline(size=(30, 10), key='-RECETA-')],
        [sg.Button("Guardar", size=(10, 1), key='-GUARDAR-', bind_return_key=True)]
    ]
    
    window = sg.Window('Agregar receta', layout, font=(font_size_1), modal=True)
    
    return window