import PySimpleGUI as sg
from src.windows import ingresar_receta
from src.handlers import ingresar_receta_handler

def start():
    """
    lanza la ventana
    """
    window = loop()
    window.close()
    
def loop():
    """
    loop de la ventana de menu que capta eventos al apretar opciones
    """
    window = ingresar_receta.build()
    
    while True:
        event, values = window.read()
        
        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-", "Salir"):
            break
        elif event == '-GUARDAR-':
            #guardar datos
            ingresar_receta_handler.agregar_receta(values)
            sg.popup('Receta almacenada.')
            break
    return window