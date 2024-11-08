from re import template
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Alternatif, Divisi, Kriteria, SubKriteria, DataKriteria, Criteria, Comparison, SubCriteria, Perbandingan, SubCriterion, Criterion, Total, Perhitungan, Alternative
from .forms import AlternatifForms, KriteriaForms, SubkriteriaForms, DataKriteriaForms, ComparisonForm, PerbandinganForm, PerhitunganForm

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
def perbandingan_kriteria(request):
    template_name = "dashboard/perbandingan_kriteria.html"
     # Predefined criteria
    criteria_names = ['Absensi', 'Skill', 'Tanggung Jawab', 'Loyalitas', 'Pelanggaran']
    
    # Create or get criteria from database
    for name in criteria_names:
        Criteria.objects.get_or_create(name=name)

    if request.method == 'POST':
        comparison_form = ComparisonForm(request.POST)
        if comparison_form.is_valid():
            comparison_form.save()
            return redirect(perbandingan_kriteria)  # Redirect after saving
    else:
        comparison_form = ComparisonForm()

    criteria = Criteria.objects.all()
    comparisons = Comparison.objects.all()

    # Calculate weights if there are enough comparisons
    weights = {}
    consistency_ratio = None
    consistency_index = None
    lambda_max = None

    if comparisons.count() > 0:
        n = len(criteria)
        matrix = np.ones((n, n))

        for comp in comparisons:
            i = list(criteria).index(comp.criteria1)
            j = list(criteria).index(comp.criteria2)
            matrix[i][j] = comp.value
            matrix[j][i] = 1 / comp.value

        # Calculate weights using AHP
        weights_raw = matrix.sum(axis=0)
        weights_normalized = weights_raw / weights_raw.sum()
        
        for i, criteria in enumerate(criteria):
            weights[criteria.name] = round(weights_normalized[i], 4)
        
        #Calculate lambda_max (principal eigenvalue)
        weighted_matrix = np.dot(matrix, weights_normalized)  # Multiply matrix by priority vector
        lambda_max = np.mean(weighted_matrix / weights_normalized)  # Calculate λmax

        # Calculate Consistency Index (CI) and Consistency Ratio (CR)
        #principal_eigenvalue = np.mean(np.dot(matrix, weights_normalized) / weights_normalized)
        # consistency_index = (lambda_max - n) / (n - 1)

        # Random Index (RI) values based on matrix size
        random_index_values = {
            1: 0.00,
            2: 0.00,
            3: 0.58,
            4: 0.90,
            5: 1.12,
            6: 1.24,
            7: 1.32,
            8: 1.41,
            9: 1.45,
            10: 1.49
        }
        
        #random_index = random_index_values.get(n, 5)
        
        #if random_index is not None:
            #consistency_ratio = consistency_index / random_index 
    context ={
        'form': comparison_form,
        'criteria': criteria,
        'comparisons':comparisons,
        'weights': weights,
        #'lambda_max': lambda_max,
        #'random_index_values':random_index_values,
        # Pass λmax to the template
        #'consistency_index': consistency_index,
        #'consistency_ratio': consistency_ratio,
        
    }
    return render(request ,template_name, context)

@login_required
def delete_perbandingan(request, id):
    Comparison.objects.get(id=id).delete()
    return redirect(perbandingan_kriteria)

