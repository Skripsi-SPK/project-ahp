from django.urls import path, include
from .views import *

urlpatterns = [ 
    path('', dashboard, name='dashboard'),
    path('alternatif/',alternatif, name='data_alternatif'),
    path('tambah-alternatif/',tambah_alternatif, name='tambah_alternatif'),
    path('alternatif/lihat/<str:id>',lihat_alternatif, name='lihat_alternatif'),
    path('alternatif/edit/<str:id>',edit_alternatif, name='edit_alternatif'),
    path('alternatif/delete/<str:id>',delete_alternatif, name='delete_alternatif'),
    path('kriteria',kriteria, name='data_kriteria'),
    path('tambah-kriteria/',tambah_kriteria, name='tambah_kriteria'),
    path('kriteria/edit/<str:id>',edit_kriteria, name='edit_kriteria'),
    path('kriteria/delete/<str:id>',delete_kriteria, name='delete_kriteria'),
    path('sub-kriteria/',sub_kriteria, name='data_subkriteria'),
    path('tambah-sub-kriteria/',tambah_subkriteria, name='tambah_subkriteria'),
    path('subkriteria/edit/<str:id>',edit_subkriteria, name='edit_subkriteria'),
    path('subkriteria/delete/<str:id>',delete_subkriteria, name='delete_subkriteria'),
    path('data',data_kriteria, name='data_nilai'),
    path('tambah-nilai/',tambah_nilai, name='tambah_nilai'),
    path('data/edit/<str:id>',edit_data, name='edit_data'),
    path('data/delete/<str:id>',delete_data, name='delete_data'),
    path('perbandingan/',perbandingan, name='perbandingan kriteria'),
    path('rumus/',rumus, name='perbandingan alternatif'),
    path('hasil/',hasil, name='hasil perhitungan'),
   
]  


