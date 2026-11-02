import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# 1. Configuración
np.random.seed(42)

Path("data").mkdir(exist_ok=True)
Path("outputs").mkdir(exist_ok=True)

# 2. Generar datos sintéticos de ventas
fechas = pd.date_range(
    start="2026-01-01",
    periods=180,
    freq="D"
)

categorias = ["Tecnología", "Hogar", "Deportes", "Accesorios"]

df = pd.DataFrame({
    "fecha": fechas,
    "categoria": np.random.choice(categorias, 180),
    "unidades": np.random.randint(1, 15, 180),
    "precio_unitario": np.random.randint(5000, 100000, 180)
})

# 3. Transformación de datos
df["ingresos"] = df["unidades"] * df["precio_unitario"]
df["mes"] = df["fecha"].dt.to_period("M").astype(str)

# 4. Análisis de datos
print("\n--- RESUMEN GENERAL ---")
print(f"Ventas totales: ${df['ingresos'].sum():,.0f}")
print(f"Unidades vendidas: {df['unidades'].sum():,}")
print(f"Promedio por venta: ${df['ingresos'].mean():,.0f}")

print("\n--- INGRESOS POR CATEGORÍA ---")
resumen = df.groupby("categoria")["ingresos"].sum()
print(resumen.sort_values(ascending=False))

# 5. Exportar datos
df.to_csv("data/ventas_sinteticas.csv", index=False)

# 6. Visualizar ingresos mensuales
ventas_mensuales = df.groupby("mes")["ingresos"].sum()

ventas_mensuales.plot(kind="bar", figsize=(10, 5))
plt.title("Ingresos mensuales - Datos sintéticos")
plt.xlabel("Mes")
plt.ylabel("Ingresos ($)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("outputs/ventas_mensuales.png")
plt.close()

print("\nAnálisis completado correctamente.")
