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

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run Scraper

**Default (Surabaya, Sidoarjo, Gresik):**
```bash
python lead_scraper.py
```

**Custom Lokasi:**
```bash
# Single lokasi
python lead_scraper.py --locations Malang

# Multiple lokasi
python lead_scraper.py --locations Surabaya Malang Mojokerto

# Alias pendek
python lead_scraper.py -l Banyuwangi Jember
```

**Skip Micro Business:**
```bash
python lead_scraper.py --no-micro
```

**Custom Output File:**
```bash
python lead_scraper.py -o hasil_surabaya.xlsx
```

**Kombinasi:**
```bash
python lead_scraper.py -l Malang Batu --no-micro -o leads_malang.xlsx
```

Script akan:
- Google Dorking otomatis buat tiap kategori bisnis × lokasi
- Crawl website yang ditemukan
- Extract email, HP, alamat dari website
- Export hasil ke `erp_leads.csv` dan `erp_leads.json`

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

1. **Rate Limiting**: Script udah ada delay otomatis, tapi kalau Google block, tunggu beberapa jam atau pakai VPN
2. **Hasil Terbaik**: Jalankan di jam kerja (09:00-17:00) buat dapetin website yang aktif
3. **Filter Manual**: Setelah scraping, filter manual buat prioritas lead terbaik
4. **Follow-up**: Pakai email `purchasing@` atau `procurement@` buat cold email pertama

## Troubleshooting

**Google block/CAPTCHA**: 
- Pakai VPN atau proxy
- Kurangi `num_results` di `google_dork_search()`
- Tambah `sleep_interval` lebih lama

**Website timeout**:
- Normal, skip aja
- Bisa re-run script, URL yang udah di-scrape akan di-skip

**Hasil sedikit**:
- Tambah kategori bisnis di `scraper_config.py`
- Coba keyword alternatif (misal: "pabrik" → "industri", "PT", "CV")
