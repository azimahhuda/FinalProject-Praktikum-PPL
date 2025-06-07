from django import forms
from django.core.validators import validate_email
from .models import Hewan, PengajuanAdopsi

class HewanForm(forms.ModelForm):
    class Meta:
        model = Hewan
        fields = ['nama', 'jenis', 'umur', 'deskripsi', 'foto', 'status']
        widgets = {
            'nama': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama hewan'}),
            'jenis': forms.Select(attrs={'class': 'form-control'}),
            'umur': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'max': '300'}),
            'deskripsi': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Deskripsi hewan'}),
            'foto': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
    
    def clean_nama(self):
        nama = self.cleaned_data.get('nama')
        if nama and len(nama.strip()) < 2:
            raise forms.ValidationError("Nama hewan minimal 2 karakter.")
        return nama.strip() if nama else nama
    
    def clean_umur(self):
        umur = self.cleaned_data.get('umur')
        if umur and (umur < 1 or umur > 300):
            raise forms.ValidationError("Umur hewan harus antara 1-300 bulan.")
        return umur

class UpdateStatusForm(forms.ModelForm):
    class Meta:
        model = PengajuanAdopsi
        fields = ['status', 'catatan_admin']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
            'catatan_admin': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Catatan tambahan (opsional)'}),
        }

class PengajuanAdopsiForm(forms.ModelForm):
    class Meta:
        model = PengajuanAdopsi
        fields = ['nama_pengaju', 'email', 'alasan']
        widgets = {
            'nama_pengaju': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama lengkap'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email aktif'}),
            'alasan': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Alasan mengapa ingin mengadopsi hewan ini'}),
        }
    
    def clean_nama_pengaju(self):
        nama = self.cleaned_data.get('nama_pengaju')
        if nama and len(nama.strip()) < 3:
            raise forms.ValidationError("Nama minimal 3 karakter.")
        return nama.strip() if nama else nama
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            try:
                validate_email(email)
            except forms.ValidationError:
                raise forms.ValidationError("Format email tidak valid.")
        return email
    
    def clean_alasan(self):
        alasan = self.cleaned_data.get('alasan')
        if alasan and len(alasan.strip()) < 20:
            raise forms.ValidationError("Alasan minimal 20 karakter.")
        return alasan.strip() if alasan else alasan
