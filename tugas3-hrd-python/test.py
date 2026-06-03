import requests

BASE_URL = "http://localhost:8000"

def rupiah(n):
    return f"Rp {int(n):,}".replace(",", ".")

def garis():
    print("-" * 55)

# ── SEMUA KARYAWAN ─────────────────────────────────────────
print("\nSEMUA DATA KARYAWAN")
garis()
res = requests.get(f"{BASE_URL}/api/karyawan").json()
print(f"{'Nama':<20} {'Divisi':<12} {'Gaji':<15} {'Status'}")
garis()
for k in res["data"]:
    print(f"{k['nama']:<20} {k['divisi']:<12} {rupiah(k['gaji']):<15} {k['status']}")
print(f"\nTotal: {res['total']} karyawan")

# ── QUERY 1 ────────────────────────────────────────────────
print("\nQUERY 1 - Karyawan Tetap & Gaji > 7.000.000 ($and, $gt)")
garis()
res1 = requests.get(f"{BASE_URL}/api/karyawan/tetap-gaji-tinggi").json()
print(f"{'Nama':<20} {'Divisi':<12} {'Gaji'}")
garis()
for k in res1["data"]:
    print(f"{k['nama']:<20} {k['divisi']:<12} {rupiah(k['gaji'])}")
print(f"\nDitemukan: {res1['total']} karyawan")

# ── QUERY 2 ────────────────────────────────────────────────
print("\nQUERY 2 - Divisi IT atau Finance ($in)")
garis()
res2 = requests.get(f"{BASE_URL}/api/karyawan/divisi-it-finance").json()
print(f"{'Nama':<20} {'Divisi':<12} {'Gaji':<15} {'Status'}")
garis()
for k in res2["data"]:
    print(f"{k['nama']:<20} {k['divisi']:<12} {rupiah(k['gaji']):<15} {k['status']}")
print(f"\nDitemukan: {res2['total']} karyawan")

# ── AGGREGATION ────────────────────────────────────────────
print("\nAGGREGATION - Laporan Gaji per Divisi ($match, $group, $sort)")
garis()
res3 = requests.get(f"{BASE_URL}/api/karyawan/laporan-divisi").json()
print(f"{'Divisi':<12} {'Jml':<6} {'Rata-rata Gaji':<18} {'Total Gaji'}")
garis()
for r in res3["data"]:
    print(f"{r['divisi']:<12} {r['jumlah_karyawan']:<6} {rupiah(r['rata_rata_gaji']):<18} {rupiah(r['total_gaji'])}")
print(f"\nTotal divisi: {res3['total_divisi']}")
print()