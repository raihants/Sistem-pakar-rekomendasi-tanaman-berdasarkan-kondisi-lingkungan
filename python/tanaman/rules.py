# forward_chaining_tanaman.py

# Fakta awal (contoh)
facts = {"tanah_gembur", "curah_hujan_tinggi"}

rules = [
    # --- Tanaman Pangan ---
    {"if": {"tanah_gembur", "curah_hujan_tinggi"}, "then": "cocok_padi"},
    {"if": {"tanah_gembur", "curah_hujan_rendah"}, "then": "cocok_jagung"},
    {"if": {"tanah_liat", "curah_hujan_sedang"}, "then": "cocok_singkong"},
    {"if": {"tanah_berpasir", "curah_hujan_rendah"}, "then": "cocok_kacang_tanah"},

    # --- Tanaman Sayur ---
    {"if": {"tanah_gembur", "iklim_dingin"}, "then": "cocok_kentang"},
    {"if": {"tanah_subur", "iklim_panas"}, "then": "cocok_cabai"},
    {"if": {"tanah_gembur", "iklim_panas", "curah_hujan_sedang"}, "then": "cocok_tomat"},

    # --- Tanaman Buah ---
    {"if": {"tanah_gembur", "curah_hujan_tinggi", "iklim_panas"}, "then": "cocok_pisang"},
    {"if": {"tanah_subur", "iklim_dingin"}, "then": "cocok_stroberi"},
    {"if": {"tanah_berpasir", "iklim_panas"}, "then": "cocok_semangka"},

    # --- Rekomendasi akhir ---
    {"if": {"cocok_padi"}, "then": "rekomendasi: tanam_padi"},
    {"if": {"cocok_jagung"}, "then": "rekomendasi: tanam_jagung"},
    {"if": {"cocok_singkong"}, "then": "rekomendasi: tanam_singkong"},
    {"if": {"cocok_kacang_tanah"}, "then": "rekomendasi: tanam_kacang_tanah"},
    {"if": {"cocok_kentang"}, "then": "rekomendasi: tanam_kentang"},
    {"if": {"cocok_cabai"}, "then": "rekomendasi: tanam_cabai"},
    {"if": {"cocok_tomat"}, "then": "rekomendasi: tanam_tomat"},
    {"if": {"cocok_pisang"}, "then": "rekomendasi: tanam_pisang"},
    {"if": {"cocok_stroberi"}, "then": "rekomendasi: tanam_stroberi"},
    {"if": {"cocok_semangka"}, "then": "rekomendasi: tanam_semangka"},
]
