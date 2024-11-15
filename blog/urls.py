from django.urls import path, include
from .views_new import *

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
    path('perbandingan/',perbandingan_kriteria, name='perbandingan_kriteria'),
    path('perbandingan/delete/<str:id>',delete_perbandingan, name='delete_perbandingan'),
    path('perbandingan-subkriteria-absensi/',perbandingan_subkriteria_absensi, name='perbandingan_subkriteria_absensi'),
    path('perbandingan-absensi/delete/<str:id>',delete_perbandingan_absensi, name='delete_perbandingan_absensi'),
    path('perbandingan-subkriteria-skill/',perbandingan_subkriteria_skill, name='perbandingan_subkriteria_skill'),
    path('perbandingan-skill/delete/<str:id>',delete_perbandingan_skill, name='delete_perbandingan_skill'),
    path('perbandingan-subkriteria-tanggungjawab/',perbandingan_subkriteria_tanggungjawab, name='perbandingan_subkriteria_tanggungjawab'),
    path('perbandingan-subkriteria-tanggungjawab/delete/<str:id>',delete_perbandingan_tanggungjawab, name='delete_perbandingan_tanggungjawab'),
    path('perbandingan-subkriteria-loyalitas/',perbandingan_subkriteria_loyalitas, name='perbandingan_subkriteria_loyalitas'),
    path('perbandingan-subkriteria-loyalitas/delete/<str:id>',delete_perbandingan_loyalitas, name='delete_perbandingan_loyalitas'),
    path('perbandingan-subkriteria-pelanggaran/',perbandingan_subkriteria_pelanggaran, name='perbandingan_subkriteria_pelanggaran'),
    path('perbandingan-subkriteria-pelanggaran/delete/<str:id>',delete_perbandingan_pelanggaran, name='delete_perbandingan_pelanggaran'),
    path('penilaian/',hasil_penilaian, name='hasil_penilaian'),
    path('penilaian/detail/<int:hasil_id>',detail_penilaian, name='detail_penilaian'),
    path('edit-penilaian/<int:hasil_id>/', edit_penilaian, name='edit_penilaian'),
    path('delete-penilaian/<int:hasil_id>/',  delete_penilaian, name='delete_penilaian'),
    path('subcriteria/',sub_criteria, name='sub_criteria'),
    
    
    
   
] 