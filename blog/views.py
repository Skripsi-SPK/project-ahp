from re import template
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Alternatif, Divisi, Kriteria, SubKriteria, DataKriteria, Criteria, Comparison, SubCriteria, Perbandingan
from .forms import AlternatifForms, KriteriaForms, SubkriteriaForms, DataKriteriaForms, ComparisonForm, PerbandinganForm

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
def hasil(request):
    template_name = "dashboard/hasil perhitungan.html"
    context ={
        'title': 'hasil perhitungan'
    }
    return render(request, template_name, context)



#def perbandingan_kriteria(request):
    template_name = "dashboard/perbandingan_kriteria.html"
    ratio_index_saaty = np.array([0, 0, 0.58, 0.9, 1.12, 1.24, 1.32, 1.41, 1.46, 1.49])

    # data_kriteria = ["saputra", 12, 1212, 1222]
    # print(data_kriteria[0])
    berpasangan = matriks_perbandingan_berpasangan()
    print(berpasangan.shape)

    p_total = np.sum(berpasangan, axis=0)
    p_priority = berpasangan / p_total
    p_priority_weight = np.mean(p_priority, axis=1)
    p_consistency = np.dot(berpasangan, p_priority_weight) / p_priority_weight
    print(p_consistency)
    n = berpasangan.shape[0]
    lambda_max = np.mean(p_consistency)

    RI = ratio_index_saaty[n]
    CI = (lambda_max - n) / (n - 1)
    CR = CI / RI
    print(CR)


    # print(berpasangan)
    context = {
        "title":"perbandingan kriteria",
    }
    return render(request, template_name, context)


#def matriks_perbandingan_berpasangan():
    p_criteria = np.array([
        [1,     1,   5,   3,   5],
        [1,     1,   5,   3,   5],
        [1/5, 1/5,   1,   1/3, 1],
        [1/3, 1/3,   3,   1,   3],
        [1/5, 1/5,   1, 1/3,   1]
    ])
    return p_criteria





###########################################################################
# ratio_index_saaty = np.array([0, 0, 0.58, 0.9, 1.12, 1.24, 1.32, 1.41, 1.46, 1.49])
# perbandinqan antar kriteria
# p_criteria = np.array([
#     [1,     1,   5,   3,   5],
#     [1,     1,   5,   3,   5],
#     [1/5, 1/5,   1,   1/3, 1],
#     [1/3, 1/3,   3,   1,   3],
#     [1/5, 1/5,   1, 1/3,   1]
# ])
# print(p_criteria.shape)
# # vektor total untuk semua baris (axis=0)
# p_total = np.sum(p_criteria, axis=0)
# print(p_total)
# # matriks normalisasi
# p_priority = p_criteria / p_total
# print(p_priority)
# # vektor bobot prioritas
# p_priority_weight = np.mean(p_priority, axis=1)
# print(p_priority_weight)

# p_consistency = np.dot(p_criteria, p_priority_weight) / p_priority_weight
# print(p_consistency)

# n = p_criteria.shape[0]
# lambda_max = np.mean(p_consistency)

# RI = ratio_index_saaty[n]
# CI = (lambda_max - n) / (n - 1)
# CR = CI / RI

# # Konsisten apabila 0 < CR < 0.1 
# print(CR)


        


