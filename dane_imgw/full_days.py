#2.1szukanie_pełnych_historii
import numpy as np
import matplotlib.pyplot as plt
from datetime import date

filename = "full.csv"
station_ids = np.genfromtxt(filename, dtype=str, delimiter=None, usecols=0, encoding="cp1250", filling_values="")

ID, counts = np.unique(station_ids, return_counts=True)

full_days = 8400
mask_full_history = counts == full_days
stacje_full = ID[mask_full_history]
stacje_nfull = ID[~mask_full_history]

print(stacje_full)
print(stacje_nfull)

#2.3 wykres średniej dziennej temperatury dla stacji z pełną historią
dni = []
średnie_temperatury = []
wybrana_stacja = stacje_full[10]
print(f"Analiza stacji: {wybrana_stacja}")

data_subset = np.genfromtxt(filename, dtype=float, delimiter=None, usecols=(0, 2, 3, 4, 7), encoding="cp1250")

maska_stacji = data_subset[:, 0] ==int(wybrana_stacja)
dane_stacji = data_subset[maska_stacji]

start = date(2001, 1, 1)
for i in range(len(dane_stacji[:,0])):
    current = date(int(dane_stacji[i,1]), int(dane_stacji[i,2]), int(dane_stacji[i,3]))
    dzień = (current - start).days
    dni.append(dzień)

    średnia_temperatura = dane_stacji[i,4]
    średnie_temperatury.append(średnia_temperatura)

plt.figure(figsize=(12, 6))
plt.plot(dni, średnie_temperatury)
plt.xlabel('liczba dni od 01.01.2001')
plt.ylabel('Średnia temperatura')
plt.grid(True)
plt.show()

#2.5a różnica dziennych średnich temperatur dwóch stacji
import numpy as np
import matplotlib.pyplot as plt

id1 = 249180010
def s1(t):
  maska = data_subset[:, 0] == id1
  dane_wybranej_stacji = data_subset[maska]
  s_temp1 = dane_wybranej_stacji[t, 4]
  return s_temp1

id2 = 249180160
def s2(t):
  maska = data_subset[:, 0] == id2
  dane_wybranej_stacji = data_subset[maska]
  s_temp2 = dane_wybranej_stacji[t, 4]
  return s_temp2

data_subset = np.genfromtxt(filename, dtype=float, delimiter=None, usecols=(0, 2, 3, 4, 7), encoding="cp1250")

s_roznica_temp = []

for t in range(8400):
  s_roznica_temp.append(s1(t) - s2(t))


s_roznica_temp = np.array(s_roznica_temp)
top_idx = np.argpartition(s_roznica_temp, -5)[-5:]
top_idx = top_idx[np.argsort(s_roznica_temp[top_idx])[::-1]]

print("Największe różnice wyniosły:")
for i in top_idx:
    print(f"{s_roznica_temp[i]:.2f} stopni – w dniu {int(data_subset[i, 1])} - {int(data_subset[i, 2])} - {int(data_subset[i, 3])}")

plt.figure(figsize=(12, 6))
plt.plot(s_roznica_temp)
plt.title(f'Średnie różnice temperatur stacji {int(id1)} i {int(id2)}')
plt.xlabel('Dzień')
plt.ylabel('Różnica')
plt.grid(True)
plt.show()