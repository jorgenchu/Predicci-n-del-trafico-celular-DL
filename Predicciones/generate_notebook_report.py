import nbformat as nbf
import os
import base64
import sys

def generate_report(notebook_path):
    if not os.path.exists(notebook_path):
        print(f"Error: {notebook_path} not found.")
        return

    notebook_name = os.path.splitext(os.path.basename(notebook_path))[0]
    report_dir = "reports"
    plots_dir = os.path.join(report_dir, "plots", notebook_name)
    os.makedirs(plots_dir, exist_ok=True)

    print(f"Reading {notebook_path}...")
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = nbf.read(f, as_version=4)

    report_content = [f"# Reporte de Visualizaciones: {notebook_name}\n"]
    report_content.append(f"Este documento contiene las figuras extraídas del notebook `{notebook_path}` con sus correspondientes explicaciones.\n")

    img_count = 0
    last_text = ""
    
    for i, cell in enumerate(nb.cells):
        if cell.cell_type == 'code':
            source = cell.source
            outputs = cell.get('outputs', [])
            
            for out in outputs:
                if out.output_type == 'stream' and out.name == 'stdout':
                    last_text += out.text
                
                if 'data' in out and 'image/png' in out['data']:
                    img_count += 1
                    img_data = out['data']['image/png']
                    img_filename = f"plot_{img_count}.png"
                    img_path = os.path.join(plots_dir, img_filename)
                    
                    with open(img_path, "wb") as fh:
                        fh.write(base64.b64decode(img_data))
                    
                    rel_img_path = f"plots/{notebook_name}/{img_filename}"
                    
                    # Heuristics for better identification
                    context = (source + "\n" + last_text).lower()
                    
                    if "scatter" in context and "ideal" in context:
                        description = "### Scatter Plot: Real vs Predicción"
                        explanation = "Este gráfico de dispersión enfrenta cada valor real contra su correspondiente predicción. La línea roja discontinua representa la predicción perfecta (y=x). La cercanía de los puntos a esta línea indica la precisión global del modelo; una nube de puntos estrecha sugiere un error bajo y alta correlación."
                        # Clear specific context bits to avoid misfire on next plot in same cell
                        last_text = "" 
                    elif "nodos aleatorios" in context or "random node" in context:
                        description = "### Serie Temporal: Nodos Aleatorios"
                        explanation = "Aquí se presentan comparaciones para nodos seleccionados al azar. Esto permite verificar la consistencia del modelo en diferentes partes de la red, no solo en los puntos críticos, asegurando que no haya sobreajuste a los nodos principales."
                        last_text = ""
                    elif "mayor tráfico" in context or "max_node_idx" in context:
                        description = "### Serie Temporal: Nodo de Mayor Tráfico"
                        explanation = "Esta gráfica muestra la comparación entre los datos reales (Ground Truth) y las predicciones del modelo para el nodo que registra el mayor volumen de tráfico promedio. Es una prueba crítica de la capacidad del modelo para capturar picos de demanda."
                        last_text = ""
                    elif "loss" in context:
                        description = "### Curvatura de Aprendizaje (Loss)"
                        explanation = "Muestra la evolución del error (MSE) durante el entrenamiento. Una curva descendente que se estabiliza indica que el modelo ha convergido correctamente."
                        last_text = ""
                    else:
                        description = f"### Visualización {img_count}"
                        explanation = "Visualización de los resultados del modelo."

                    report_content.append(description + "\n")
                    report_content.append(f"![{description.strip()}]({rel_img_path})\n")
                    report_content.append(f"{explanation}\n")
                    report_content.append("\n---\n")
            
            # Reset text context for each cell if no image found to avoid bleed-through
            last_text = ""

    report_file = f"{notebook_name}_Reporte.md"
    report_path = os.path.join(report_dir, report_file)
    with open(report_path, "w", encoding='utf-8') as f:
        f.write("\n".join(report_content))

    print(f"Report generated successfully: {report_path}")

if __name__ == "__main__":
    notebook = sys.argv[1] if len(sys.argv) > 1 else r"c:\Users\jorge\Desktop\TFM DATA\Predicciones\GNN_Internet_Dense.ipynb"
    generate_report(notebook)
