from fastapi import FastAPI
from pymongo import MongoClient
from bson import ObjectId
import json

app = FastAPI(title="Tugas 3 - Sistem HRD Karyawan (Python)")

# Koneksi MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["hrd_perusahaan"]
koleksi = db["karyawans"]

# Helper untuk konversi ObjectId ke string
def parse(data):
    if isinstance(data, list):
        for item in data:
            if "_id" in item:
                item["_id"] = str(item["_id"])
        return data
    if "_id" in data:
        data["_id"] = str(data["_id"])
    return data

# ============================================================
# ROOT - Dokumentasi endpoint
# ============================================================
@app.get("/")
def root():
    return {
        "judul": "Tugas 3 - Sistem HRD Karyawan (Python Version)",
        "endpoints": [
            {"method": "GET", "url": "/api/karyawan",             "deskripsi": "Semua data karyawan"},
            {"method": "GET", "url": "/api/karyawan/tetap-gaji-tinggi", "deskripsi": "Karyawan Tetap gaji > 7jt ($and, $gt)"},
            {"method": "GET", "url": "/api/karyawan/divisi-it-finance", "deskripsi": "Divisi IT atau Finance ($in)"},
            {"method": "GET", "url": "/api/karyawan/laporan-divisi",    "deskripsi": "Agregasi per divisi ($match, $group, $sort)"},
        ]
    }

# ============================================================
# ENDPOINT 1: Semua karyawan
# GET /api/karyawan
# ============================================================
@app.get("/api/karyawan")
def get_semua_karyawan():
    data = list(koleksi.find().sort("nama", 1))
    return {
        "status": "success",
        "total": len(data),
        "data": parse(data)
    }

# ============================================================
# ENDPOINT 2: Karyawan Tetap DAN gaji > 7.000.000
# GET /api/karyawan/tetap-gaji-tinggi
# Query Operator: $and, $gt
# ============================================================
@app.get("/api/karyawan/tetap-gaji-tinggi")
def get_tetap_gaji_tinggi():
    query = {
        "$and": [
            {"status": "Tetap"},
            {"gaji": {"$gt": 7000000}}
        ]
    }
    data = list(koleksi.find(query).sort("gaji", -1))
    return {
        "status": "success",
        "deskripsi": "Karyawan berstatus Tetap dengan gaji di atas Rp 7.000.000",
        "operator_digunakan": ["$and", "$gt"],
        "total": len(data),
        "data": parse(data)
    }

# ============================================================
# ENDPOINT 3: Karyawan divisi IT atau Finance
# GET /api/karyawan/divisi-it-finance
# Query Operator: $in
# ============================================================
@app.get("/api/karyawan/divisi-it-finance")
def get_divisi_it_finance():
    query = {
        "divisi": {"$in": ["IT", "Finance"]}
    }
    data = list(koleksi.find(query).sort([("divisi", 1), ("nama", 1)]))
    return {
        "status": "success",
        "deskripsi": "Karyawan yang berada di divisi IT atau Finance",
        "operator_digunakan": ["$in"],
        "total": len(data),
        "data": parse(data)
    }

# ============================================================
# ENDPOINT 4: Laporan agregasi per divisi
# GET /api/karyawan/laporan-divisi
# Aggregation Pipeline: $match -> $group -> $sort
# ============================================================
@app.get("/api/karyawan/laporan-divisi")
def get_laporan_divisi():
    pipeline = [
        # Tahap 1: $match - hanya karyawan Tetap
        {"$match": {"status": "Tetap"}},

        # Tahap 2: $group - kelompokkan per divisi
        {"$group": {
            "_id": "$divisi",
            "jumlah_karyawan": {"$sum": 1},
            "rata_rata_gaji":  {"$avg": "$gaji"},
            "total_gaji":      {"$sum": "$gaji"},
            "gaji_tertinggi":  {"$max": "$gaji"},
            "gaji_terendah":   {"$min": "$gaji"},
        }},

        # Tahap 3 (BONUS): $sort - rata-rata gaji tertinggi
        {"$sort": {"rata_rata_gaji": -1}},

        # $project - rapikan output
        {"$project": {
            "_id": 0,
            "divisi":          "$_id",
            "jumlah_karyawan": 1,
            "rata_rata_gaji":  {"$round": ["$rata_rata_gaji", 0]},
            "total_gaji":      1,
            "gaji_tertinggi":  1,
            "gaji_terendah":   1,
        }}
    ]

    hasil = list(koleksi.aggregate(pipeline))
    return {
        "status": "success",
        "deskripsi": "Laporan ringkasan gaji per divisi (hanya karyawan Tetap)",
        "pipeline": ["$match", "$group", "$sort (bonus)", "$project"],
        "total_divisi": len(hasil),
        "data": hasil
    }
