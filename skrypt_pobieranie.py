import os
import urllib.request
import zipfile
import time
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

OUTPUT_DIR = "dane_imgw"
os.makedirs(OUTPUT_DIR, exist_ok=True)

for rok_val in range(2001, 2024):
    rok = f"{rok_val:04d}"
    for miesiac_val in range(1, 13):
        mm = f"{miesiac_val:02d}"
        zip_filename = f"{rok}_{mm}_k.zip"
        zip_url = f"https://danepubliczne.imgw.pl/data/dane_pomiarowo_obserwacyjne/dane_meteorologiczne/dobowe/klimat/{rok}/{zip_filename}"

        print(f"Pobieram {zip_filename} ...")

        try:
            urllib.request.urlretrieve(zip_url, zip_filename)
        except Exception as e:
            print(f"Brak pliku dla {rok}-{mm}: {e}")
            continue

        if not os.path.exists(zip_filename) or os.path.getsize(zip_filename) == 0:
            print(f"Plik dla {rok}-{mm} nie istnieje lub jest pusty")
            continue

        try:
            with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
                zip_ref.extractall(OUTPUT_DIR)
        except zipfile.BadZipFile:
            print(f"Plik {zip_filename} jest uszkodzony")
            os.remove(zip_filename)
            continue

        os.remove(zip_filename)

        unwanted_csv = f"klimat_d_t_{rok}_{mm}.csv"
        unwanted_path = os.path.join(OUTPUT_DIR, unwanted_csv)
        if os.path.exists(unwanted_path):
            os.remove(unwanted_path)

        time.sleep(1)
