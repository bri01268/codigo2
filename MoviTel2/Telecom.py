import pyodbc
import pandas as pd

# Ruta para conectarse al SQL Server
conn_str = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=MovistarTelecom;Trusted_Connection=yes;'

# Conectar a la base de datos
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# Función para insertar datos en la tabla correspondiente
def insert_data_from_dataframe(df, table_name):
    for i, row in df.iterrows():
        columns = ', '.join(df.columns)
        values = ', '.join([f"'{str(val)}'" if isinstance(val, str) else str(val) for val in row])
        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
        cursor.execute(sql)
    conn.commit()

# Leer los archivos CSV generados
clientes = pd.read_csv('clientes.csv')
servicios = pd.read_csv('servicios.csv')
tiempo = pd.read_csv('tiempo.csv')
ubicaciones = pd.read_csv('ubicaciones.csv')
dispositivos = pd.read_csv('dispositivos.csv')
facturacion = pd.read_csv('facturacion.csv')
promociones = pd.read_csv('promociones.csv')
soporte = pd.read_csv('soporte.csv')
consumo = pd.read_csv('consumo.csv')
hechos_servicios = pd.read_csv('hechos_servicios.csv')

# Insertar datos en cada tabla
insert_data_from_dataframe(clientes, 'dim_cliente')
insert_data_from_dataframe(servicios, 'dim_servicio')
insert_data_from_dataframe(tiempo, 'dim_tiempo')
insert_data_from_dataframe(ubicaciones, 'dim_ubicacion')
insert_data_from_dataframe(dispositivos, 'dim_dispositivo')
insert_data_from_dataframe(facturacion, 'dim_facturacion')
insert_data_from_dataframe(promociones, 'dim_promociones')
insert_data_from_dataframe(soporte, 'dim_soporte')
insert_data_from_dataframe(consumo, 'dim_consumo')
insert_data_from_dataframe(hechos_servicios, 'hechos_servicios')

# Cerrar la conexión
cursor.close()
conn.close()

print("Datos insertados correctamente en la base de datos.")
