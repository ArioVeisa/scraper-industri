# ERP Lead Scraper - Surabaya, Sidoarjo, Gresik

Tools scraping gratis buat dapetin data kontak UMKM/Industri yang butuh ERP.

## Target Data
- Nama bisnis
- Alamat
- Email (prioritas: purchasing@, procurement@, info@, management@)
- No HP/Telepon
- Website

## Target Bisnis
1. Manufaktur & Pabrik (plastik, garmen, tekstil, sparepart, packaging, F&B)
2. Distributor, Grosir & Logistik
3. F&B Skala Menengah-Besar (roastery, franchise, central kitchen)
4. Retail Grosir & Jaringan Toko
5. Institusi Keuangan Lokal & Koperasi (BPR, koperasi)

## Cara Pakai

### 1. Setup Virtual Environment
```bash
# Create venv
python3 -m venv venv

# Activate venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Run Scraper

**PENTING: Selalu activate venv dulu sebelum run!**
```bash
source venv/bin/activate
```

**Default (5 hasil per kategori, ~20 menit):**
```bash
python3 lead_scraper.py
```

**Quick Test (3 hasil per kategori, ~12 menit):**
```bash
python3 lead_scraper.py -r 3
```

**Deep Scrape (10 hasil per kategori, ~40 menit):**
```bash
python3 lead_scraper.py -r 10
```

**Test Mode (10 kategori pertama aja):**
```bash
python3 lead_scraper.py -m 10 -r 3
```

**Custom Lokasi:**
```bash
# Single lokasi
python3 lead_scraper.py --locations Malang

# Multiple lokasi
python3 lead_scraper.py --locations Surabaya Malang Mojokerto

# Alias pendek
python3 lead_scraper.py -l Banyuwangi Jember
```

**Skip Micro Business:**
```bash
python3 lead_scraper.py --no-micro
```

**Custom Output File:**
```bash
python3 lead_scraper.py -o hasil_surabaya.xlsx
```

**Kombinasi:**
```bash
# Malang only, no micro, 3 results per category
python3 lead_scraper.py -l Malang --no-micro -r 3 -o leads_malang.xlsx

# Test 5 kategori pertama, 2 results each
python3 lead_scraper.py -m 5 -r 2 -o test.xlsx
```

**Selesai? Deactivate venv:**
```bash
deactivate
```

### 3. Customize Target (Opsional)
Edit `scraper_config.py` buat:
- Tambah/kurangi kategori bisnis
- Tambah lokasi lain
- Tambah kawasan industri spesifik

## Output

**erp_leads.xlsx** - Excel file dengan formatting:
```
Nama | Kategori | Lokasi | Alamat | Email | No HP | Website
```

**erp_leads.json** - Format lengkap dengan array email/phone

## Tips

1. **Rate Limiting**: Script udah ada delay otomatis, tapi kalau kena block, tunggu beberapa jam atau pakai VPN
2. **Hasil Terbaik**: Jalankan di jam kerja (09:00-17:00) buat dapetin website yang aktif
3. **Filter Manual**: Setelah scraping, filter manual buat prioritas lead terbaik
4. **Follow-up**: Pakai email `purchasing@` atau `procurement@` buat cold email pertama

## Troubleshooting

**ModuleNotFoundError**: 
- Lu lupa activate venv! Jalankan: `source venv/bin/activate`

**Website timeout**:
- Normal, skip aja
- Bisa re-run script, URL yang udah di-scrape akan di-skip

**Hasil sedikit**:
- Tambah kategori bisnis di `scraper_config.py`
- Coba keyword alternatif (misal: "pabrik" → "industri", "PT", "CV")
- Naikkan `-r` value (misal: `-r 10`)

## Estimasi Waktu & Hasil

| Mode | Command | Kategori | URLs | Waktu |
|------|---------|----------|------|-------|
| **Quick Test** | `-m 10 -r 3` | 10 | ~90 | ~10 menit |
| **Medium** | `-r 5` | 81 | ~1,215 | ~2 jam |
| **No Micro** | `--no-micro -r 5` | 58 | ~870 | ~1.5 jam |
| **Deep** | `-r 10` | 81 | ~2,430 | ~4 jam |
