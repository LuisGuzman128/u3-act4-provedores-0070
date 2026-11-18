import pandas as pd
import matplotlib.pyplot as plt

## Número de Lista 26
# 1. Crear diccionario con datos de proveedores
proveedores_empresa = {
    'id_proveedor': [601, 602, 603, 604, 605, 606],
    'nombre_empresa': ['Distribuidora Sur', 'Aceites MX', 'Lala Directo', 'Bimbo Directo', 'Granjas Unidas', 'Papelera Central'],
    'contacto': ['Juan Perez', 'Maria Lopez', 'Carlos Ruiz', 'Ana Garcia', 'Luis Torres', 'Sofia Diaz'],
    'telefono': ['551111', '552222', '553333', '554444', '555555', '556666'],
    'correo': ['juan@dist.com', 'maria@aceites.com', 'carlos@lala.com', 'ana@bimbo.com', 'luis@granjas.com', 'sofia@papel.com'],
    'categoria_suministro': ['Abarrotes', 'Aceites', 'Lacteos', 'Panaderia', 'Refrigerados', 'Papeleria'],
    'dias_credito': [15, 30, 15, 7, 15, 30],
    'calificacion_servicio': [9, 8, 10, 9, 7, 8],
    'compras_ultimo_mes': [15000, 8000, 12000, 20000, 9000, 3000],
    'estado': ['Activo', 'Activo', 'Activo', 'Activo', 'Suspendido', 'Activo'],
    'ciudad': ['CDMX', 'Guadalajara', 'Monterrey', 'CDMX', 'Puebla', 'CDMX']
}

print("Analisis exploratorio de datos EDA")
print("Exploratory data analysis por Número de Lista 26 Axel Guzman 0070")
print("5. crear el diccionario con 11 listas y 6 elementos")

# 2. Convertir diccionario en DataFrame
df = pd.DataFrame(proveedores_empresa)
print("Tabla original de proveedores")
print(df)

# 3. Exportar los datos a CSV
df.to_csv(
    'proveedores_empresa_26.csv',
    index=False,
    encoding='utf-8-sig'
)

print("\n✅ Archivo CSV creado correctamente")
print("leer los datos desde el archivo CSV")
print("proveedores_empresa_26.csv")

# 4. Leer el archivo CSV
df = pd.read_csv('proveedores_empresa_26.csv')
print("\n--- DATOS LEÍDOS DESDE CSV ---")
print(df)
print("+-+-+- 9. Análisis Exploratorio de Datos (EDA) +-+-+-")

# 5. Primeros y últimos registros
print("+-+-+-\n1. PRIMEROS REGISTROS (Head):+-+-+-")
print(df.head(4)) # Muestra los primeros 4
print("+-+-+-\n2. ÚLTIMOS REGISTROS (Tail):+-+-+-+")
print(df.tail(2)) # Muestra los últimos 2

# 6. Dimensiones y estructura
print(" +-+-+-6 Dimensiones y estructura+-+-+-")
print(df) # mostrar tabla o matriz
print("\n3. DIMENSIONES (Filas, Columnas):", df.shape)
print("\n4. NOMBRES DE COLUMNAS:\n", df.columns)
print("\n5. TIPOS DE DATOS:\n", df.dtypes)
print("\n6. INFORMACIÓN GENERAL:")
df.info()
 # 7. Estadísticas y limpieza
print("+-+-+-\n7. ESTADÍSTICAS DESCRIPTIVAS:+-+-+-")
print(df.describe())
print("\n8. VALORES FALTANTES (Nulls):")
print(df.isnull().sum())
print("\n9. REGISTROS DUPLICADOS:")
print(df.duplicated().sum())
print("\n10. VALORES ÚNICOS POR COLUMNA:")
print(df.nunique())
print("Ciudades únicas:", df['ciudad'].unique())

# 8. Análisis específico
print(df)
print("-----------------------------------------------------")
print("\n11. PROVEEDORES POR CIUDAD:")
print(df['ciudad'].value_counts())

print("\n12. PROMEDIO DE COMPRAS ÚLTIMO MES: $", df['compras_ultimo_mes'].mean())
print("13. COMPRA MÁXIMA ÚLTIMO MES: $", df['compras_ultimo_mes'].max())
print("14. COMPRA MÍNIMA ÚLTIMO MES: $", df['compras_ultimo_mes'].min())

# 9. Ordenamiento, filtrado y agrupación
print("9 Ordenamiento, filtrado y agrupación")
print("\n15. PROVEEDORES ORDENADOS POR COMPRAS DEL MES (Mayor a menor):")
print(df.sort_values(by='compras_ultimo_mes', ascending=False))

print("\n16. PROVEEDORES CON COMPRAS MAYORES A $10,000:")
filtro = df[df['compras_ultimo_mes'] > 10000]
print(filtro)
