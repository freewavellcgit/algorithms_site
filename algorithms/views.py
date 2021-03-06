from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic

from .models import Algorithm


def index(request):
    latest_algorithm_list = Algorithm.objects.order_by('-pub_date')[:5]
    context = {
        'latest_algorithm_list': latest_algorithm_list
    }
    return render(request, 'algorithms/index.html', context)


def detail(request, algorithm_id):
    algorithm = get_object_or_404(Algorithm, pk=algorithm_id)
    return render(request, 'algorithms/detail.html', {'algorithm': algorithm})



