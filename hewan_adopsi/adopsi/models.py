from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Hewan(models.Model):
    JENIS_CHOICES = [
        ('kucing', 'Kucing'),
        ('anjing', 'Anjing'),
        ('kelinci', 'Kelinci'),
        ('hamster', 'Hamster'),
        ('iguana', 'Iguana'),
        ('landak', 'Landak'),
    ]
    
    STATUS_CHOICES = [
        ('Tersedia', 'Tersedia'),
        ('Diproses', 'Diproses'),
        ('Diadopsi', 'Diadopsi'),
    ]

    nama = models.CharField(max_length=100)
    jenis = models.CharField(max_length=10, choices=JENIS_CHOICES)
    umur = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(300)],
        help_text="Umur dalam bulan"
    )
    deskripsi = models.TextField()
    foto = models.ImageField(upload_to='foto_hewan/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Tersedia')
    tanggal_dibuat = models.DateTimeField(auto_now_add=True)
    tanggal_diupdate = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Hewan"
        verbose_name_plural = "Hewan"
        ordering = ['-tanggal_dibuat']

    def __str__(self):
        return f"{self.nama} ({self.get_jenis_display()})"
    
class PengajuanAdopsi(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Diterima', 'Diterima'),
        ('Ditolak', 'Ditolak'),
    ]
    
    hewan = models.ForeignKey(Hewan, on_delete=models.CASCADE, related_name='pengajuan_adopsi')
    nama_pengaju = models.CharField(max_length=100)
    email = models.EmailField()
    alasan = models.TextField()
    tanggal_pengajuan = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    catatan_admin = models.TextField(blank=True, null=True, help_text="Catatan dari admin")

    class Meta:
        verbose_name = "Pengajuan Adopsi"
        verbose_name_plural = "Pengajuan Adopsi"
        ordering = ['-tanggal_pengajuan']

    def __str__(self):
        return f"Pengajuan {self.nama_pengaju} untuk {self.hewan.nama}"
