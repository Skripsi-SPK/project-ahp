from re import template
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Alternatif, Divisi, Kriteria, SubKriteria, DataKriteria
from .forms import AlternatifForms, KriteriaForms, SubkriteriaForms, DataKriteriaForms

from numpy.linalg import eig
import numpy as np

@login_required

def dashboard(request):
    template_name = "dashboard/dashboard.html"
    context ={
        'title':'dashboard',
        
    }
    return render(request ,template_name, context)

@login_required
def alternatif(request):
    template_name = "dashboard/data_alternatif.html"
    alternatif = Alternatif.objects.all()
    # for a in alternatif:
     #   print(a.nama,'_',a.jabatan,'_',a.divisi)
    context ={
        'title':'data alternatif',
        'alternatif':alternatif,
        
    }
    return render(request ,template_name, context)

@login_required
def tambah_alternatif(request):
    template_name = "dashboard/tambah_alternatif.html"
    divisi = Divisi.objects.all()
    
    if request.method == "POST":
        forms_alternatif = AlternatifForms(request.POST)
        if forms_alternatif.is_valid():
            forms_alternatif.save()

        return redirect(alternatif)
    else:
        forms_alternatif = AlternatifForms()
        pass
    context ={
        'title':'tambah alternatif',
        'divisi':divisi,
        'forms_alternatif':forms_alternatif
    }
    return render(request, template_name, context)

@login_required
def lihat_alternatif(request, id):
    template_name = "dashboard/lihat_alternatif.html"
    alternatif = Alternatif.objects.get(id=id)
    context = {
        'title':'lihat alternatif',
        'alternatif': alternatif,
    }
    return render(request, template_name, context)

@login_required
def edit_alternatif(request, id):
    template_name = "dashboard/tambah_alternatif.html"
    a = Alternatif.objects.get(id=id)
    if request.method == "POST":
        forms_alternatif= AlternatifForms(request.POST, instance=a)
        if forms_alternatif.is_valid():
           forms_alternatif.save()
        return redirect(alternatif)
    else:
        forms_alternatif= AlternatifForms(instance=a)
           
    context = {
        'title':'edit alternatif',
        'alternatif': a,
        'forms_alternatif':forms_alternatif
    }
    return render(request, template_name, context)

@login_required
def delete_alternatif(request, id):
    Alternatif.objects.get(id=id).delete()
    return redirect(alternatif)

@login_required
def kriteria(request):
    template_name = "dashboard/data_kriteria.html"
    kriteria = Kriteria.objects.all()
    
    context ={
        'title':'bobot kriteria',
        'kriteria':kriteria,
        
    }
    return render(request ,template_name, context)

@login_required
def tambah_kriteria(request):
    template_name = "dashboard/tambah_kriteria.html"
    k = Kriteria.objects.all()

    if request.method == "POST":
       forms_kriteria = KriteriaForms(request.POST)
       if forms_kriteria.is_valid():
           forms_kriteria.save()

       return redirect(kriteria)
    else:
        forms_kriteria = KriteriaForms()
        pass
    context={
        'title':'tambah kriteria',
        'k':k,
        'forms_kriteria':forms_kriteria
        
    }
    return render(request, template_name, context)

@login_required
def edit_kriteria(request, id):
    template_name = "dashboard/tambah_kriteria.html"
    k = Kriteria.objects.get(id=id)
    if request.method == "POST":
        forms_kriteria= KriteriaForms(request.POST, instance=k)
        if forms_kriteria.is_valid():
            forms_kriteria.save()
        return redirect(kriteria)
    else:
        forms_kriteria= KriteriaForms(instance=k)
    
    context = {
        'title':'edit kriteria',
        'kriteria': k,
        'forms_kriteria':forms_kriteria
    }
    return render(request, template_name, context)

@login_required
def delete_kriteria(request, id):
    Kriteria.objects.get(id=id).delete()
    return redirect(kriteria)


@login_required
def sub_kriteria(request):
    template_name = "dashboard/data_subkriteria.html"
    sub_kriteria = SubKriteria.objects.all()
    #print(subkriteria)
    context ={
        'title':'nilai kriteria',
        'subkriteria':sub_kriteria,
        
    }
    return render(request ,template_name, context)

@login_required
def tambah_subkriteria(request):
    template_name = "dashboard/tambah_subkriteria.html"
    sk = SubKriteria.objects.all()

    if request.method == "POST":
       forms_sub_kriteria = SubkriteriaForms(request.POST)
       if forms_sub_kriteria.is_valid():
            forms_sub_kriteria.save()

       return redirect(sub_kriteria)
    else:
        forms_sub_kriteria = SubkriteriaForms() 
        pass
    context={
        'title':'tambah subkriteria',
        'sk':sk,
        'forms_sub_kriteria':forms_sub_kriteria
        
    }
    return render(request, template_name, context)

