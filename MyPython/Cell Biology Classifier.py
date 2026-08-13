def classify_cell(has_nucleus, has_cell_wall, cell_size_micrometers):
    if not has_nucleus:
        return "Prokaryotic Cell (e.g., Bacteria) - No defined nucleus."
    else:
        if has_cell_wall:
            if cell_size_micrometers > 10:
                return "Eukaryotic Plant Cell - Has a nucleus and a rigid cell wall."
            else:
                return "Eukaryotic Fungal/Algal Cell - Has a nucleus and cell wall, but smaller."
        else:
            return "Eukaryotic Animal Cell - Has a nucleus, but NO cell wall."

print("Cell Biology Data Classifier\n")

print("Testing Sample 1:")
result_1 = classify_cell(has_nucleus=True, has_cell_wall=False, cell_size_micrometers=30)
print(f"Result: {result_1}\n")

print("Testing Sample 2:")
result_2 = classify_cell(has_nucleus=True, has_cell_wall=True, cell_size_micrometers=50)
print(f"Result: {result_2}\n")

print("Testing Sample 3:")
result_3 = classify_cell(has_nucleus=False, has_cell_wall=True, cell_size_micrometers=2)
print(f"Result: {result_3}\n")
