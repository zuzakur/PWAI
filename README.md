# Analiza historycznych danych pogodowych (IMGW)

Projekt zrealizowany w ramach przedmiotu **Podstawowy warsztat AI**. Celem projektu jest pobranie, konsolidacja oraz analiza historycznych danych temperaturowych udostępnianych przez IMGW, a następnie wykonanie prostych statystyk oraz wykrywanie anomalii pogodowych.

---

## Wymagania systemowe

* **Python**: 3.14.0 (projekt był testowany na tej wersji)
* System operacyjny: macOS / Linux / Windows

### Wykorzystywane biblioteki

Wszystkie biblioteki są standardowe lub powszechnie dostępne:

```python
import numpy as np
import matplotlib.pyplot as plt
import os
import time
import urllib.request
import zipfile
import ssl
from datetime import date
```
---

## Kolejność uruchamiania kodu

Projekt należy uruchamiać **w poniższej kolejności**.

### 1. Pobieranie danych

Plik `skrypt_pobieranie.py` automatycznie pobiera archiwa ZIP z danymi IMGW dla lat 2001–2023 i je rozpakowuje.

Skrypt zawiera opóźnienia (`time.sleep(1)`) pomiędzy kolejnymi żądaniami, aby nie przeciążać serwerów IMGW.

---

### 2. Scalanie danych

Plik `scalanie.py`:

* wczytuje wszystkie miesięczne pliki CSV,
* usuwa zbędne kolumny,
* scala dane w jedną tablicę,
* zapisuje wynik do `full.csv`.

Po wykonaniu tego kroku plik `full.csv` powinien mieć rozmiar ok. 35–75 MB.

---

### 3. Analiza danych i zadania projektowe

Plik `full_days.py` realizuje:

* proste charakterystyki statystyczne danych,
* wizualizacje wymagane w sekcji 2 projektu,
* wyszukiwanie ekstremalnych temperatur,
* wykrywanie anomalii pogodowych.

Wyniki wypisywane są w konsoli oraz prezentowane w postaci wykresów.

Link do projektu Google Colab ze skryptami: https://colab.research.google.com/drive/1h8LCozwp0xlxlcEGQzsbQHjxz3RQxlog?usp=sharing
