import json
import os

notebook_path = 'analysis.ipynb'

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# 1. Modify Weekly Viz Cell
# Search for cell containing "plt.tight_layout()" and "plt.show()"
found_weekly = False
for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        source = "".join(cell['source'])
        if "plt.tight_layout()" in source and "plt.show()" in source and "ax1.plot" in source:
            # Modify source lines
            new_source = []
            for line in cell['source']:
                if "plt.show()" in line:
                    new_source.append("plt.savefig('internet_sms_call_traffic.png')\n")
                    new_source.append(line)
                else:
                    new_source.append(line)
            cell['source'] = new_source
            found_weekly = True
            print("Modified Weekly Viz cell.")
            break

if not found_weekly:
    print("Warning: Weekly Viz cell not found.")

# 2. Modify Spatial 3D Cell
# Search for cell defining plot_3d_surface
found_spatial = False
for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        source = "".join(cell['source'])
        if "def plot_3d_surface" in source:
            new_source = []
            for line in cell['source']:
                # Update function signature
                if "def plot_3d_surface" in line:
                    new_source.append(line.replace("title, cmap='inferno')", "title, filename, cmap='inferno')"))
                # Update savefig
                elif "plt.show()" in line:
                    new_source.append("    plt.savefig(filename)\n")
                    new_source.append(line)
                # Update calls
                elif "plot_3d_surface(" in line and "def " not in line:
                    # We need to insert the filename argument.
                    # The calls are like: plot_3d_surface(data, title, cmap=...)
                    # We want: plot_3d_surface(data, title, filename, cmap=...)
                    # This is a bit tricky with string replacement if we don't parse it.
                    # But the calls are specific:
                    if "Distribución Espacial 3D - SMS" in line:
                        new_source.append(line.replace("'Distribución Espacial 3D - SMS',", "'Distribución Espacial 3D - SMS', 'spatial_sms.png',"))
                    elif "Distribución Espacial 3D - Internet" in line:
                        new_source.append(line.replace("'Distribución Espacial 3D - Internet',", "'Distribución Espacial 3D - Internet', 'spatial_internet.png',"))
                    elif "Distribución Espacial 3D - Llamadas" in line:
                        new_source.append(line.replace("'Distribución Espacial 3D - Llamadas',", "'Distribución Espacial 3D - Llamadas', 'spatial_calls.png',"))
                    else:
                        new_source.append(line)
                else:
                    new_source.append(line)
            cell['source'] = new_source
            found_spatial = True
            print("Modified Spatial 3D cell.")
            break

if not found_spatial:
    print("Warning: Spatial 3D cell not found.")

# 3. Add Report Generation Cell
new_cell = {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "import datetime\n",
    "\n",
    "report_content = f\"\"\"# Reporte de Análisis de Tráfico\\n",
    "Fecha de generación: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\\n",
    "\\n",
    "## Tráfico Semanal\\n",
    "![Tráfico de Internet, SMS y Llamadas](internet_sms_call_traffic.png)\\n",
    "\\n",
    "## Distribución Espacial\\n",
    "### SMS\\n",
    "![Distribución Espacial SMS](spatial_sms.png)\\n",
    "\\n",
    "### Internet\\n",
    "![Distribución Espacial Internet](spatial_internet.png)\\n",
    "\\n",
    "### Llamadas\\n",
    "![Distribución Espacial Llamadas](spatial_calls.png)\\n",
    "\"\"\"\n",
    "\n",
    "with open('analysis_report.md', 'w', encoding='utf-8') as f:\n",
    "    f.write(report_content)\n",
    "\n",
    "print(\"Reporte generado: analysis_report.md\")"
   ]
}

# Check if cell already exists to avoid duplicates
last_cell_source = "".join(nb['cells'][-1]['source'])
if "analysis_report.md" not in last_cell_source:
    nb['cells'].append(new_cell)
    print("Added Report Generation cell.")
else:
    print("Report Generation cell already exists.")

with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print("Notebook updated successfully.")
