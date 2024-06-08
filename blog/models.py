from django.db import models


class Divisi(models.Model):
    nama = models.CharField(max_length=20)

    def __str__(self):
        return self.nama
    
    class Meta:
        verbose_name_plural = 'Divisi'
        
        

class Alternatif(models.Model):
    nama = models.CharField(max_length=100, blank=True, null=True)
    jabatan = models.CharField(max_length=100)
    body = models.TextField()
    divisi = models.ForeignKey(Divisi, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {}". format(self.nama, self.jabatan)
    
    class Meta:
        ordering = ['-date']
        verbose_name_plural = "Alternatif"

class Kriteria(models.Model):
    kode_kriteria = models.CharField(max_length=100, blank=True, null=True)
    nama_kriteria = models.CharField(max_length=100)
    bobot= models.CharField(max_length=100)
    jenis = models.CharField(max_length=100)

    def __str__(self):
        return "{} - {}". format(self.kode_kriteria, self.nama_kriteria)

    class Meta:
        verbose_name_plural = "Kriteria"

class SubKriteria(models.Model):
    nama_sub_kriteria = models.CharField(max_length=100, blank=True, null=True)
    nilai = models.IntegerField(default=0)

    def __str__(self):
        return "{} - {}". format(self.nama_sub_kriteria, self.nilai)

    class Meta:
        verbose_name_plural = "SubKriteria"


class DataKriteria(models.Model):
    nama = models.CharField(max_length=100, blank=True, null=True)
    absensi = models.IntegerField(default=0)
    skill = models.IntegerField(default=0)
    tanggung_jawab = models.IntegerField(default=0)
    loyalitas = models.IntegerField(default=0)
    pelanggaran = models.IntegerField(default=0)

    def __str__(self):
        return self.nama
    
    class Meta:
        verbose_name_plural = "DataKriteria"
