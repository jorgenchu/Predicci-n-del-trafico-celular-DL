import json

notebook_path = 'prediction_model_call_in.ipynb'

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

eval_code = [
    "model.eval()\n",
    "predictions = []\n",
    "ground_truth = []\n",
    "\n",
    "print(\"Iniciando evaluación...\")\n",
    "with torch.no_grad():\n",
    "    for xc, xd, y in test_loader:\n",
    "        xc, xd, y = xc.to(DEVICE), xd.to(DEVICE), y.to(DEVICE)\n",
    "        output = model(xc, xd)\n",
    "        predictions.append(output.cpu().numpy())\n",
    "        ground_truth.append(y.cpu().numpy())\n",
    "\n",
    "predictions = np.concatenate(predictions, axis=0)\n",
    "ground_truth = np.concatenate(ground_truth, axis=0)\n",
    "\n",
    "# Rescalado Inverso (Denormalization)\n",
    "preds_rescaled = predictions * (mmn_max - mmn_min) + mmn_min\n",
    "gt_rescaled = ground_truth * (mmn_max - mmn_min) + mmn_min\n",
    "\n",
    "# --- MÉTRICAS ---\n",
    "mse = mean_squared_error(gt_rescaled.flatten(), preds_rescaled.flatten())\n",
    "rmse = np.sqrt(mse)\n",
    "mae = mean_absolute_error(gt_rescaled.flatten(), preds_rescaled.flatten())\n",
    "r2 = r2_score(gt_rescaled.flatten(), preds_rescaled.flatten())\n",
    "\n",
    "print(f\"Resultados de Evaluación:\")\n",
    "print(f\"RMSE: {rmse:.4f}\")\n",
    "print(f\"MAE:  {mae:.4f}\")\n",
    "print(f\"R2:   {r2:.4f}\")\n",
    "\n",
    "# 4. Serie Temporal para la Celda con más Tráfico\n",
    "total_traffic = np.sum(gt_rescaled, axis=(0, 1))\n",
    "y_max, x_max = np.unravel_index(np.argmax(total_traffic), total_traffic.shape)\n",
    "\n",
    "print(f\"Visualizando serie temporal para la celda con más tráfico: ({y_max}, {x_max})\")\n",
    "\n",
    "gt_series = gt_rescaled[:, 0, y_max, x_max] # Channel 0 (SMS In)\n",
    "pred_series = preds_rescaled[:, 0, y_max, x_max]\n",
    "\n",
    "plt.figure(figsize=(15, 5))\n",
    "plt.plot(gt_series, label='Ground Truth')\n",
    "plt.plot(pred_series, label='Prediction', alpha=0.7)\n",
    "plt.title(f'Serie Temporal de Tráfico SMS In - Celda ({y_max}, {x_max})')\n",
    "plt.xlabel('Horas (Test Set)')\n",
    "plt.ylabel('Volumen de Call')\n",
    "plt.legend()\n",
    "plt.show()\n",
    "\n"
]

# Find the last code cell which contains the visualization code we added
# It starts with "# --- VISUALIZACIONES ADICIONALES ---"
found_cell = False
for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        source = "".join(cell['source'])
        if "# --- VISUALIZACIONES ADICIONALES ---" in source:
            # Prepend the eval code
            cell['source'] = eval_code + cell['source']
            found_cell = True
            print("Inserted evaluation code before visualizations.")
            break

if not found_cell:
    print("Error: Could not find the visualization cell to prepend code to.")

with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print("Notebook updated successfully.")
