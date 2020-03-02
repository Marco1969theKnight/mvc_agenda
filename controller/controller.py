from model.model import Model
from view.view import View

class Controller:

    #Constructor
    def __init__(self):
        self.model = Model()
        self.view = View()

    #Contacto controllers
    def agregar_contacto(self, id_contacto, nombre, tel, correo, dir):
        e, c = self.model.agregar_contacto(id_contacto, nombre, tel, correo, dir)
        if e:
            self.view.crear_contacto(c)
        else:
            self.view.contacto_ya_existe(c)
    
    def leer_contacto(self, id_contacto):
        e, c = self.model.leer_contacto(id_contacto)
        if e:
            self.view.mostrar_contacto(c)
        else:
            self.view.contacto_no_existe(id_contacto)

    def leer_contactos_letra(self, letra):
        contactos = self.model.leer_contactos_letra(letra)
        if contactos:
            self.view.mostrar_contactos(contactos)
        else:
            self.view.lista_vacia_contactos()

    def leer_todos_contactos(self):
        c = self.model.leer_todos_contactos()
        self.view.mostrar_contactos(c)

    def actualizar_contacto(self, id_contacto = 0, n_nombre = '', n_tel = '', n_correo = '', n_dir = ''):
        e = self.model.actualizar_contacto(id_contacto, n_nombre, n_tel, n_correo, n_dir)
        if e:
            self.view.actualizar_contacto(id_contacto)
        else:
            self.view.contacto_no_existe(id_contacto)
        
    def borrar_contacto(self, id_contacto):
        e, c = self.model.borrar_contacto(id_contacto)
        if e:
            self.view.borrar_contacto(id_contacto)
        else:
            self.view.contacto_no_existe(id_contacto)

    #Cita controllers
    def agregar_cita(self, id_cita, id_contacto, lugar, fecha, hora, asunto):
        e, c = self.model.agregar_cita(
            id_cita, id_contacto, lugar, fecha, hora, asunto)
        if e:
            self.view.crear_cita(c)
        else:
            self.view.cita_ya_existe(c)

    def leer_cita(self, id_cita):
        e, c = self.model.leer_cita(id_cita)
        if e:
            self.view.mostrar_cita(c)
        else:
            self.view.cita_no_existe(id_cita)

    def leer_citas_fecha(self, fecha):
        citas = self.model.leer_citas_fecha(fecha)
        if citas:
            self.view.mostrar_citas(citas)
        else:
            self.view.lista_vacia_citas()

    def leer_todos_citas(self):
        c = self.model.leer_todas_citas()
        self.view.mostrar_citas(c)

    def actualizar_cita(self, id_cita = 0, n_id_contacto = 0, n_lugar = '', n_fecha = '', n_hora = '', n_asunto = ''):
        e = self.model.actualizar_cita(id_cita, n_id_contacto, n_lugar, n_fecha, n_hora, n_asunto)
        if e:
            self.view.actualizar_cita(id_cita)
        else:
            self.view.cita_no_existe(id_cita)

    def borrar_cita(self, id_cita):
        e, c = self.model.borrar_cita(id_cita)
        if e:
            self.view.borrar_cita(id_cita)
        else:
            self.view.cita_no_existe(id_cita)

    #Menu controllers
    def insertar_contactos(self):
        self.agregar_contacto(1, 'Juan Perez', '464-123-1234', 'jp@gmail.com', 'Arteaga No 432, Calle Lopez Mateos, San Miguel')
        self.agregar_contacto(2, 'Jose Peralez', '464-321-8765', 'jos@gmail.com', 'Centro No 765, Avenida Guerrero, Salamanca')
        self.agregar_contacto(3, 'Martin Rosalez', '462-539-0203', 'mr@gmail.com', 'Deportiva No 1888, Avenida Reforma, Irapuato')
        self.agregar_contacto(4, 'Mauricio Corrales', '462-940-1122', 'mc@gmail.com', 'Espanita No 425, Avenida Jacarandas, Silao')

    def insertar_citas(self):
        self.agregar_cita(1, 2, 'Tacos la Herradura', '22-02-2020', '20:00', 'salida con amigos')
        self.agregar_cita(2, 4, 'Aula 310', '22-02-2020', '14:00', 'Clase de Sistemas de Informacion')
        self.agregar_cita(3, 1, 'Casa', '22-02-2020', '7:00', 'Cita con el medico')
        self.agregar_cita(4, 3, 'Plaza de toros', '29-02-2020', '15:00', 'Ir a la corrida de toros')

    def menu(self):
        #Display menu
        o = '0'
        while (o != '9'):
            self.view.menu()
            o = input('Selecciona una opcion (1-9): ')
            if o == '1':
                c1 = int(input('Id_contacto: '))
                c2 = input('Nombre: ')
                c3 = input('Telefono: ')
                c4 = input('Correo: ')
                c5 = input('Direccion: ')
                self.agregar_contacto(c1, c2, c3, c4, c5)
                pass
            elif o == '2':
                c1 = int(input('Id_cita: '))
                c2 = int(input('Id_contacto: '))
                c3 = input('Lugar: ')
                c4 = input('Fecha: ')
                c5 = input('Hora: ')
                c6 = input('Asunto: ')
                self.agregar_cita(c1, c2, c3, c4, c5, c6)
                pass
            elif o == '3':
                c1 = int(input('Id_contacto: '))
                c2 = input('Nombre: ')
                c3 = input('Telefono: ')
                c4 = input('Correo: ')
                c5 = input('Direccion: ')
                self.actualizar_contacto(c1, c2, c3, c4, c5)
                pass
            elif o == '4':
                c1 = int(input('Id_cita: '))
                c2 = int(input('Id_contacto: '))
                c3 = input('Lugar: ')
                c4 = input('Fecha: ')
                c5 = input('Hora: ')
                c6 = input('Asunto: ')
                self.actualizar_cita(c1, c2, c3, c4, c5, c6)
                pass
            elif o == '5':
                c1 = int(input('Id_contacto: '))
                self.borrar_contacto(c1)
                pass
            elif o == '6':
                c1 = int(input('Id_cita: '))
                self.borrar_cita(c1)
                pass
            elif o == '7':
                c1 = input('Primer letra del nombre: ')
                self.leer_contactos_letra(c1)
                pass
            elif o == '8':
                c1 = input('Fecha de cita: ')
                self.leer_citas_fecha(c1)
                pass
            elif o == '9':
                self.view.end()
            else:
                self.view.opcion_no_valida()


    def start(self):
        #Display a welcome message
        self.view.start()
        #Insertar data in model
        self.insertar_contactos()
        self.insertar_citas()
        #Show all contacts in DB
        self.leer_todos_contactos()
        self.leer_todos_citas()
        #Show menu
        self.menu()
