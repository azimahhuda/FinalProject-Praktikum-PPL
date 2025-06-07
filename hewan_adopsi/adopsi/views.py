from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Hewan, PengajuanAdopsi
from .forms import HewanForm, UpdateStatusForm

def is_admin(user):
    return user.is_staff and user.is_authenticated

def landing_page(request):
    return render(request, 'adopsi/landing_page.html')

def daftar_hewan(request):
    hewans = Hewan.objects.filter(status='Tersedia')
    return render(request, 'adopsi/daftar_hewan.html', {'hewans': hewans})

def login_page(request):
    return render(request, 'adopsi/login_page.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard') 
            else:
                messages.error(request, 'Username atau password salah')
        else:
            messages.error(request, 'Username dan password harus diisi')
    
    return render(request, 'adopsi/user_login.html')

def user_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Validasi input kosong
        if not all([username, email, password1, password2]):
            messages.error(request, "Semua field harus diisi.")
        elif password1 != password2:
            messages.error(request, "Password tidak cocok.")
        elif len(password1) < 8:
            messages.error(request, "Password minimal 8 karakter.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username sudah digunakan.")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email sudah digunakan.")
        else:
            try:
                User.objects.create_user(username=username, email=email, password=password1)
                messages.success(request, "Akun berhasil dibuat. Silakan login.")
                return redirect('user_login')
            except Exception as e:
                messages.error(request, "Terjadi kesalahan saat membuat akun.")
    
    return render(request, 'adopsi/register.html')

def user_logout(request):
    logout(request)
    messages.success(request, "Anda telah berhasil logout.")
    return redirect('landing_page')

@login_required
def dashboard(request):
    return render(request, 'adopsi/dashboard.html')

def detail_hewan(request, pk):
    hewan = get_object_or_404(Hewan, pk=pk)

    if request.method == 'POST':
        nama_pengaju = request.POST.get('nama')
        email = request.POST.get('email')
        alasan = request.POST.get('alasan')
        
        # Validasi input
        if not all([nama_pengaju, email, alasan]):
            messages.error(request, 'Semua field harus diisi.')
            return render(request, 'adopsi/detail_hewan.html', {'hewan': hewan})
        
        # Cek apakah hewan masih tersedia
        if hewan.status != 'Tersedia':
            messages.error(request, 'Hewan ini sudah tidak tersedia untuk adopsi.')
            return redirect('daftar_hewan')
        
        try:
            PengajuanAdopsi.objects.create(
                hewan=hewan,
                nama_pengaju=nama_pengaju,
                email=email,
                alasan=alasan
            )
            hewan.status = 'Diproses'
            hewan.save()
            messages.success(request, 'Pengajuan adopsi berhasil dikirim!')
            return redirect('daftar_hewan')
        except Exception as e:
            messages.error(request, 'Terjadi kesalahan saat mengirim pengajuan.')

    return render(request, 'adopsi/detail_hewan.html', {'hewan': hewan})

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_staff: 
                login(request, user)
                return redirect('dashboard_admin')
            else:
                messages.error(request, "Username atau password salah, atau Anda bukan admin.")
        else:
            messages.error(request, "Username dan password harus diisi.")
    
    return render(request, 'adopsi/admin_login.html')

@user_passes_test(is_admin, login_url='admin_login')
def dashboard_admin(request):
    hewans = Hewan.objects.all().order_by('-id')
    pengajuan = PengajuanAdopsi.objects.all().order_by('-tanggal_pengajuan')
    return render(request, 'adopsi/dashboard_admin.html', {
        'hewans': hewans,
        'pengajuan': pengajuan
    })

@user_passes_test(is_admin, login_url='admin_login')
def tambah_hewan(request):
    if request.method == 'POST':
        form = HewanForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Hewan berhasil ditambahkan!')
            return redirect('dashboard_admin')
        else:
            messages.error(request, 'Terjadi kesalahan. Periksa kembali form Anda.')
    else:
        form = HewanForm()
    return render(request, 'adopsi/form_hewan.html', {'form': form, 'mode': 'Tambah'})

@user_passes_test(is_admin, login_url='admin_login')
def edit_hewan(request, pk):
    hewan = get_object_or_404(Hewan, pk=pk)
    if request.method == 'POST':
        form = HewanForm(request.POST, request.FILES, instance=hewan)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data hewan berhasil diupdate!')
            return redirect('dashboard_admin')
        else:
            messages.error(request, 'Terjadi kesalahan. Periksa kembali form Anda.')
    else:
        form = HewanForm(instance=hewan)
    return render(request, 'adopsi/form_hewan.html', {'form': form, 'mode': 'Edit', 'hewan': hewan})

@user_passes_test(is_admin, login_url='admin_login')
def hapus_hewan(request, pk):
    hewan = get_object_or_404(Hewan, pk=pk)
    
    # Terima both GET dan POST
    if request.method == 'POST' or request.method == 'GET':
        nama_hewan = hewan.nama
        hewan.delete()
        messages.success(request, f'Hewan {nama_hewan} berhasil dihapus!')
    
    return redirect('dashboard_admin')

@user_passes_test(is_admin, login_url='admin_login')
def ubah_status_pengajuan(request, pk):
    pengajuan = get_object_or_404(PengajuanAdopsi, pk=pk)
    if request.method == 'POST':
        form = UpdateStatusForm(request.POST, instance=pengajuan)
        if form.is_valid():
            pengajuan = form.save()
            # Jika status diterima, update status hewan
            if pengajuan.status == 'Diterima':
                hewan = pengajuan.hewan
                hewan.status = 'Diadopsi'
                hewan.save()
                messages.success(request, f'Pengajuan adopsi {hewan.nama} telah diterima!')
            elif pengajuan.status == 'Ditolak':
                # Kembalikan status hewan ke Tersedia jika ditolak
                hewan = pengajuan.hewan
                hewan.status = 'Tersedia'
                hewan.save()
                messages.success(request, f'Pengajuan adopsi {hewan.nama} telah ditolak.')
            else:
                messages.success(request, 'Status pengajuan berhasil diupdate!')
            return redirect('dashboard_admin')
        else:
            messages.error(request, 'Terjadi kesalahan saat mengupdate status.')
    else:
        form = UpdateStatusForm(instance=pengajuan)
    return render(request, 'adopsi/ubah_status_pengajuan.html', {'form': form, 'pengajuan': pengajuan})