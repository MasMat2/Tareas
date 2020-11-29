import datetime

Tareas = {"Materias":{
    "Probabilidad":{
        "PIA":{
            "Fecha de entrega": datetime.datetime(2020, 12, 7, 23, 59), 
            "Partes":[
                "Pasar tabla a estructura de datos",
                "Encontrar medidas descriptivas de centralidad y dispercion",
                "Construir una tabla de frecuencias",
                "Elaborar una grafica con los porcentajes",
                "Pasar calculos y procedimientos a Word"
            ]
        },
    },
    "Ecuaciones diferenciales":{
        "Tarea 7":{
            "Fecha de entrega": datetime.datetime(2020, 11, 29, 23, 59),
            "Partes":[
                "Estudiar transformadas de Laplace",
                "Resolver problema"
            ]
        },
    },
    "Circuitos Digitales":{
        "PIA":{
            "Fecha de entrega": datetime.datetime(2020, 12, 5, 12, 0),
            "Partes":[
                "Revisar Introducion, Descripcion, Diagrama, Materiales",
                "Revisar Desarrollo con la descripcion y fotografia de cada uno de los pasos",
                "Documentar el funcionamiento con dos sumas y dos restas",
                "Hacer conslusion individual y grupal",
                "Agreagar Indice, Portada, Formato",
            ]
        },
        "Tarea":{
            "Fecha de entrega": datetime.datetime(2020, 11, 30, 16, 0),
            "Partes":[
                "Simplificar 6 ecuaciones booleanas, con tablas de verdad y mapas de karnaugh",
            ]
        },
        "Investigacion":{
            "Fecha de entrega": datetime.datetime(2020, 12, 4, 16, 0),
            "Partes":[
                "Crear layout del documento a entregar",
                "Definir concepto memoria",
                "Definir concepto de memoria Ram",
                "Investigar caracteristicas de 9 tipos de memoria",
                "Agregar conclusiones",
                "Agregar indice, introduccion, bibliografia, dar formato"
            ]
        },
    },
    "Estructuras de Datos":{
        "PIA":{
            "Fecha de entrega": datetime.datetime(2020, 12, 6, 23, 59),
            "Partes":[
                "Revisar avances y actualizar pendientes"
            ]
        },
    },
    "Laboratorio de Aplicaciones Moviles":{
        "Practicas 11-15":{
            "Fecha de entrega": datetime.datetime(2020, 12, 8, 0, 0),
            "Partes":[
                "Realizar Practica 11",
                "Realizar Practica 12",
                "Realizar Practica 13",
                "Realizar Practica 14",
                "Realizar Practica 15",
            ]
        },
    },
    "Aplicaciones Moviles":{
        "PIA":{
            "Fecha de entrega": datetime.datetime(2020, 12, 4, 23, 59),
            "Partes":[
                {
                    "Idear un proyecto Angular":{
                        "Ideas":[
                            "Clon de reddit"
                        ],
                        "Requistos":[
                            "Debe incluir al menos 3 componentes",
                            "Usar una API Rest",
                        ]
                    }
                },
                "Tipar estructuras del proyecto en Typescript",
                "Resgauardar en git",
                "Validaciones en los formularios",
                "Documentacion funcional manual o video obligatorio"
            ]
        },
        "Tarea 4":{
            "Fecha de entrega": datetime.datetime(2020, 12, 4, 23, 59),
            "Partes":[
                "Realizar presentacion de powerpoint acerca del tema que mas me haya gustado de la materia",
                {"Ideas":[
                    "Realizar presentacion acerca de las APIs"]}
                ]
        },
        "Proyecto de innovacion":{
            "Fecha de entrega": datetime.datetime(2020, 12, 3, 23, 59),
            "Partes":[
                "Actualizar tareas"
            ]
            },
    },
    "Cultura de Paz":{
        "Evidencia 3":{
            "Fecha de entrega": datetime.datetime(2020, 12, 10, 23, 59),
            "Partes":[
                "Investigar acerca de Asociación Faro en el Camino: Reinserción Social",
                "Crear layout del ensayo o resumen",
                "Desarrollar ensayo o resumen",
                "Terminar ensayo o resumen"
            ]
            },
        "Evidencia 4":{
            "Fecha de entrega": datetime.datetime(2020, 12, 10, 23, 59),
            "Partes":[
                {"Investigacion":{
                    "Identificar conflicto social; plantear la problemática.",
                    "Analizar qué estrategias se han utilizado para tratar de solucionarlo.",
                    "Hacer propuesta de estrategia de cómo lo solucionarían.",
                    "Indicar qué valores de la cultura de paz están contemplados y en qué parte de la estrategia de la propuesta están."
                }},
                "Crear layout del ensayo",
                "Desarrollar ensayo",
                "Terminar ensayo"
            ]
            },
        "Evidencia 5":{
            "Fecha de entrega": datetime.datetime(2020, 12, 7, 23, 59),
            # "Fecha de entrega": datetime.datetime(2020, 12, 10, 23, 59), #original
            "Partes":[
                "Identificar modelo de responsabilidad social",
                "Describir las acciones actuales que lleva a cabo su institución de educación superior para incluir en sus modelos educativos la educación para la paz.",
                "Identificar las áreas de oportunidad que presentan las acciones actuales de su institución.",
                "Definir idea",
                "Proponer una estrategia de mejora a favor de acciones de educación para la paz en su institución de educación superior, en concordancia con los modelos de responsabilidad social, en la que se incluyan: descripción, objetivos, alcances, impacto social y beneficios.",
                "Crear layout del ensayo",
                "Desarrollar ensayo",
                "Terminar ensayo"
            ]
        },
        "PIA":{
            "Fecha de entrega": datetime.datetime(2020, 12, 11, 23, 59),
            "Partes":[
                "Terminar evidencia 5",
                "Organizar campaña para promover la cultura de paz en el contexto local e inmediato",
                "Actualizar tareas",
                "Crear layout",
                "Desarrollar campania",
                "Terminar campania"
            ]
            },
    },
}}

def count(structure):
    if isinstance(structure, (str, datetime.datetime)):
        return 1
    
    if isinstance(structure, list):
        return len(structure)
    
    if not isinstance(structure, dict):
        print(type(structure))
        raise ValueError


    suma = 0
    for key, value in structure.items():
        suma += count(value)
    
    return suma


dinamic_to_do = []
for materia, tareas in Tareas["Materias"].items():
    for tarea, detalles in tareas.items():
        fecha = detalles["Fecha de entrega"]
        puntos = count(detalles["Partes"])+1
        delta_t = (fecha - datetime.datetime.now())/puntos
        for index in range(len(detalles["Partes"])):
            dinamic_to_do.append((delta_t*(index+1)+datetime.datetime.now(), detalles["Partes"][index]))

for i in (sorted(dinamic_to_do, key=lambda x: x[0])):
    print(f'{i[0].strftime("%d/%m/%Y %H:%M:%S")}    {i[1]}')

print(datetime.datetime.now())
# print(count(tareas["Materias"]["Circuitos Digitales"]))