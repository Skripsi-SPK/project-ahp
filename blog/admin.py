from django.contrib import admin
from .models import *


class AlternatifAdmin(admin.ModelAdmin):
    list_display = ('nama','jabatan','body','divisi','date')

class KriteriaAdmin(admin.ModelAdmin):
    list_display = ('kode_kriteria','nama_kriteria','bobot','jenis')

class SubKriteriaAdmin(admin.ModelAdmin):
    list_display = ('nama_sub_kriteria','nilai')

class DataKriteriaAdmin(admin.ModelAdmin):
    list_display = ('nama','absensi','skill','tanggung_jawab','loyalitas','pelanggaran')

class CriteriaAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ComparisonAdmin(admin.ModelAdmin):
    list_display = ('criteria1', 'criteria2', 'value')

class SubCriteriaAdmin(admin.ModelAdmin):
    list_display = ('name',)

class PerbandinganAdmin(admin.ModelAdmin):
    list_display = ('subcriteria1', 'subcriteria2', 'value')

admin.site.register(Divisi)
admin.site.register(Alternatif, AlternatifAdmin)
admin.site.register(Kriteria, KriteriaAdmin)
admin.site.register(SubKriteria)


admin.site.register(DataKriteria, DataKriteriaAdmin)

admin.site.register(Criteria, CriteriaAdmin)
admin.site.register(Comparison, ComparisonAdmin)

admin.site.register(SubCriteria, SubCriteriaAdmin)
admin.site.register(Perbandingan, PerbandinganAdmin)
    