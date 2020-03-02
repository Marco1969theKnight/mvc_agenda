from model.contacto import Contacto
from model.cita import Cita
from model.model import Model
from view.view import View
from controller.controller import Controller

"""c1 = Contacto(1, 'Juan Perez', '464-123-1234', 'jp@gmail.com', 
                'Arteaga No 432, Calle Lopez Mateos, San Miguel')
print(c1.nombre)
print(c1.tel)
print(c1.correo)
print(c1.dir)

contactos = []

contactos.append(c1)

c2 = Contacto(2, 'Jose Peralez', '464-321-8765', 'jos@gmail.com', 'Centro No 765, Avenida Guerrero, Salamanca')
c3 = Contacto(3, 'Martin Rosalez', '462-539-0203', 'mr@gmail.com', 'Deportiva No 1888, Avenida Reforma, Irapuato')

t1 = Cita(1, 1, 'Aula 310', '20-02-2020', '14:00', 'Clase de Sistemas de Informacion')

contactos.append(c2)
contactos.append(c3)

#guess = input('Dame un nombre:')

for indice in range(len(contactos)) :
    if contactos[indice].nombre == guess :
        print('si esta')
        break
    if indice == len(contactos) - 1 :
        if contactos[indice].nombre != guess:
            print('no esta')

for c in contactos:
    if guess.lower() == c.nombre.lower():
        print('si esta')
        break
    else :
        print('no esta')


m = Model()
m.agregar_contacto(1, 'Juan Perez', '464-123-1234', 'jp@gmail.com', 'Arteaga No 432, Calle Lopez Mateos, San Miguel')
m.agregar_contacto(2, 'Jose Peralez', '464-321-8765', 'jos@gmail.com', 'Centro No 765, Avenida Guerrero, Salamanca')
m.agregar_contacto(3, 'Martin Rosalez', '462-539-0203', 'mr@gmail.com', 'Deportiva No 1888, Avenida Reforma, Irapuato')
m.agregar_contacto(4, 'Mauricio Corrales', '462-940-1122', 'mc@gmail.com', 'Espanita No 425, Avenida Jacarandas, Silao')

m.agregar_cita(1, 2, 'Tacos la Herradura', '22-02-2020', '20:00', 'salida con amigos')
m.agregar_cita(2, 4, 'Aula 310', '22-02-2020', '14:00', 'Clase de Sistemas de Informacion')
m.agregar_cita(3, 1, 'Casa', '22-02-2020', '7:00', 'Cita con el medico')
m.agregar_cita(4, 3, 'Plaza de toros', '29-02-2020', '15:00', 'Ir a la corrida de toros')

v = View()
s = m.leer_todos_contactos()
v.mostrar_contactos(s)
c = m.leer_contacto(1)
v.mostrar_contacto(c)

f = m.borrar_contacto(1)
if f:
    v.borrar_contacto(c)
else:
    v.contacto_no_existe(1)

s = m.leer_todas_citas()
v.mostrar_citas(s)
c = m.leer_cita(1)
v.mostrar_cita(c)

f = m.borrar_cita(1)
if f:
    v.borrar_cita(c)
else:
    v.cita_no_existe(1)
"""

cont = Controller()
cont.start()
