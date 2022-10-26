import json

def agregar_receta(datos_nuevos):
    """guardar datos de la receta en el json
    Args:
        datos_nuevos (_type_): _description_
    """
    
    with open('files/recetas.json', 'r') as archivo:
        lista_recetas = json.load(archivo) #carga todos las recetas
    if not lista_recetas:
        id_nuevo = 1
    else:
        id_nuevo = int(max(lista_recetas, key=lambda x:x['id'])['id']) + 1
    datos_nuevos['id'] = id_nuevo
    lista_recetas.append(datos_nuevos)
    with open('files/recetas.json', 'w') as archivo:
        json.dump(lista_recetas, archivo, indent=4)
        
def leer_archivo():
    """
    Lee todos los datos de recetas.json y los devuelve como una lista de diccionarios
    """
    with open('files/recetas.json', 'r') as file:  # r para leer
        datos = json.load(file)  # json.load(file) para leerlo como un diccionario
    datos_para_tabla = []
    for dato in datos:
        datos_para_tabla.append([dato["-TITULO-"], dato["-COMPLEJIDAD-"], dato["-TIEMPO-"], dato["-INGREDIENTES-"], dato["-RECETA-"], dato["-CATEGORIA-"]])
    return datos_para_tabla
