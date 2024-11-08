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

class Criteria(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Comparison(models.Model):
    criteria1 = models.ForeignKey(Criteria, related_name='comparisons_as_first', on_delete=models.CASCADE)
    criteria2 = models.ForeignKey(Criteria, related_name='comparisons_as_second', on_delete=models.CASCADE)
    value = models.FloatField()

    def __str__(self):
        return f"{self.criteria1} vs {self.criteria2} : {self.value}"

class SubCriteria(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Perbandingan(models.Model):
    subcriteria1 = models.ForeignKey(SubCriteria, related_name='comparisons_as_first', on_delete=models.CASCADE)
    subcriteria2 = models.ForeignKey(SubCriteria, related_name='comparisons_as_second', on_delete=models.CASCADE)
    value = models.FloatField()

    def __str__(self):
        return f"{self.subcriteria1} vs {self.subcriteria2} : {self.value}"
    
class Criterion(models.Model):
    nama = models.CharField(max_length=100)
    bobot = models.FloatField()

    def __str__(self):
        return self.nama

class SubCriterion(models.Model):
    NILAI_CHOICES = [
        ('5', '5'),
        ('4', '4'),
        ('3', '3'),
        ('2', '2'),
        ('1', '1'),
        
    ]
    
    kriteria = models.ForeignKey(Criterion, on_delete=models.CASCADE)
    nilai = models.CharField(max_length=20, choices=NILAI_CHOICES)
    bobot = models.FloatField()

    def __str__(self):
        return f"{self.kriteria.nama} - {self.nilai}"


class Alternative(models.Model):
    nama = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nama

class Perhitungan(models.Model):
    alternatif = models.ForeignKey(Alternative, on_delete=models.CASCADE)
    kriteria = models.ForeignKey(Criterion, on_delete=models.CASCADE)
    sub_kriteria = models.ForeignKey(SubCriterion, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.alternatif.nama} - {self.kriteria.nama}"

class Total(models.Model):
    alternatif = models.ForeignKey(Alternative, on_delete=models.CASCADE)
    nilai_akhir = models.FloatField()
    ranking = models.IntegerField()
    tanggal = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.alternatif.nama} - Ranking {self.ranking}"
    

