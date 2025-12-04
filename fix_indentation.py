import json

notebook_path = 'prediction_model_call_out.ipynb'

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Iterate through cells to find the one with the error
for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        source = cell['source']
        # Check if this is the target cell by looking for specific lines
        # We look for the line "    data_tensor = np.zeros..."
        
        new_source = []
        modified = False
        for line in source:
            if "    data_tensor = np.zeros" in line:
                new_source.append(line.lstrip()) # Remove leading whitespace
                modified = True
                print("Fixed indentation for data_tensor")
            elif "    df_pivot = df_agg.pivot_table" in line:
                new_source.append(line.lstrip()) # Remove leading whitespace
                modified = True
                print("Fixed indentation for df_pivot")
            else:
                new_source.append(line)
        
        if modified:
            cell['source'] = new_source
            print("Cell modified.")

with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print("Notebook indentation fixed.")
