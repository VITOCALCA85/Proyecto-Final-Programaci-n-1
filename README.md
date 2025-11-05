# Proyecto-Final-Programación 1

**Inventario de Mapas para Primaria y EBI:  es una aplicación en Python con interfaz gráfica (Tkinter) y base de datos SqLite.

En este proyecto final, pensamos en un sistema ágil para para consultar, registrar, categorizar, almacenar y buscar mapas. 

En el inventario aparecerá la siguiente información sobre cada mapa:título,fecha,autor,tipo y el enlace al archivo de cada mapa. Pensando que cada mapa pueda descargarse.

Podría ser usado por Maestras en las escuelas y docentes de Historia/Geografía en EBI.

*Utilizamos: -tkinter (interfaz gráfica)
             -sqlite (persistencia)
             -pytest (para pruebas unitarias, opcional)

Se utilizó la técnica del encapsulamiento para proteger los datos y acceder a través de métodos públicos. Este inventario permite la búsqueda y organización adecuada en Primaria y Secundaria. Se utilizan atributos privados y se controlan con con getters y setters. Esto es clave para enseñar buenas prácticas de POO.
Los docstrings explican qué hace cada clase.
El mapa representa un recurso educativo.
El InventarioMapas gestiona un conjunto de recursos.
Hay principios de diseño limpio. Al buscar por título se usar "lower" para búsquedas no sensibles a mayúsculas y minúsculas.







