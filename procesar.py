import csv

def analizar_viajes():
    estados = []
    costos_totales = []

    try:
        with open('data.txt', mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Cálculo: (Alojamiento + Transporte) * Dias
                costo = (int(row['Costo_Alojamiento']) + int(row['Costo_Transporte'])) * int(row['Dias_Promedio'])
                estados.append(row['Estado'])
                costos_totales.append(costo)

        # Generar el reporte
        with open('resultado.txt', 'w', encoding='utf-8') as f:
            f.write("--- REPORTE DE COSTOS DE VIAJE (MÉXICO) ---\n")
            f.write(f"Total de estados analizados: {len(estados)}\n")
            f.write(f"Estado más caro: {estados[costos_totales.index(max(costos_totales))]} (${max(costos_totales)})\n")
            f.write(f"Estado más barato: {estados[costos_totales.index(min(costos_totales))]} (${min(costos_totales)})\n")
            f.write(f"Promedio de costo general: ${sum(costos_totales) / len(costos_totales):.2f}\n")
            f.write("\nActualizado automáticamente por el Pipeline de AWS.")
            
        print("Reporte generado con éxito.")
    except Exception as e:
        print(f"Error procesando datos: {e}")

if __name__ == "__main__":
    analizar_viajes()