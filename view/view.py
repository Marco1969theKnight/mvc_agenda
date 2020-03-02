class View:
    #Vista contactos
    def mostrar_contacto(self, contacto):
        print('****** Datos del contacto ******')
        print('Nombre:', contacto.nombre)
        print('Telefono:', contacto.tel)
        print('Correo:', contacto.correo)
        print('Direccion:', contacto.dir)
        print('********************************')

    def mostrar_contactos(self, contactos):
        print('********** Contactos **********')
        for c in contactos:
            print(c.nombre, c.tel, c.correo, c.dir)
        print('*******************************')

    def lista_vacia_contactos(self):
        print('No hay contactos')

    def crear_contacto(self, contacto):
        print(contacto.nombre, 'se ha agregado a la base de datos!')
    
    def borrar_contacto(self, contacto):
        print(contacto.nombre, 'se ha borrado de la base de datos')

    def actualizar_contacto(self, contacto,):
        print(contacto.nombre, 'se ha modificado correctamente!')

    def contacto_ya_existe(self, contacto):
        print('EL CONTACTO', contacto.id_contacto, 'YA EXISTE EN LA BASE DE DATOS')
    
    def contacto_no_existe(self, contacto):
        print('EL CONTACTO', contacto.nombre, 'NO EXISTE EN LA BASE DE DATOS')

    #Vista citas
    def mostrar_cita(self, cita):
        print('****** Datos de la cita ******')
        print('Contacto:', cita.id_contacto)
        print('Lugar:', cita.lugar)
        print('Fecha:', cita.fecha)
        print('Hora:', cita.hora)
        print('Asunto:', cita.asunto)
        print('******************************')

    def mostrar_citas(self, citas):
        print('********** Citas **********')
        for c in citas:
            print(c.id_contacto, c.lugar, c.fecha, c.hora, c.asunto)
        print('***************************')

    def lista_vacia_citas(self):
        print('No hay citas')

    def crear_cita(self, cita):
        print(cita.fecha, cita.asunto, 'se ha agregado a la base de datos!')

    def borrar_cita(self, cita):
        print(cita.fecha, cita.asunto, 'se ha borrado de la base de datos')

    def actualizar_cita(self, cita):
        print(cita.fecha, cita.asunto, 'se ha modificado correctamente!')

    def cita_ya_existe(self, cita):
        print('LA CITA', cita.id_cita, 'YA EXISTE EN LA BASE DE DATOS')

    def cita_no_existe(self, cita):
        print('LA CITA', cita.id_cita, 'NO EXISTE EN LA BASE DE DATOS')

    #Vista menus
    def start(self):
        print('Esto es un ejemplo de vista sencilla')

    def menu(self):
        print('*****Programa de citas y contactos*****')
        print('1. Agregar contacto')
        print('2. Agregar cita')
        print('3. Modificar contacto')
        print('4. Modificar cita')
        print('5. Eliminar contacto')
        print('6. Eliminar cita')
        print('7. Buscar contacto')
        print('8. Buscar cita')
        print('9. Salir del programa')

    def opcion_no_valida(self):
        print('Esta opcion no es valida')

    def end(self):
        print('Hasta la vista!')
