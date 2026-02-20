# Target Locations
LOCATIONS = ["Surabaya", "Sidoarjo", "Gresik"]

# Target Business Categories - UMKM/Industri Menengah-Besar
BUSINESS_QUERIES = [
    # Manufaktur & Pabrik (Fokus Produksi & Bahan Baku)
    "pabrik plastik injection",
    "pabrik garmen tekstil",
    "pabrik sparepart otomotif",
    "pabrik packaging kardus",
    "pabrik kosmetik maklon",
    "pabrik farmasi",
    "pabrik mebel ekspor",
    "pabrik kertas",
    "pabrik besi baja",
    "pabrik kimia industri",
    "pabrik pupuk",
    "pabrik cat",
    "perusahaan karoseri",
    "smelter",

    # F&B, Agrobisnis & Pengolahan (Fokus Batch & Expire Date)
    "pabrik makanan olahan",
    "pabrik minuman kemasan",
    "pabrik pakan ternak",
    "pengolahan hasil laut",
    "cold storage ikan",
    "rumah potong ayam",
    "pabrik roti industri",
    "coffee roastery besar",
    "central kitchen",
    "catering industri",

    # Distributor, Supply Chain & Logistik (Fokus Multi-Gudang)
    "distributor sembako grosir",
    "distributor FMCG",
    "supplier bahan bangunan",
    "distributor alat kesehatan",
    "distributor alat berat",
    "distributor sparepart industri",
    "distributor bahan kimia",
    "agen LPG besar",
    "importir mesin",
    "ekspedisi kargo",
    "perusahaan logistik",
    "jasa sewa gudang",

    # Retail Besar & Jaringan (Fokus Multi-Cabang & POS)
    "depo bangunan",
    "toko besi besar",
    "toko elektronik grosir",
    "grosir pakaian",
    "grosir kain",
    "supermarket lokal",
    "minimarket lokal",
    "distributor ATK",

    # Konstruksi & Properti (Fokus Project Management)
    "kontraktor sipil",
    "developer perumahan",
    "pabrik beton ready mix",
    "supplier aspal",
    "jasa konstruksi baja",

    # Layanan, Otomotif & Institusi (Fokus CRM & HRIS)
    "dealer resmi motor",
    "dealer mobil bekas besar",
    "bengkel resmi mobil",
    "klinik utama",
    "rumah sakit ibu dan anak",
    "perusahaan outsourcing",
    "BPR",
    "koperasi simpan pinjam"
]

# Micro Business Queries - Warung/Toko Kecil (Target: POS/Kasir Sederhana)
MICRO_BUSINESS_QUERIES = [
    # Warung & Kelontong (Target: POS / Kasir / Aplikasi Grosir)
    "warung madura",
    "toko kelontong",
    "toko sembako",
    "agen beras",
    "agen galon gas",
    "toko plastik",
    
    # F&B Skala Mikro/Kecil (Target: POS / QRIS Menu)
    "warkop",
    "warung kopi",
    "kedai kopi",
    "cafe kekinian",
    "depot makan",
    "warung tegal",
    "warung padang",
    "seblak",
    "mie gacoan",
    
    # Jasa Skala Kecil (Target: Aplikasi Booking / POS Sederhana)
    "laundry kiloan",
    "cuci motor",
    "cucian mobil",
    "barbershop",
    "pangkas rambut",
    "bengkel motor kecil",
    "toko pakan burung"
]

# Email patterns to prioritize
PRIORITY_EMAIL_PREFIXES = [
    "purchasing", "procurement", "info", "management",
    "finance", "business", "partnership", "it", "admin"
]

# Kawasan Industri Spesifik
INDUSTRIAL_AREAS = [
    "SIER Surabaya",
    "KIG Gresik", 
    "Berbek Sidoarjo",
    "Rungkut Industri",
    "Ngoro Industri"
]
