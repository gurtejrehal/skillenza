from django.shortcuts import render
from django.http import HttpResponse
from medical.forms import DetailsForm

def index(request):
    form = DetailsForm()
    context_dict = {'form': form}
    return render(request, 'medical/index.html', context=context_dict)

def get_result(request):
    return HttpResponse('chode')