@login_required
def perbandingan_subkriteria_absensi(request):
    template_name = "dashboard/perbandingan_subkriteria_absensi.html"
     # Predefined subcriteria
    subcriteria_names = ['Sangat Baik', 'Baik', 'Cukup Baik', 'Kurang Baik', 'Buruk']
    
    # Create or get criteria from database
    for name in subcriteria_names:
        SubCriteria.objects.get_or_create(name=name)

    if request.method == 'POST':
        perbandingan_form = PerbandinganForm(request.POST)
        if perbandingan_form.is_valid():
            perbandingan_form.save()
            return redirect(perbandingan_subkriteria_absensi)  # Redirect after saving
    else:
        perbandingan_form = PerbandinganForm()

    subcriteria = SubCriteria.objects.all()
    perbandingan = Perbandingan.objects.all()

    # Calculate weights if there are enough comparisons
    weights = {}
    consistency_ratio = None
    consistency_index = None
    lambda_max = None

    if perbandingan.count() > 0:
        n = len(subcriteria)
        matrix = np.ones((n, n))

        for perb in perbandingan:
            i = list(subcriteria).index(perb.subcriteria1)
            j = list(subcriteria).index(perb.subcriteria2)
            matrix[i][j] = perb.value
            matrix[j][i] = 1 / perb.value

        # Calculate weights using AHP
        weights_raw = matrix.sum(axis=0)
        weights_normalized = weights_raw / weights_raw.sum()
        
        for i, subcriteria in enumerate(subcriteria):
            weights[subcriteria.name] = round(weights_normalized[i], 4)
        
        #Calculate lambda_max (principal eigenvalue)
        weighted_matrix = np.dot(matrix, weights_normalized)  # Multiply matrix by priority vector
        lambda_max = np.mean(weighted_matrix / weights_normalized)  # Calculate λmax

        # Calculate Consistency Index (CI) and Consistency Ratio (CR)
        #principal_eigenvalue = np.mean(np.dot(matrix, weights_normalized) / weights_normalized)
        # consistency_index = (lambda_max - n) / (n - 1)

        # Random Index (RI) values based on matrix size
        random_index_values = {
            1: 0.00,
            2: 0.00,
            3: 0.58,
            4: 0.90,
            5: 1.12,
            6: 1.24,
            7: 1.32,
            8: 1.41,
            9: 1.45,
            10: 1.49
        }
        
        #random_index = random_index_values.get(n, 5)
        
        #if random_index is not None:
            #consistency_ratio = consistency_index / random_index 
    context ={
        'form': perbandingan_form,
        'subcriteria': subcriteria,
        'perbandingan':perbandingan,
        'weights': weights,
        #'lambda_max': lambda_max,
        #'random_index_values':random_index_values,
        # Pass λmax to the template
        #'consistency_index': consistency_index,
        #'consistency_ratio': consistency_ratio,
        
    }
    return render(request ,template_name, context)

@login_required
def delete_perbandingan_absensi(request, id):
    Perbandingan.objects.get(id=id).delete()
    return redirect(perbandingan_subkriteria_absensi)

def perbandingan_subkriteria_skill(request):
    template_name = "dashboard/perbandingan_subkriteria_skill.html"
     # Predefined subcriteria
    subcriteria_names = ['Sangat Baik', 'Baik', 'Cukup Baik', 'Kurang Baik', 'Buruk']
    
    # Create or get criteria from database
    for name in subcriteria_names:
        SubCriteria.objects.get_or_create(name=name)

    if request.method == 'POST':
        perbandingan_form = PerbandinganForm(request.POST)
        if perbandingan_form.is_valid():
            perbandingan_form.save()
            return redirect(perbandingan_subkriteria_skill)  # Redirect after saving
    else:
        perbandingan_form = PerbandinganForm()

    subcriteria = SubCriteria.objects.all()
    perbandingan = Perbandingan.objects.all()

    # Calculate weights if there are enough comparisons
    weights = {}
    consistency_ratio = None
    consistency_index = None
    lambda_max = None

    if perbandingan.count() > 0:
        n = len(subcriteria)
        matrix = np.ones((n, n))

        for comp in perbandingan:
            i = list(subcriteria).index(comp.subcriteria1)
            j = list(subcriteria).index(comp.subcriteria2)
            matrix[i][j] = comp.value
            matrix[j][i] = 1 / comp.value

        # Calculate weights using AHP
        weights_raw = matrix.sum(axis=0)
        weights_normalized = weights_raw / weights_raw.sum()
        
        for i, subcriteria in enumerate(subcriteria):
            weights[subcriteria.name] = round(weights_normalized[i], 4)
        
        #Calculate lambda_max (principal eigenvalue)
        weighted_matrix = np.dot(matrix, weights_normalized)  # Multiply matrix by priority vector
        lambda_max = np.mean(weighted_matrix / weights_normalized)  # Calculate λmax

        # Calculate Consistency Index (CI) and Consistency Ratio (CR)
        #principal_eigenvalue = np.mean(np.dot(matrix, weights_normalized) / weights_normalized)
        # consistency_index = (lambda_max - n) / (n - 1)

        # Random Index (RI) values based on matrix size
        random_index_values = {
            1: 0.00,
            2: 0.00,
            3: 0.58,
            4: 0.90,
            5: 1.12,
            6: 1.24,
            7: 1.32,
            8: 1.41,
            9: 1.45,
            10: 1.49
        }
        
        #random_index = random_index_values.get(n, 5)
        
        #if random_index is not None:
            #consistency_ratio = consistency_index / random_index 
    context ={
        'form': perbandingan_form,
        'subcriteria': subcriteria,
        'perbandingan':perbandingan,
        'weights': weights,
        #'lambda_max': lambda_max,
        #'random_index_values':random_index_values,
        # Pass λmax to the template
        #'consistency_index': consistency_index,
        #'consistency_ratio': consistency_ratio,
        
    }
    return render(request ,template_name, context)

