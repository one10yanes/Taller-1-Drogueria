import funciones
from conexion import DAO


#Menu Principal-----------------------------------------------------------------------------

def menuPrincipal():
        continuar = True
        while(continuar):
            opcionCorrecta = False
            while(not opcionCorrecta):
                print("==================== Drogueria La Principal ====================")
                print("1.- Clientes")
                print("2.- Productos")
                print("3.- Facturas")
                print("0.- Salir")
                print("========================================================")
                opcion = int(input("Seleccione una opción: "))

                if opcion < 0 or opcion > 3:
                    print("Opción incorrecta, ingrese nuevamente...")
                elif opcion == 0:
                    continuar = False
                    print("¡Gracias por usar este sistema!")
                    break
                else:
                    opcionCorrecta = True
                    ejecutarOpcionMP(opcion)



#Disparador Menu Principal-----------------------------------------------------------------------------
def ejecutarOpcionMP(opcion):
    
        if opcion == 1:
                    continuar = True
        while(continuar):
            opcionCorrecta = False
            while(not opcionCorrecta):
                print("==================== Drogueria La Principal ====================")
                print("1.- Listar Clientes")
                print("2.- Crear Clientes")
                print("3.- Actualizar Clientes")
                print("4.- Eliminar Clientes")
                print("0.- Salir")
                print("========================================================")
                opcion = int(input("Seleccione una opción: "))

                if opcion < 0 or opcion > 4:
                    print("Opción incorrecta, ingrese nuevamente...")
                elif opcion == 0:
                    continuar = False
                    break
                else:
                    opcionCorrecta = True
                    subOpCliente(opcion)
                    
#*********************************************************************************************************       
        if opcion == 2:
                continuar = True
        while(continuar):
            opcionCorrecta = False
            while(not opcionCorrecta):
                print("==================== Drogueria La Principal ====================")
                print("1.- Listar Productos")
                print("2.- Crear Productos")
                print("3.- Eliminar Eliminar")
                print("4.- Actualizar Productos")
                print("0.- Regresar")
                print("========================================================")
                opcion = int(input("Seleccione una opción: "))

                if opcion < 0 or opcion > 4:
                    print("Opción incorrecta, ingrese nuevamente...")
                elif opcion == 0:
                    continuar = False
                    break
                else:
                    opcionCorrecta = True
                    subOpProd(opcion)
                    
#*********************************************************************************************************            
        
                if opcion == 3:
                   continuar = True
        while(continuar):
            opcionCorrecta = False
            while(not opcionCorrecta):
                print("==================== Drogueria La Principal ====================")
                print("1.- Listar Facturas")
                print("2.- Crear Facturas")
                print("3.- Eliminar Facturas")
                print("4.- Actualizar Facturas")
                print("0.- Regresar")
                print("========================================================")
                opcion = int(input("Seleccione una opción: "))

                if opcion < 0 or opcion > 4:
                    print("Opción incorrecta, ingrese nuevamente...")
                elif opcion == 0:
                    continuar = False
                    break
                else:
                    opcionCorrecta = True
                    subOpFac(opcion)
                    
#************************************************************************************************

           
                    
 #Disparador Cliente----------------------------------------------------------------------------                
                   
def subOpCliente(opcion):
        dao = DAO()
        if opcion == 1:
            try:
                clientes = dao.listarClientes()
                if len(clientes) > 0:
                    funciones.listarClientes(clientes)
                else:
                    print("No se encontraron clientes creados...")
            except:
                print("Ocurrió un error ...")
        
        elif opcion == 2:
            clNuevo = funciones.crearClientes()
            try:
                dao.crearClientes(clNuevo)
            except:
                print("Ocurrió un error...")
        
        elif opcion == 3:
            try:
                cliente = funciones.actualizarClientes()
                dao.actualizarClientes(cliente)
            except:
                print("Error interno de la plataforma! ")
            
        elif opcion == 4:
            try:
                clientes = dao.listarClientes()
                idCliente = int(input("Ingrese el id del cliente a eliminar... "))
                if(clientes[0] == idCLiente):
                    dao.eliminarClientes(idCliente)
                    print("Cliente eliminado con exito!")
            except:
                print("El cliente no se encuentra en la base de datos...")       
                       
menuPrincipal()
