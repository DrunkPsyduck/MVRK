import pyodbc
import SystemInformation as sys
import Financial as finance
#información necesario para la conexion. BD alojada en Azure
server = 'sqlmarioc.database.windows.net'
database = 'Proyecto'
username = 'adminsql'
password = 'Admin123'   
driver= '{ODBC Driver 17 for SQL Server}'

def MainMenu():
    fin = False
    while fin==False:
        print("seleccione su opción: ")
        print("\n1:Comprobar conexion a base de datos en Azure")
        print("\n99: Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            AzureDatabaseSelect("Usuarios")
        elif opcion == "2":
            sys.SystemInformation()
        elif opcion == "3":
            finance.Menu()
        elif opcion == "99":
            fin = True
            exit()
        elif input == "":
            print("No se ha encontrado ninguna orden")

        input("Pulse cualquier tecla para continuar... ")


def AzureDatabaseSelect(tabla):
    print("Conectandose a la BBDD de Azure")
    with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM dbo."+ tabla)
            row = cursor.fetchone()
            print("IdTransacn, id")
            while row:
                print (str(row[0]) + "         " + str(row[1]))
                row = cursor.fetchone()
    print("Conexion a Azure satisfactoria")            

def InsertarDoctor():
    pint("Insertando Doctor en la tabla")
