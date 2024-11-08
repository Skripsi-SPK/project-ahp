from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import  Alternatif, Kriteria, SubKriteria, DataKriteria, Comparison,  Perbandingan, Perhitungan, SubCriterion

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

class ComparisonForm(forms.ModelForm):
    class Meta:
        model = Comparison
        fields = ['criteria1', 'criteria2', 'value']

    def clean(self):
        cleaned_data = super().clean()
        c1 = cleaned_data.get('criteria1')
        c2 = cleaned_data.get('criteria2')
        if c1 == c2:
            raise forms.ValidationError("Criteria must be different.")
        
class PerbandinganForm(forms.ModelForm):
    class Meta:
        model = Perbandingan
        fields = ['subcriteria1', 'subcriteria2', 'value']

    def clean(self):
        cleaned_data = super().clean()
        c1 = cleaned_data.get('subcriteria1')
        c2 = cleaned_data.get('subcriteria2')
        if c1 == c2:
            raise forms.ValidationError("SubCriteria must be different.")
        

class PerhitunganForm(forms.ModelForm):
    class Meta:
        model = Perhitungan
        fields = ['alternatif', 'kriteria', 'sub_kriteria']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sub_kriteria'].queryset = SubCriterion.objects.none()

        if 'kriteria' in self.data:
            kriteria_id = int(self.data.get('kriteria'))
            self.fields['sub_kriteria'].queryset = SubCriterion.objects.filter(kriteria_id=kriteria_id)