@login_required
def delete_perbandingan_skill(request, id):
    Perbandingan.objects.get(id=id).delete()
    return redirect(perbandingan_subkriteria_skill)

def perbandingan_subkriteria_tanggungjawab(request):
    template_name = "dashboard/perbandingan_subkriteria_tanggungjawab.html"
     # Predefined subcriteria
    subcriteria_names = ['Sangat Baik', 'Baik', 'Cukup Baik', 'Kurang Baik', 'Buruk']
    
    # Create or get criteria from database
    for name in subcriteria_names:
        SubCriteria.objects.get_or_create(name=name)

    if request.method == 'POST':
        perbandingan_form = PerbandinganForm(request.POST)
        if perbandingan_form.is_valid():
            perbandingan_form.save()
            return redirect(perbandingan_subkriteria_tanggungjawab)  # Redirect after saving
    else:
        perbandingan_form = PerbandinganForm()

    subcriteria = SubCriteria.objects.all()
    perbandingan = Perbandingan.objects.all()

    # Calculate weights if there are enough comparisons
    weights = {}
    consistency_ratio = None
    consistency_index = None
    lambda_max = None

    if perbandingan.count() > 0:
        n = len(subcriteria)
        matrix = np.ones((n, n))

        for comp in perbandingan:
            i = list(subcriteria).index(comp.subcriteria1)
            j = list(subcriteria).index(comp.subcriteria2)
            matrix[i][j] = comp.value
            matrix[j][i] = 1 / comp.value

        # Calculate weights using AHP
        weights_raw = matrix.sum(axis=0)
        weights_normalized = weights_raw / weights_raw.sum()
        
        for i, subcriteria in enumerate(subcriteria):
            weights[subcriteria.name] = round(weights_normalized[i], 4)
        
        #Calculate lambda_max (principal eigenvalue)
        weighted_matrix = np.dot(matrix, weights_normalized)  # Multiply matrix by priority vector
        lambda_max = np.mean(weighted_matrix / weights_normalized)  # Calculate λmax

        # Calculate Consistency Index (CI) and Consistency Ratio (CR)
        #principal_eigenvalue = np.mean(np.dot(matrix, weights_normalized) / weights_normalized)
        # consistency_index = (lambda_max - n) / (n - 1)

        # Random Index (RI) values based on matrix size
        random_index_values = {
            1: 0.00,
            2: 0.00,
            3: 0.58,
            4: 0.90,
            5: 1.12,
            6: 1.24,
            7: 1.32,
            8: 1.41,
            9: 1.45,
            10: 1.49
        }
        
        #random_index = random_index_values.get(n, 5)
        
        #if random_index is not None:
            #consistency_ratio = consistency_index / random_index 
    context ={
        'form': perbandingan_form,
        'subcriteria': subcriteria,
        'perbandingan':perbandingan,
        'weights': weights,
        #'lambda_max': lambda_max,
        #'random_index_values':random_index_values,
        # Pass λmax to the template
        #'consistency_index': consistency_index,
        #'consistency_ratio': consistency_ratio,
        
    }
    return render(request ,template_name, context)

