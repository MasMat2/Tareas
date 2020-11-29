import datetime

tareas = {"Materias":{
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
            datetime.datetime(2020, 11, 29, 23, 59),
            "Partes":[
                "Estudiar transformadas de Laplace",
                "Resolver problema"
            ]
        },
    },
    "Circuitos Digitales":{
        "PIA":{
            datetime.datetime(2020, 12, 5, 12, 0),
            "Partes":[
                "Revisar Introducion, Descripcion, Diagrama, Materiales",
                "Revisar Desarrollo con la descripcion y fotografia de cada uno de los pasos",
                "Documentar el funcionamiento con dos sumas y dos restas",
                "Hacer conslusion individual y grupal",
                "Agreagar Indice, Portada, Formato",
            ]
        },
        "Tarea":{
            datetime.datetime(2020, 11, 30, 16, 0),
            "Partes":{
                "Simplificar 6 ecuaciones booleanas, con tablas de verdad y mapas de karnaugh",
            }
        },
        "Investigacion":{
            datetime.datetime(2020, 12, 4, 16, 0)
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
            datetime.datetime(2020, 12, 6, 23, 59)
            "Partes":[
                "Revisar avances y actualizar pendientes"
            ]
        },
    },
    "Laboratorio de Aplicaciones Moviles":{
        "Practicas 11-15":{
            datetime.datetime(2020, 12, 8, 0, 0),
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
            datetime.datetime(2020, 12, 4, 23, 59),
            "Partes":[
                {
                    "Idear un proyecto Angular":{
                        "Ideas":[
                            "Clon de reddit"
                        ]
                        "Requistos":[
                            "Debe incluir al menos 3 componentes",
                            "Usar una API Rest",
                        ]
                    }
                }
                "Tipar estructuras del proyecto en Typescript",
                "Resgauardar en git",
                "Validaciones en los formularios",
                "Documentacion funcional manual o video obligatorio"
            ]
        },
        "Tarea 4":{
            datetime.datetime(2020, 12, 4, 23, 59),
            "Partes":[
                "Realizar presentacion de powerpoint acerca del tema que mas me haya gustado de la materia",
                {"Ideas":[
                    "Realizar presentacion acerca de las APIs"]}
                ]
        },
        "Proyecto de innovacion":{datetime.datetime(2020, 12, 3, 23, 59)},
    },
    "Cultura de Paz":{
        "Evidencia 3":{
            datetime.datetime(2020, 12, 10, 23, 59),
            "Partes":{
                "Investigar acerca de Asociación Faro en el Camino: Reinserción Social",
                "Crear layout del ensayo o resumen",
                "Terminar mitad del ensayo o resumen",
                "Terminar ensayo o resumen"
            }
            },
        "Evidencia 4":{
            datetime.datetime(2020, 12, 10, 23, 59),
            "Partes":{
                "Investigacion":{
                    "Identificar conflicto social; plantear la problemática.",
                    "Analizar qué estrategias se han utilizado para tratar de solucionarlo.",
                    "Hacer propuesta de estrategia de cómo lo solucionarían.",
                    "Indicar qué valores de la cultura de paz están contemplados y en qué parte de la estrategia de la propuesta están."
                }
                "Crear layout del ensayo",
                "Terminar mitad del ensayo",
                "Terminar ensayo"
            }
            },
        "Evidencia 5":[
            datetime.datetime(2020, 12, 10, 23, 59),
            "Partes":[
                "Identificar modelo de responsabilidad social",
                "Describir las acciones actuales que lleva a cabo su institución de educación superior para incluir en sus modelos educativos la educación para la paz.",
                "Identificar las áreas de oportunidad que presentan las acciones actuales de su institución.",
                "Definir idea",
                "Proponer una estrategia de mejora a favor de acciones de educación para la paz en su institución de educación superior, en concordancia con los modelos de responsabilidad social, en la que se incluyan: descripción, objetivos, alcances, impacto social y beneficios.",
                "Crear layout del ensayo",
                "Terminar mitad del ensayo",
                "Terminar ensayo"
            ]
        ],
        "PIA":{datetime.datetime(2020, 12, 11, 23, 59),},
    },
}}

for materia in tareas.Materias:
    print(materia)