@login_required
def edit_subkriteria(request, id):
    template_name = "dashboard/tambah_subkriteria.html"
    sk = SubKriteria.objects.get(id=id)
    if request.method == "POST":
       forms_sub_kriteria= SubkriteriaForms(request.POST, instance=sk)
       if forms_sub_kriteria.is_valid():
            forms_sub_kriteria.save()

       return redirect(sub_kriteria)
    else:
        forms_sub_kriteria= SubkriteriaForms(instance=sk)

    context = {
        'title':'edit subkriteria',
        'subkriteria': sk,
        'forms_sub_kriteria':forms_sub_kriteria
    }
    return render(request, template_name, context)


@login_required
def delete_subkriteria(request, id):
    SubKriteria.objects.get(id=id).delete()
    return redirect(sub_kriteria)

@login_required
def data_kriteria(request):
    template_name = "dashboard/data_nilai.html"
    data_kriteria = DataKriteria.objects.all()
    
    context ={
        'title':'data kriteria',
        'datakriteria':data_kriteria, 
    }
    return render(request ,template_name, context)

@login_required
def tambah_nilai(request):
    template_name = "dashboard/tambah_nilai.html"
    dk = DataKriteria.objects.all()

    if request.method == "POST":
       forms_datakriteria = DataKriteriaForms(request.POST)
       if forms_datakriteria.is_valid():
           forms_datakriteria.save()

       return redirect(data_kriteria)
    else:
        forms_datakriteria = DataKriteriaForms()
        pass
    context={
        'title':'tambah kriteria',
        'dk':dk,
        'forms_datakriteria':forms_datakriteria
        
    }
    return render(request, template_name, context)

@login_required
def edit_data(request, id):
    template_name = "dashboard/tambah_nilai.html"
    dk = DataKriteria.objects.get(id=id)
    if request.method == "POST":
        forms_datakriteria= DataKriteriaForms(request.POST, instance=dk)
        if forms_datakriteria.is_valid():
            forms_datakriteria.save()
        return redirect(data_kriteria)
    else:
        forms_datakriteria= DataKriteriaForms(instance=dk)
    
    context = {
        'title':'edit kriteria',
        'datakriteria': dk,
        'forms_datakriteria':forms_datakriteria
    }
    return render(request, template_name, context)

@login_required
def delete_data(request, id):
    DataKriteria.objects.get(id=id).delete()
    return redirect(data_kriteria)


@login_required
def perbandingan(request):
    template_name = "dashboard/perbandingan kriteria.html"
    context ={
        'title':'perbandingan kriteria',
        
    }
    return render(request ,template_name, context)

@login_required
def rumus(request):
    template_name = "dashboard/perbandingan alternatif.html"
    context ={
        'title':'perbandingan alternatif',
        
    }
    return render(request ,template_name, context)

@login_required
def hasil(request):
    template_name = "dashboard/hasil perhitungan.html"
    criteria_data = DataKriteria.objects.all().first()  # Ambil hanya satu data saja sesuai kebutuhan Anda

    # Ubah data dari model ke dalam bentuk dictionary
    data = {
        'absensi': criteria_data.absensi,
        'skill': criteria_data.skill,
        'tanggung_jawab': criteria_data.tanggung_jawab,
        'loyalitas': criteria_data.loyalitas,
        'pelanggaran': criteria_data.pelanggaran
    }

    # Hitung bobot relatif menggunakan fungsi calculate_AHP_weights
    weights = calculate_AHP_weights(data)

    print("Bobot relatif kriteria:", weights)
    context ={
        'title':'hasil perhitungan',
        
    }
    return render(request ,template_name, context)


def calculate_AHP_weights(data):
    # Buat matriks perbandingan pasangan
    pairwise_matrix = np.array([
        [1, data['absensi'],data['skill'], data['loyalitas'], data['tanggung_jawab']],
        [1/data['absensi'], 1, data['absensi']/data['skill'], data['absensi']/data['loyalitas'], data['absensi']/data['tanggung_jawab']],
        [1/data['skill'], data['skill']/data['absensi'], 1, data['skill']/data['loyalitas'], data['skill']/data['tanggung_jawab']],
        [1/data['loyalitas'], data['loyalitas']/data['absensi'], data['loyalitas']/data['skill'], 1, data['loyalitas']/data['tanggung_jawab']],
        [1/data['tanggung_jawab'], data['tanggung_jawab']/data['absensi'], data['tanggung_jawab']/data['skill'], data['tanggung_jawab']/data['loyalitas'], 1],
    ])

    # Hitung eigenvalue dan eigenvector
    eigenvalues, eigenvectors = eig(pairwise_matrix)

    # Ambil eigenvector yang sesuai dengan eigenvalue maksimum
    max_eigenvalue_index = np.argmax(eigenvalues)
    weights = np.real(eigenvectors[:, max_eigenvalue_index])

    # Normalisasi bobot
    normalized_weights = weights / np.sum(weights)

    return normalized_weights[:5].tolist()  # Mengembalikan hanya 5 bobot relatif pertama





        