@login_required
def delete_perbandingan_tanggungjawab(request, id):
    Perbandingan.objects.get(id=id).delete()
    return redirect(perbandingan_subkriteria_tanggungjawab)

@login_required
def perbandingan_subkriteria_loyalitas(request):
    template_name = "dashboard/perbandingan_subkriteria_loyalitas.html"
     # Predefined subcriteria
    subcriteria_names = ['Sangat Baik', 'Baik', 'Cukup Baik', 'Kurang Baik', 'Buruk']
    
    # Create or get criteria from database
    for name in subcriteria_names:
        SubCriteria.objects.get_or_create(name=name)

    if request.method == 'POST':
        perbandingan_form = PerbandinganForm(request.POST)
        if perbandingan_form.is_valid():
            perbandingan_form.save()
            return redirect(perbandingan_subkriteria_loyalitas)  # Redirect after saving
    else:
        perbandingan_form = PerbandinganForm()

    subcriteria = SubCriteria.objects.all()
    perbandingan = Perbandingan.objects.all()

    # Calculate weights if there are enough comparisons
    weights = {}
    consistency_ratio = None
    consistency_index = None
    lambda_max = None

    if perbandingan.count() > 0:
        n = len(subcriteria)
        matrix = np.ones((n, n))

        for comp in perbandingan:
            i = list(subcriteria).index(comp.subcriteria1)
            j = list(subcriteria).index(comp.subcriteria2)
            matrix[i][j] = comp.value
            matrix[j][i] = 1 / comp.value

        # Calculate weights using AHP
        weights_raw = matrix.sum(axis=0)
        weights_normalized = weights_raw / weights_raw.sum()
        
        for i, subcriteria in enumerate(subcriteria):
            weights[subcriteria.name] = round(weights_normalized[i], 4)
        
        #Calculate lambda_max (principal eigenvalue)
        weighted_matrix = np.dot(matrix, weights_normalized)  # Multiply matrix by priority vector
        lambda_max = np.mean(weighted_matrix / weights_normalized)  # Calculate λmax

        # Calculate Consistency Index (CI) and Consistency Ratio (CR)
        #principal_eigenvalue = np.mean(np.dot(matrix, weights_normalized) / weights_normalized)
        # consistency_index = (lambda_max - n) / (n - 1)

        # Random Index (RI) values based on matrix size
        random_index_values = {
            1: 0.00,
            2: 0.00,
            3: 0.58,
            4: 0.90,
            5: 1.12,
            6: 1.24,
            7: 1.32,
            8: 1.41,
            9: 1.45,
            10: 1.49
        }
        
        #random_index = random_index_values.get(n, 5)
        
        #if random_index is not None:
            #consistency_ratio = consistency_index / random_index 
    context ={
        'form': perbandingan_form,
        'subcriteria': subcriteria,
        'perbandingan':perbandingan,
        'weights': weights,
        #'lambda_max': lambda_max,
        #'random_index_values':random_index_values,
        # Pass λmax to the template
        #'consistency_index': consistency_index,
        #'consistency_ratio': consistency_ratio,
        
    }
    return render(request ,template_name, context)

@login_required
def delete_perbandingan_loyalitas(request, id):
    Perbandingan.objects.get(id=id).delete()
    return redirect(perbandingan_subkriteria_loyalitas)

