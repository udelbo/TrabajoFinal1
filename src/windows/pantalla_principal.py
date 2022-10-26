from datetime import date
import PySimpleGUI as sg
from src.consts.font import *

def build():
    """
    construye ventana principal
    """
    #poner primero el theme sino no funca
    sg.theme('SystemDefault')
    
    menu_def = [['&Archivo', ['!&Abrir', '&Guardar::guardarkey', '---', '&Propiedades', 'E&xit']],
            ['!&Edit', ['!&Paste', ['Special', 'Normal', ], 'Undo'], ],
            ['&Ventanas nuevas', ['Ventana &1', 'Ventana &2']],
            ['&Ayuda', '&Acerca de...'], ]
    
    layout = [
        [sg.Menu(menu_def)],
        [sg.Text(f'Recetas', font=(font_name, font_size_2), size=(30, 1)),
         sg.Text(f'{date.today().strftime("%d/%m/%Y")}', font=(font_name, font_size_2), size=(30, 1), justification="r")
        ],
        [sg.HorizontalSeparator()],
        [sg.Button("Agregar receta", key="-INGRESAR_RECETA-", font=(font_name, font_size_1))],
        [sg.Table(values=[["-","-","-","-","-","-"]], key="-TABLA_RECETAS-", 
                justification="c", enable_events=True, enable_click_events=True, 
                headings=[" Título ", " Complejidad ", " Tiempo ", " Ingredientes ", " Receta ", " Categoria "],
                row_height=20, num_rows=8, header_background_color="#009AAE", header_text_color="#FFFFFF"
        )],
        [sg.Text('Receta seleccionada', font=(font_name, font_size_2), size=(30, 1))],  
        [sg.HorizontalSeparator()], 
        
        [sg.Text("Titulo", size=(15, 1)), sg.Input(size=(78, 1), key='-VER_TITULO-', disabled=True)],
        [sg.Text("Categoria", size=(15, 1)), sg.Input(size=(78, 1), key='-VER_CATEGORIA-', disabled=True)],
        [sg.Text("Complejidad", size=(15, 1)), sg.Input(size=(78, 1), key='-VER_COMPLEJIDAD-', disabled=True)],
        [sg.Text("Tiempo", size=(15, 1)), sg.Spin(list(range(99999)), size=(10,1), key='-VER_TIEMPO-', disabled=True)],
        [sg.Text("Ingredientes", size=(15, 1)), sg.Multiline(size=(78, 3), key='-VER_INGREDIENTES-', disabled=True)],
        [sg.Text("Receta", size=(15, 1)), sg.Multiline(size=(78, 10), key='-VER_RECETA-', disabled=True)],
        
    ]
    
    window = sg.Window("Sistema Recetas 0.1a", layout=layout, resizable=True, finalize=True)
    
    return window