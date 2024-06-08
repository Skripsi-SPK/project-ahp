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

admin.site.register(Divisi)
admin.site.register(Alternatif, AlternatifAdmin)
admin.site.register(Kriteria, KriteriaAdmin)
admin.site.register(SubKriteria)


admin.site.register(DataKriteria, DataKriteriaAdmin)
    