from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import  Alternatif, Kriteria, SubKriteria, DataKriteria

class AlternatifForms(forms.ModelForm):
    class Meta:
        model = Alternatif
        fields = ('nama', 'jabatan', 'body', 'divisi')
        widgets = {
            "nama" : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'type': 'text',
                    'placeholder': "Nama",
                    'required':True 
                }),
            "jabatan" : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'type': 'text',
                    'placeholder': "jabatan kerja",
                    'required':True 
                }),
            "body" : forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'cols': '30',
                    'rows': '10',
                    'required':True 
                }),
            "divisi" : forms.Select(
                attrs={
                    'class': 'selectpicker',
                    'type':'text',
                    'required':True,
                    'data-style':'btn btn-danger btn-block',
                    'title':'Pilih Kategory',
                    'data-size':'7',
                }),

        }

class KriteriaForms(forms.ModelForm):
    class Meta:
        model = Kriteria
        fields = ('kode_kriteria', 'nama_kriteria', 'bobot', 'jenis')
        widgets = {
            "kode_kriteria" : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'type': 'text',
                    'placeholder': "Kode Kriteria",
                    'required':True 
                }),
            "nama_kriteria" : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'type': 'text',
                    'placeholder': "Nama Kriteria",
                    'required':True 
                }),
            "bobot" : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'type': 'text',
                    'placeholder': 'Bobot',
                    'required':True 
                }),
            "jenis" : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'type':'text',
                    'placeholder': 'Jenis',
                    'required':True
                }),
        }
class SubkriteriaForms(forms.ModelForm):
    class Meta:
        model = SubKriteria
        fields = ('nama_sub_kriteria', 'nilai')
        widgets = {
            "nama_sub_kriteria" : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'type': 'text',
                    'placeholder': 'Nama Sub Kriteria',
                    'required':True
                }),
            "nilai" : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'type': 'text',
                    'placeholder': 'Nilai',
                    'required':True
                }),
        }

class DataKriteriaForms(forms.ModelForm):
    class Meta:
        model = DataKriteria
        fields = ('nama','absensi','skill','tanggung_jawab','loyalitas','pelanggaran')
        widgets = {
            "nama" : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'type': 'text',
                    'placeholder': "Nama",
                    'required':True 
                }),
            "absensi" : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'type': 'text',
                    'placeholder': 'Absensi',
                    'required':True
                }),
            "skill" :forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'type': 'text',
                    'placeholder': 'Skill',
                    'required':True
                }),
            "tanggung_jawab" :forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'type': 'text',
                    'placeholder': 'Tanggung Jawab',
                    'required':True
                }),
            "loyalitas":forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'type': 'text',
                    'placeholder': 'Loyalitas',
                    'required':True
                }),
            "pelanggaran" :forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'type': 'text',
                    'placeholder': 'Pelanggaran',
                    'required':True
                }),
        }

