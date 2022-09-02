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
                print("3.- Eliminar Clientes")
                print("4.- Actualizar Clientes")
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
                usuarios = dao.listarClientes()
            
                if len(usuarios) > 0:
                    funciones.listarClientes(usuarios)
                    usuario = funciones.eliminarClientes()
                    print(usuarios)
                    for usu in usuarios:
                        print(usu[0])
                        if(usuario == usu[0]):
                            dao.eliminarClientes(usuario)
                else:
                    print ("No se Encontraron Usuarios")
            except:
                print("Ocurrió un error...")
             
            
            
            
            
            
            
                       
menuPrincipal()