def perbandingan_subkriteria_pelanggaran(request):
    template_name = "dashboard/perbandingan_subkriteria_pelanggaran.html"
     # Predefined subcriteria
    subcriteria_names = ['Sangat Baik', 'Baik', 'Cukup Baik', 'Kurang Baik', 'Buruk']
    
    # Create or get criteria from database
    for name in subcriteria_names:
        SubCriteria.objects.get_or_create(name=name)

    if request.method == 'POST':
        perbandingan_form = PerbandinganForm(request.POST)
        if perbandingan_form.is_valid():
            perbandingan_form.save()
            return redirect(perbandingan_subkriteria_pelanggaran)  # Redirect after saving
    else:
        perbandingan_form = PerbandinganForm()

    subcriteria = SubCriteria.objects.all()
    perbandingan = Perbandingan.objects.all()

    # Calculate weights if there are enough comparisons
    weights = {}
    consistency_ratio = None
    consistency_index = None
    lambda_max = None

    if perbandingan.count() > 0:
        n = len(subcriteria)
        matrix = np.ones((n, n))

        for comp in perbandingan:
            i = list(subcriteria).index(comp.subcriteria1)
            j = list(subcriteria).index(comp.subcriteria2)
            matrix[i][j] = comp.value
            matrix[j][i] = 1 / comp.value

        # Calculate weights using AHP
        weights_raw = matrix.sum(axis=0)
        weights_normalized = weights_raw / weights_raw.sum()
        
        for i, subcriteria in enumerate(subcriteria):
            weights[subcriteria.name] = round(weights_normalized[i], 4)
        
        #Calculate lambda_max (principal eigenvalue)
        weighted_matrix = np.dot(matrix, weights_normalized)  # Multiply matrix by priority vector
        lambda_max = np.mean(weighted_matrix / weights_normalized)  # Calculate λmax

        # Calculate Consistency Index (CI) and Consistency Ratio (CR)
        #principal_eigenvalue = np.mean(np.dot(matrix, weights_normalized) / weights_normalized)
        # consistency_index = (lambda_max - n) / (n - 1)

        # Random Index (RI) values based on matrix size
        random_index_values = {
            1: 0.00,
            2: 0.00,
            3: 0.58,
            4: 0.90,
            5: 1.12,
            6: 1.24,
            7: 1.32,
            8: 1.41,
            9: 1.45,
            10: 1.49
        }
        
        #random_index = random_index_values.get(n, 5)
        
        #if random_index is not None:
            #consistency_ratio = consistency_index / random_index 
    context ={
        'form': perbandingan_form,
        'subcriteria': subcriteria,
        'perbandingan':perbandingan,
        'weights': weights,
        #'lambda_max': lambda_max,
        #'random_index_values':random_index_values,
        # Pass λmax to the template
        #'consistency_index': consistency_index,
        #'consistency_ratio': consistency_ratio,
        
    }
    return render(request ,template_name, context)

@login_required
def delete_perbandingan_pelanggaran(request, id):
    Perbandingan.objects.get(id=id).delete()
    return redirect(perbandingan_subkriteria_pelanggaran)

