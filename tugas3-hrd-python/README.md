# Tugas 3 – Pencarian Data Karyawan & Agregasi MongoDB (Python Version)

## Stack
- **Python** + **FastAPI** (pengganti Node.js + Express)
- **PyMongo** (pengganti Mongoose)
- **MongoDB**

## Perbandingan dengan Versi Node.js

| Node.js          | Python          |
|------------------|-----------------|
| Express          | FastAPI         |
| Mongoose         | PyMongo         |
| app.js           | main.py         |
| seed.js          | seed.py         |
| package.json     | requirements.txt|
| npm install      | pip install     |
| node app.js      | uvicorn main:app|

## Struktur Proyek
```
tugas3-hrd-python/
├── main.py            ← Entry point FastAPI + semua endpoint
├── seed.py            ← Script insert data dummy
└── requirements.txt   ← Daftar library Python
```

## Instalasi & Menjalankan

```bash
pip install -r requirements.txt
python seed.py                        # Insert data dummy
uvicorn main:app --reload             # Jalankan server port 8000
```

## Endpoints

| Method | URL                                  | Deskripsi                        |
|--------|--------------------------------------|----------------------------------|
| GET    | /api/karyawan                        | Semua data karyawan              |
| GET    | /api/karyawan/tetap-gaji-tinggi      | Filter $and + $gt                |
| GET    | /api/karyawan/divisi-it-finance      | Filter $in                       |
| GET    | /api/karyawan/laporan-divisi         | Aggregation Pipeline             |
| GET    | /docs                                | Swagger UI (otomatis dari FastAPI)|
