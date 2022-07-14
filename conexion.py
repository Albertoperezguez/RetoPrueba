def __init__(self):
        self.conexion = mysql.connector.connect(
             host='localhost',
             database ='BBVA',
             port = '1433', 
             user = 'sa',
             password ='root')


def mostrar_productos(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM productos " 
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

def busca_producto(self, nombre_producto):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM productos WHERE NOMBRE = {}".format(nombre_producto)
        cur.execute(sql)
        nombreX = cur.fetchall()
        cur.close()     
        return nombreX 