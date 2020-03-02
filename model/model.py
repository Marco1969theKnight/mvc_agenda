from .contacto import Contacto
from .cita import Cita

class Model:

    def __init__(self):
        self.contactos = []
        self.citas = []

    def esta_id(self, id_contacto):
        for c in self.contactos:
            if c.id_contacto == id_contacto:
                return True, c
        return False, 0

    def esta_c_id(self, id_cita):
        for c in self.citas:
            if c.id_cita == id_cita:
                return True, c
        return False, 0

    #Contacto methods

    def agregar_contacto(self, id_contacto, nombre, tel, correo, dir):
        e, c = self.esta_id(id_contacto)
        if not e:
            c = Contacto(id_contacto, nombre, tel, correo, dir)
            self.contactos.append(c)
            return True, c
        return False, c
    
    def leer_contacto(self, id_contacto):
        e, c = self.esta_id(id_contacto)
        return e, c
    
    def actualizar_contacto(self, id_contacto, n_nombre, n_tel, n_correo, n_dir):
        e, c = self.esta_id(id_contacto)
        if e:
            if not n_nombre == '':
                c.nombre = n_nombre
            if not n_tel == '':
                c.tel = n_tel
            if not n_correo == '':
                c.correo = n_correo
            if not n_dir == '':
                c.dir = n_dir
            return True
        return False
    
    def borrar_contacto(self, id_contacto):
        e, c = self.esta_id(id_contacto)
        if e:
            self.contactos.remove(c)
            lista_temp = [c for c in self.citas if c.id_contacto == id_contacto]
            for c in lista_temp:
                self.citas.remove(c)
            return True
        return False
    
    def lista_contactos(self):
        n = input('Ingrese la letra: ')
        for indice in range(len(self.contactos)):
            if self.contactos[indice].nombre[0] == n[0]:
                print(self.contactos[indice].nombre)
                print(self.contactos[indice].tel)
                print(self.contactos[indice].correo)
                print(self.contactos[indice].dir)
    
    def leer_contactos_letra(self, letra):
        lista = [c for c in self.contactos if c.nombre.lower().startswith(letra.lower())]
        return lista
    
    def leer_todos_contactos(self):
        return self.contactos

    #Cita methods

    def agregar_cita(self, id_cita, id_contacto, lugar, fecha, hora, asunto):
        e, c = self.esta_c_id(id_cita)
        if not e:
            if self.esta_id(id_contacto)[0]:
                c = Cita(id_cita, id_contacto, lugar, fecha, hora, asunto)
                self.citas.append(c)
                return True, c
        return False, c

    def leer_cita(self, id_cita):
        e, c = self.esta_c_id(id_cita)
        return e, c

    def actualizar_cita(self, id_cita, n_id_contacto, n_lugar, n_fecha, n_hora, n_asunto):
        e, c = self.esta_c_id(id_cita)
        if e:
            if not n_id_contacto == 0:
                c.id_contacto = n_id_contacto
            if not n_lugar == '':
                c.lugar = n_lugar
            if not n_fecha == '':
                c.fecha = n_fecha
            if not n_hora == '':
                c.hora = n_hora
            if not n_asunto == '':
                c.asunto = n_asunto
            return True
        return False

    def borrar_cita(self, id_cita):
        e, c = self.esta_c_id(id_cita)
        if e:
            self.citas.remove(c)
            return True
        return False

    def lista_citas_fecha(self, fecha):
        for indice in range(len(self.citas)):
            if self.citas[indice].fecha == fecha:
                print(self.citas[indice].id_contacto)
                print(self.citas[indice].lugar)
                print(self.citas[indice].fecha)
                print(self.citas[indice].hora)
                print(self.citas[indice].asunto)

    def leer_citas_fecha(self, fecha):
        lista = [c for c in self.citas if c.fecha == fecha]
        return lista
    
    def leer_todas_citas(self):
        return self.citas
