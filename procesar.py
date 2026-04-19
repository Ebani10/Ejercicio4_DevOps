import csv
import os

def analizar_viajes():
    estados = []
    costos_totales = []

    if not os.path.exists('data.txt'):
        print("Error: data.txt no encontrado")
        return

    try:
        with open('data.txt', mode='r', encoding='utf-8') as f:
            # .strip() elimina espacios o saltos de línea accidentales
            reader = csv.DictReader(f)
            
            for row in reader:
                # Verificación de seguridad: saltar filas vacías
                if not row.get('Estado'):
                    continue
                
                try:
                    # Limpiamos posibles espacios en los valores
                    alojamiento = int(row['Costo_Alojamiento'].strip())
                    transporte = int(row['Costo_Transporte'].strip())
                    dias = int(row['Dias_Promedio'].strip())
                    
                    costo = (alojamiento + transporte) * dias
                    estados.append(row['Estado'].strip())
                    costos_totales.append(costo)
                except (ValueError, TypeError, KeyError) as e:
                    print(f"Saltando fila con error en datos: {row} - Error: {e}")
                    continue

        if not estados:
            print("No se procesaron datos válidos.")
            return

        # Generar el reporte
        with open('resultado.txt', 'w', encoding='utf-8') as f:
            f.write("--- REPORTE DE COSTOS DE VIAJE (MÉXICO) ---\n")
            f.write(f"Total de estados analizados: {len(estados)}\n")
            f.write(f"Estado más caro: {estados[costos_totales.index(max(costos_totales))]} (${max(costos_totales)})\n")
            f.write(f"Estado más barato: {estados[costos_totales.index(min(costos_totales))]} (${min(costos_totales)})\n")
            f.write(f"Promedio de costo general: ${sum(costos_totales) / len(costos_totales):.2f}\n")
            
        print("Reporte resultado.txt generado con éxito.")

    except Exception as e:
        print(f"Error crítico: {e}")
        # Forzamos la salida con error para que CodeBuild se detenga si algo sale mal
        exit(1) 

if __name__ == "__main__":
    analizar_viajes()