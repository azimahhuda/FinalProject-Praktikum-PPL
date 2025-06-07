from django.contrib import admin
from django.utils.html import format_html
from .models import Hewan, PengajuanAdopsi

@admin.register(Hewan)
class HewanAdmin(admin.ModelAdmin):
    list_display = ['nama', 'jenis', 'umur', 'status', 'tanggal_dibuat', 'foto_preview']
    list_filter = ['jenis', 'status', 'tanggal_dibuat']
    search_fields = ['nama', 'deskripsi']
    readonly_fields = ['tanggal_dibuat', 'tanggal_diupdate']
    list_per_page = 20
    
    def foto_preview(self, obj):
        if obj.foto:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 5px;" />', obj.foto.url)
        return "Tidak ada foto"
    foto_preview.short_description = "Foto"

@admin.register(PengajuanAdopsi)
class PengajuanAdopsiAdmin(admin.ModelAdmin):
    list_display = ['nama_pengaju', 'hewan', 'email', 'status', 'tanggal_pengajuan']
    list_filter = ['status', 'tanggal_pengajuan', 'hewan__jenis']
    search_fields = ['nama_pengaju', 'email', 'hewan__nama']
    readonly_fields = ['tanggal_pengajuan']
    list_per_page = 20
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('hewan')
