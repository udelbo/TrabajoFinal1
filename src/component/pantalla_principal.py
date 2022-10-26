import PySimpleGUI as sg
from src.windows import pantalla_principal
from src.component import ingresar_receta, acercade
from src.handlers import ingresar_receta_handler


def start():
    """
    Lanza la ejecución de la ventana
    """
    window = loop()
    window.close()


def loop():
    """
    Loop de la ventana de menú que capta los eventos al apretar las opciones
    """

    window = pantalla_principal.build()
    window["-TABLA_RECETAS-"].update(ingresar_receta_handler.leer_archivo())

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-", "Salir"):
            break

        elif event == '-INGRESAR_RECETA-':
            ingresar_receta.start()
            window["-TABLA_RECETAS-"].update(ingresar_receta_handler.leer_archivo())
        elif event == 'Acerca de...':
            acercade.start()
        elif event == "-TABLA_RECETAS-" and window["-TABLA_RECETAS-"].get():
            if values["-TABLA_RECETAS-"]:
                print(f'Fila selecciona de la tabla: {values["-TABLA_RECETAS-"][0]}')
                receta_seleccionada = window["-TABLA_RECETAS-"].get()[values["-TABLA_RECETAS-"][0]]
                
                window['-VER_TITULO-'].update(receta_seleccionada[0])
                window['-VER_CATEGORIA-'].update(receta_seleccionada[5])
                window['-VER_COMPLEJIDAD-'].update(receta_seleccionada[1])
                window['-VER_TIEMPO-'].update(receta_seleccionada[2])
                window['-VER_INGREDIENTES-'].update(receta_seleccionada[3])
                window['-VER_RECETA-'].update(receta_seleccionada[4])
                
                
    return window