# Proyecto_Modular
Desarrollo del proyecto modular a entregar en Noviembre 2025

Integrantes del equipo:
  *  Tristan Caro Crhistopher
  *  Franco Gonzalez Karla Angela
  *  Navarro Rodriguez Damian

Metodologia de trabajo:
  Los miembros del equipo de trabajo buscaran solucionar una problematica con soluciones tecnologicas.
  Para el presente trabajo se selecciono la agilidad de alimentacion y la optimizacion de tiempos de entrega y espera de alimentos
  al crear un software orientado a alumnos, administrativos y academicos que pudieran estar dentro de las instalaciones del centro
  que busquen saciar su apetito con alimentos internos de las instalaciones en las multiples cafeterias que se encuentran al interior
  del plantel. Al ofrecer un menu y una previsualizacion de los alimentos y/o bebidas donde los propios estudiantes, administrativos
  y personal interno de las instalaciones (**Usuarios**) tendran la facilidad de pre-ordenar sus alimentos, las multiples cafeterias
  dentro de las instalaciones (**Clientes**), podran mostrar su menu asi como los precios de sus productos, para que ellos solo sean
  los encargados de preparar los alimentos y recibir el pago correspondiente, ayudando asi a disminuir las cargas de trabajo que por
  momentos podria tornarse agotadora con tantos pedidos pendientes por preparar.

Lenguajes y herramientas utilizadas:
  Lenguaje de programacion:
    Para el presente proyecto se apoyara de un lenguaje de programacion tan practico y eficiente como lo es **Python**, esto debido a
    su facilidad para manejar una gran cantidad de datos y su sintaxis intuitiva

  Base de datos:
    Todo sistema requiere de un buen almacenamiento, por lo tanto se utilizara PostgreSQL como base de datos principal para la gestion
    de la informacion y modificaciones que pudieran surgir durante el proceso

  Acceso a la informacion:
    Para evitar una sobrecarga en nuestro sistema optaremos por utilizar una metodologia llamada "pool connection" la cual nos permite
    tener una serie definida de conexiones siempre abiertas para accesar a la base de datos, de esta manera cuando una consulta obtenga 
    su resultado, dicha conexion se cierra con la peticion pero la conexion hacia la base de datos se mantiene abierta
  
