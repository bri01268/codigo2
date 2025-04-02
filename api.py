from fastapi import FastAPI, Query
import pyodbc

app = FastAPI()

# Configuración de conexión a SQL Server
conn_str = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=MovistarTelecom;"
    "Trusted_Connection=yes;"
)

@app.get("/tabla/{nombre_tabla}")
async def obtener_datos_tabla(
    nombre_tabla: str,
    columna_filtro: str = Query(None, description="Nombre de la columna para filtrar"),
    valor_filtro: str = Query(None, description="Valor de la columna para filtrar")
):
    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()

        # Validar que la tabla existe
        cursor.execute(
            "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = ?", 
            (nombre_tabla,)
        )
        if not cursor.fetchone():
            return {"error": "La tabla no existe"}

        # Construcción dinámica de la consulta con filtros
        query = f"SELECT * FROM {nombre_tabla}"
        params = []

        if columna_filtro and valor_filtro:
            query += f" WHERE {columna_filtro} = ?"
            params.append(valor_filtro)

        cursor.execute(query, params)
        columnas = [column[0] for column in cursor.description]
        datos = [dict(zip(columnas, row)) for row in cursor.fetchall()]

        cursor.close()
        conn.close()

        return {
            "total_registros": len(datos),
            "datos": datos
        }
    except Exception as e:
        return {"error": str(e)}