@login_required
def hasil_penilaian(request):
    template_name = "dashboard/hasil_penilaian.html"
    alternatifs = Alternative.objects.all()
    kriterias = Criterion.objects.all()

    if request.method == 'POST':
        try:
            # Proses input penilaian
            for alternatif in alternatifs:
                for kriteria in kriterias:
                    field_name = f'penilaian_{alternatif.id}_{kriteria.id}'
                    sub_kriteria_id = request.POST.get(field_name)
                    
                    if sub_kriteria_id:
                        sub_kriteria = SubCriterion.objects.get(id=sub_kriteria_id)
                        Perhitungan.objects.update_or_create(
                            alternatif=alternatif,
                            kriteria=kriteria,
                            defaults={'sub_kriteria': sub_kriteria}
                        )

            # Hitung matrix penilaian
            hasil_matrix = np.zeros((len(alternatifs), len(kriterias)))
            
            for i, alternatif in enumerate(alternatifs):
                for j, kriteria in enumerate(kriterias):
                    penilaian = Perhitungan.objects.filter(
                        alternatif=alternatif,
                        kriteria=kriteria
                    ).first()
                    
                    if penilaian:
                        nilai_subkriteria = penilaian.sub_kriteria.bobot
                        bobot_kriteria = kriteria.bobot
                        hasil_matrix[i][j] = nilai_subkriteria * bobot_kriteria

            # Hitung nilai akhir
            nilai_akhir = np.sum(hasil_matrix, axis=1)
            
            # Update atau buat hasil AHP
            Total.objects.all().delete()  # Hapus hasil sebelumnya
            
            # Buat ranking
            ranking = np.argsort(-nilai_akhir)  # Descending order
            
            # Simpan hasil
            for rank, idx in enumerate(ranking, 1):
                Total.objects.create(
                    alternatif=alternatifs[idx],
                    nilai_akhir=float(nilai_akhir[idx]),
                    ranking=rank
                )
            
            return redirect(hasil_penilaian)
        
        except Exception as e:
            print(f"Error: {e}")
            messages.error(request, f"Terjadi kesalahan: {str(e)}")

    # Kode untuk GET request
    penilaian_dict = get_penilaian_dict(alternatifs, kriterias)
    hasil_ahp = Total.objects.all().order_by('ranking')

    context = {
        'title': 'Penilaian Alternatif',
        'alternatif': alternatifs,
        'kriteria': kriterias,
        'penilaian_dict': penilaian_dict,
        'hasil_ahp': hasil_ahp,
    }

    return render(request, template_name, context)

def get_penilaian_dict(alternatifs, kriterias):
    penilaian_dict = {}
    for alternatif in alternatifs:
        penilaian_dict[alternatif.id] = {}
        for kriteria in kriterias:
            penilaian = Perhitungan.objects.filter(
                alternatif=alternatif,
                kriteria=kriteria
            ).first()
            penilaian_dict[alternatif.id][kriteria.id] = penilaian
    return penilaian_dict

def detail_penilaian(request, hasil_id):
    template_name = "dashboard/detail_penilaian.html"
    try:
        hasil = Total.objects.get(id=hasil_id)
        alternatif = hasil.alternatif
        penilaians = Perhitungan.objects.filter(alternatif=alternatif)
        
        detail_matrix = []
        total_nilai = 0
        
        for penilaian in penilaians:
            nilai = penilaian.sub_kriteria.bobot * penilaian.kriteria.bobot
            detail_matrix.append({
                'kriteria': penilaian.kriteria.nama,
                'sub_kriteria': penilaian.sub_kriteria.nama,
                'bobot_kriteria': penilaian.kriteria.bobot,
                'bobot_sub_kriteria': penilaian.sub_kriteria.bobot,
                'nilai': nilai
            })
            total_nilai += nilai
        
        context = {
            'title': f'Detail Penilaian - {alternatif.nama}',
            'hasil': hasil,
            'detail_matrix': detail_matrix,
            'total_nilai': total_nilai
        }
        
        return render(request, template_name, context)
    
    except Total.DoesNotExist:
        messages.error(request, 'Data hasil tidak ditemukan')
        return redirect(hasil_penilaian)
    
@login_required
def hapus_penilaian(request, alternatif_id):
    if request.method == 'POST':
        try:
            Perhitungan.objects.filter(alternatif_id=alternatif_id).delete()
            Total.objects.filter(alternatif_id=alternatif_id).delete()
            
        except Exception as e:
    
            return redirect(hapus_penilaian)

@login_required
# View untuk mengatur ulang semua penilaian
def reset_penilaian(request):
    if request.method == 'POST':
        try:
            Perhitungan.objects.all().delete()
            Total.objects.all().delete()
           
        except Exception as e:

            return redirect(reset_penilaian)

def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        self.hitung_ahp()
    
    

@login_required
#def hasil(request):
   # template_name = "dashboard/hasil_perhitungan.html"
    #hasil = HasilAHP.objects.all().order_by('ranking')
    #return render(request, template_name, context={'hasil': hasil})
  
def load_subkriteria(request):
    KeyError = ('kriteria')


        


