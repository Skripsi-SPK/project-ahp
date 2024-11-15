from django import template
from django.db.models import Avg

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def average_nilai(hasil_ahp):
    """
    Filter untuk menghitung rata-rata nilai akhir
    """
    try:
        return hasil_ahp.aggregate(Avg('nilai_akhir'))['nilai_akhir__avg']
    except:
        return 0