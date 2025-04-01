import pandas as pd
import random
from faker import Faker

# Usar Faker con idioma en español (España)
fake = Faker('es_ES')  # Usando Faker para generar datos en español (España)
Faker.seed(42)
random.seed(42)

# Generar datos para dim_cliente
num_clientes = 2000
clientes = pd.DataFrame({
    'id_cliente': range(1, num_clientes + 1),
    'nombre': [fake.first_name() for _ in range(num_clientes)],
    'apellido': [fake.last_name() for _ in range(num_clientes)],
    'tipo_plan': [random.choice(['prepago', 'postpago']) for _ in range(num_clientes)],
    'segmento': [random.choice(['corporativo', 'residencial']) for _ in range(num_clientes)],
    'edad': [random.randint(18, 70) for _ in range(num_clientes)],
    'sexo': [random.choice(['M', 'F']) for _ in range(num_clientes)]
})

# Generar datos para dim_servicio
servicios = pd.DataFrame({
    'id_servicio': range(1, 6),
    'tipo_servicio': ['llamada móvil', 'llamada fija', 'TV', 'internet', 'datos móviles'],
    'descripcion': [fake.sentence() for _ in range(5)],
    'empresa_proveedor': ['Movistar'] * 5
})

# Generar datos para dim_tiempo
fechas = pd.date_range(start='2024-01-01', periods=30)
tiempo = pd.DataFrame({
    'id_tiempo': range(1, 31),
    'fecha': fechas,
    'año': fechas.year,
    'mes': fechas.month,
    'día': fechas.day,
    'día_semana': fechas.day_name(),
    'trimestre': fechas.quarter
})

# Generar datos para dim_ubicacion
ubicaciones = pd.DataFrame({
    'id_ubicacion': range(1, 11),
    'pais': ['Perú'] * 10,  # Actualizar país a Perú
    'ciudad': [fake.city() for _ in range(10)],
    'zona': [random.choice(['urbana', 'rural']) for _ in range(10)]
})

# Generar datos para dim_dispositivo
dispositivos = pd.DataFrame({
    'id_dispositivo': range(1, 6),
    'tipo_dispositivo': ['celular', 'teléfono fijo', 'TV', 'router', 'tablet'],
    'marca': [fake.company() for _ in range(5)],
    'modelo': [fake.word() for _ in range(5)],
    'sistema_operativo': random.choices(['Android', 'iOS', 'Windows', 'Linux', 'Otro'], k=5)
})

# Generar datos para dim_facturacion
num_facturas = 50
facturacion = pd.DataFrame({
    'id_facturacion': range(1, num_facturas + 1),
    'metodo_pago': [random.choice(['tarjeta de crédito', 'transferencia', 'efectivo', 'débito']) for _ in range(num_facturas)],
    'fecha_pago': [fake.date_this_year() for _ in range(num_facturas)],
    'monto': [round(random.uniform(10, 100), 2) for _ in range(num_facturas)]
})

# Generar datos para dim_promociones
promociones = pd.DataFrame({
    'id_promocion': range(1, 6),
    'descripcion': [fake.sentence() for _ in range(5)],
    'descuento': [round(random.uniform(5, 50), 2) for _ in range(5)],
    'fecha_inicio': [fake.date_this_year() for _ in range(5)],
    'fecha_fin': [fake.date_this_year() for _ in range(5)]
})

# Generar datos para dim_soporte
soporte = pd.DataFrame({
    'id_soporte': range(1, 6),
    'tipo_incidencia': ['caída servicio', 'reclamo facturación', 'fallo técnico', 'consulta', 'instalación'],
    'descripcion': [fake.sentence() for _ in range(5)],
    'tiempo_resolucion': [round(random.uniform(1, 48), 2) for _ in range(5)]
})

# Generar datos para dim_consumo
consumo = pd.DataFrame({
    'id_consumo': range(1, 6),
    'tipo_consumo': ['minutos', 'MB', 'GB', 'MB', 'GB'],
    'cantidad': [round(random.uniform(1, 100), 2) for _ in range(5)],
    'unidad': ['minutos', 'MB', 'GB', 'MB', 'GB']
})

# Generar datos para la tabla de hechos
num_registros = 30000
hechos_servicios = pd.DataFrame({
    'id_servicio': random.choices(servicios.id_servicio, k=num_registros),
    'id_cliente': random.choices(clientes.id_cliente, k=num_registros),
    'id_tiempo': random.choices(tiempo.id_tiempo, k=num_registros),
    'id_ubicacion': random.choices(ubicaciones.id_ubicacion, k=num_registros),
    'id_dispositivo': random.choices(dispositivos.id_dispositivo, k=num_registros),
    'id_facturacion': random.choices(facturacion.id_facturacion, k=num_registros),
    'id_promocion': random.choices(promociones.id_promocion, k=num_registros),
    'id_soporte': random.choices(soporte.id_soporte, k=num_registros),
    'id_consumo': random.choices(consumo.id_consumo, k=num_registros),
    'duracion_llamada': [round(random.uniform(1, 60), 2) for _ in range(num_registros)],
    'costo_servicio': [round(random.uniform(5, 100), 2) for _ in range(num_registros)],
    'tipo_transaccion': random.choices(['llamada', 'TV', 'internet'], k=num_registros),
    'ancho_banda': [round(random.uniform(1, 100), 2) for _ in range(num_registros)],
    'cantidad_datos_consumidos': [round(random.uniform(1, 1000), 2) for _ in range(num_registros)]
})

# Guardar en archivos CSV
clientes.to_csv('clientes.csv', index=False)
servicios.to_csv('servicios.csv', index=False)
tiempo.to_csv('tiempo.csv', index=False)
ubicaciones.to_csv('ubicaciones.csv', index=False)
dispositivos.to_csv('dispositivos.csv', index=False)
facturacion.to_csv('facturacion.csv', index=False)
promociones.to_csv('promociones.csv', index=False)
soporte.to_csv('soporte.csv', index=False)
consumo.to_csv('consumo.csv', index=False)
hechos_servicios.to_csv('hechos_servicios.csv', index=False)

# Mostrar ejemplos de las tablas generadas
print(clientes.head())
print(servicios.head())
print(hechos_servicios.head())
