
# 🐾 Pawfect Home

**Pawfect Home** adalah aplikasi web berbasis Django yang memfasilitasi adopsi hewan peliharaan seperti kucing, anjing, kelinci, landak, hamster, dan iguana. Aplikasi ini memungkinkan pengguna melihat daftar hewan yang tersedia dan mengajukan permohonan adopsi, serta menyediakan dashboard admin untuk mengelola data hewan dan pengajuan.

## 🚀 Fitur Utama

- Beranda publik untuk melihat daftar hewan yang tersedia.
- Detail hewan dan form pengajuan adopsi.
- Login dan registrasi pengguna.
- Dashboard admin untuk:
  - Menambahkan, mengedit, dan menghapus data hewan.
  - Melihat dan mengelola pengajuan adopsi.
  - Mengubah status pengajuan dan hewan.

## 🛠 Teknologi yang Digunakan

- **Backend**: Python, Django
- **Frontend**: HTML, CSS 
- **Database**: SQLite (default Django)
- **Media**: Upload gambar hewan (disimpan di `media/`)

## 📁 Struktur Folder

```
hewan_adopsi/                # Root project directory
│
├── hewan_adopsi/            # Django project utama
│   ├── init.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── adopsi/                  # Aplikasi Django (app) utama
│   ├── migrations/          # Folder migrasi database
│   │   └── init.py
│   ├── templates/           # Folder template HTML
│   │   └── adopsi/
│   │       ├── beranda.html
│   │       ├── dashboard_admin.html
│   │       ├── dashboard.html
│   │       ├── daftar_hewan.html
│   │       ├── detail_hewan.html
│   │       ├── form_hewan.html
│   │       ├── landing_page.html
│   │       ├── login_page.html
│   │       ├── register.html
│   │       └── ubah_status_pengajuan.html
│   ├── init.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── media_foto_hewan/        # Folder media upload foto hewan
│
├── db.sqlite3               # Database SQLite bawaan Django
├── manage.py                # File manajemen Django
└── venv/                    # Virtual environment
```

## 🧪 Cara Menjalankan

1. **Clone repo** dan masuk ke direktori:
   ```bash
   git clone <repo_url>
   cd hewan_adopsi
   ```

2. **Aktifkan virtual environment** dan install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install django
   python -m pip install Pillow
   ```

3. **Migrasi database dan jalankan server:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver
   ```

4. **Akses di browser:**  
   `http://127.0.0.1:8000/`

## 🙌 Anggota

- Cut Dahliana (2208107010027)
- Azimah Al-Huda (2208107010069)
- Firjatullah Afny Abus (2208107010059)
