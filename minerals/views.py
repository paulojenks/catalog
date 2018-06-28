from django.shortcuts import render
from django.http import Http404

from minerals.models import Mineral


def minerals_list(request):
    """Generates list of all minerals in the entire catalog"""
    minerals = Mineral.objects.all()
    return render(request, 'minerals/index.html', {'minerals': minerals})


def mineral_detail(request, pk):
    """Gives all the non-empty details for each mineral"""
    try:
        mineral = Mineral.objects.filter(pk=pk).values('name', 'category', 'formula', 'strunz_classification',
                                                       'crystal_system', 'unit_cell', 'color', 'crystal_symmetry',
                                                       'cleavage', 'mohs_scale_hardness', 'luster', 'streak',
                                                       'diaphaneity', 'optical_properties', 'refractive_index',
                                                       'crystal_habit', 'specific_gravity', 'image_caption')
    except Mineral.DoesNotExist:
        raise Http404('You were looking for a rock, but you found a hard place.')
    try:
        mineral = mineral[0]
    except IndexError:
        raise Http404('You were looking for a rock, but you found a hard place.')
    return render(request, 'minerals/detail.html', {'mineral': mineral})
