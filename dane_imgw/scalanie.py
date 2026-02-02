import numpy as np

full_data = np.empty((0, 18), dtype=object)

for year in range(2001, 2024):
    for month in range(1, 13):
        filename = f"k_d_{month:02d}_{year}.csv"
        data = np.loadtxt(filename, delimiter=',', dtype=str, encoding="cp1250", quotechar='"')
        full_data = np.vstack((full_data, data))

cols_to_delete = [17, 16, 15, 14, 13, 12, 11, 10, 8, 6]  # od największego do najmniejszego
full_data = np.delete(full_data, cols_to_delete, axis=1)

full_data = full_data.astype(str)
full_data = np.char.strip(full_data, '"')

np.savetxt("full.csv", full_data, fmt="%s", encoding="cp1250")