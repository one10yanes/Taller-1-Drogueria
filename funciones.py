def listarClientes(clientes):
    print("\n******CLientes Creados***** \n")
    contador = 1
    for cl in clientes:
        datos = "{0} | Nombre Cliente: {1} | Telefono: {2} "
        print(datos.format( cl[0], cl[1], cl[2]))
    print(" ")
    
def crearClientes():
    nomCl = input("Ingrese el nombre del Cliente: ")
    nroTel = input("Ingrese su numero Telefonico: ")
    datos = (nomCl, nroTel)
    return datos

def eliminarClientes():
    idCl = input("Ingrese el ID del cliente a eliminar: ")
    return idCl