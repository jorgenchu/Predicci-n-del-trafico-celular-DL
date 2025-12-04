import json

notebook_path = 'prediction_model_call_in.ipynb'

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Code to append
viz_code = [
    "\n",
    "# --- VISUALIZACIONES ADICIONALES ---\n",
    "\n",
    "# 1. Scatter Plot: Predicción vs Realidad\n",
    "plt.figure(figsize=(8, 8))\n",
    "plt.scatter(gt_rescaled.flatten(), preds_rescaled.flatten(), alpha=0.1, s=1)\n",
    "plt.plot([mmn_min, mmn_max], [mmn_min, mmn_max], 'r--', lw=2) # Diagonal\n",
    "plt.xlabel('Valor Real (Ground Truth)')\n",
    "plt.ylabel('Predicción')\n",
    "plt.title('Scatter Plot: Real vs Predicción')\n",
    "plt.grid(True)\n",
    "plt.show()\n",
    "\n",
    "# 2. Distribución de Errores\n",
    "residuals = preds_rescaled.flatten() - gt_rescaled.flatten()\n",
    "plt.figure(figsize=(10, 5))\n",
    "plt.hist(residuals, bins=100, color='blue', alpha=0.7)\n",
    "plt.xlabel('Error (Predicción - Real)')\n",
    "plt.ylabel('Frecuencia')\n",
    "plt.title('Distribución de Errores')\n",
    "plt.grid(True)\n",
    "plt.show()\n",
    "\n",
    "# 3. Mapa de Calor del Error (MAE Espacial)\n",
    "# Calcular MAE por celda (promedio en el tiempo y canales)\n",
    "mae_spatial = np.mean(np.abs(preds_rescaled - gt_rescaled), axis=(0, 1)) # [H, W]\n",
    "\n",
    "plt.figure(figsize=(10, 8))\n",
    "plt.imshow(mae_spatial, cmap='hot', interpolation='nearest')\n",
    "plt.colorbar(label='MAE Promedio')\n",
    "plt.title('Mapa de Calor del Error Absoluto Medio (MAE)')\n",
    "plt.xlabel('Grid X')\n",
    "plt.ylabel('Grid Y')\n",
    "plt.show()\n"
]

# Find the last code cell (Evaluation cell)
# We assume the last code cell is the one doing the evaluation and plotting the time series.
# We will append the new code to the end of its source.

found_cell = False
for i in range(len(nb['cells']) - 1, -1, -1):
    cell = nb['cells'][i]
    if cell['cell_type'] == 'code':
        # Check if it looks like the evaluation cell
        source = "".join(cell['source'])
        if "plt.show()" in source and "model.eval()" in source:
            cell['source'].extend(viz_code)
            found_cell = True
            print("Appended visualization code to the evaluation cell.")
            break

if not found_cell:
    print("Warning: Could not find the specific evaluation cell. Appending a new cell instead.")
    new_cell = {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": viz_code
    }
    nb['cells'].append(new_cell)

with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print("Notebook updated successfully.")
