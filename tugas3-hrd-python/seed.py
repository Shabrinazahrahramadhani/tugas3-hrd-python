from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["hrd_perusahaan"]
koleksi = db["karyawans"]

data_dummy = [
    {"nama": "James Carter",    "divisi": "IT",        "gaji": 9500000,  "status": "Tetap",   "tahun_masuk": 2018},
    {"nama": "Emily Watson",    "divisi": "Finance",   "gaji": 8200000,  "status": "Tetap",   "tahun_masuk": 2019},
    {"nama": "Sarah Mitchell",  "divisi": "HR",        "gaji": 6800000,  "status": "Tetap",   "tahun_masuk": 2020},
    {"nama": "David Reynolds",  "divisi": "IT",        "gaji": 11000000, "status": "Tetap",   "tahun_masuk": 2017},
    {"nama": "Laura Bennett",   "divisi": "Marketing", "gaji": 5500000,  "status": "Kontrak", "tahun_masuk": 2022},
    {"nama": "Michael Foster",  "divisi": "Finance",   "gaji": 7500000,  "status": "Tetap",   "tahun_masuk": 2021},
    {"nama": "Rachel Greene",   "divisi": "IT",        "gaji": 6200000,  "status": "Kontrak", "tahun_masuk": 2023},
    {"nama": "Thomas Harper",   "divisi": "Marketing", "gaji": 8800000,  "status": "Tetap",   "tahun_masuk": 2016},
    {"nama": "Amanda Collins",  "divisi": "HR",        "gaji": 5900000,  "status": "Kontrak", "tahun_masuk": 2022},
    {"nama": "Robert Sullivan", "divisi": "Finance",   "gaji": 9100000,  "status": "Tetap",   "tahun_masuk": 2018},
    {"nama": "Natalie Brooks",  "divisi": "IT",        "gaji": 7800000,  "status": "Tetap",   "tahun_masuk": 2020},
    {"nama": "Kevin Thornton",  "divisi": "Marketing", "gaji": 6400000,  "status": "Kontrak", "tahun_masuk": 2023},
]

koleksi.delete_many({})
print("🗑️  Data lama dihapus")

koleksi.insert_many(data_dummy)
print(f"✅ {len(data_dummy)} data karyawan berhasil dimasukkan")

client.close()
print("🔌 Koneksi ditutup")
