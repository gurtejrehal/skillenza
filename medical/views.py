from django.shortcuts import render, render_to_response, reverse, redirect
from django.http import HttpResponse
from medical.forms import DetailsForm
from medical.models import Details
from django.db.models import Q

from urllib.request import urlopen, Request
# If you are using Python 3+, import urllib instead of urllib2

import json


def index(request):
    return render(request, 'medical/index.html')

def new_entry(request):
    form = DetailsForm()
    if request.method == 'POST':
        form = DetailsForm(request.POST)

        if form.is_valid():

            f = form.save(commit=False)
            f.save()
            return redirect(reverse('medical:dashboard', args=(f.id,)))
        else:
            print(form.errors)



    data = {

        "Inputs": {

            "input1":
                {
                    "ColumnNames": ["Age", "family_history-No", "family_history-Yes", "treatment", "work_interfere-NA",
                                    "work_interfere-Never", "work_interfere-Often", "work_interfere-Rarely",
                                    "work_interfere-Sometimes", "remote_work-No", "remote_work-Yes", "tech_company-No",
                                    "tech_company-Yes", "benefits-Don't know", "benefits-No", "benefits-Yes",
                                    "wellness_program-Don't know", "wellness_program-No", "wellness_program-Yes",
                                    "mental_health_interview-Maybe", "mental_health_interview-No",
                                    "mental_health_interview-Yes", "phys_health_interview-Maybe",
                                    "phys_health_interview-No", "phys_health_interview-Yes",
                                    "mental_vs_physical-Don't know", "mental_vs_physical-No", "mental_vs_physical-Yes",
                                    "obs_consequence-No", "obs_consequence-Yes"],
                    "Values": [
                        ["20", "0", "1", "1", "0", "1", "0", "0", "0", "0", "0", "1", "0", "0", "0", "0", "0", "0",
                         "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                        ["0", "0", "0", "1", "0", "0", "0", "0", "0", "0", "1", "0", "0", "0", "0", "0", "0", "0",
                         "0", "0", "0", "1", "0", "0", "1", "0", "0", "0", "0", "0"], ]
                }, },
        "GlobalParameters": {
        }
    }

    body = str.encode(json.dumps(data))

    url = 'https://ussouthcentral.services.azureml.net/workspaces/5394747c05f64a7faa25e1071778c8a6/services/8aa67e875713464e99662d93a9f5493a/execute?api-version=2.0&details=true'
    api_key = '8PAxwphpKvYiD81fNDaFWLUZTCXWnnJpCE+ZoO8ER3yXCjWEpmCbQ9Knkqa0PxQUTxbLlg1Tq5XpVA9PGlDvuw=='  # Replace this with the API key for the web service
    headers = {'Content-Type': 'application/json', 'Authorization': ('Bearer ' + api_key)}

    req = Request(url, body, headers)

    try:
        response = urlopen(req)

        # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
        # req = urllib.request.Request(url, body, headers)
        # response = urllib.request.urlopen(req)

        result = response.read()
        print(result)
    except :
        print("The request failed with status code: " )


    context_dict = {'form' :form}

    return render(request, 'medical/new_entry.html', context=context_dict)

def get_result(request):
    if request.method == 'POST':
        form = DetailsForm(request.POST)
        if form.is_valid():

            f = form.save(commit=False)
            f.save()

            return redirect(reverse('medical:dashboard', args=(f.id,)))
        else:
            print(form.errors)

    context_dict = {'form': form}
    return HttpResponse('cazz')



def search(request):

    if request.method == 'POST':
        query = str(request.POST['query'])
    else:
        query =""
    result = Details.objects.filter(Q(name__contains=query))
    context = {
        "result" : result
    }

    return render_to_response('medical/search.html', context=context)


def edit(request, acc_id):
    if acc_id:
        f = Details.objects.get(pk=acc_id)
    else:
        f = None

    if request.method == 'POST':  # If the form has been submitted...
        form = DetailsForm(request.POST, request.FILES, instance=f)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
            form.save()
            pass # Redirect after POST
    else:
        form = DetailsForm(instance=f)  # An unbound form

    context_dict={'form': form}
    return render(request, 'medical/new_entry.html', context=context_dict)


def dashboard(request, acc_id):
    user = Details.objects.get(pk=acc_id)
    context_dict = { 'user': user}
    return render(request, 'medical/dashboard.html', context=context_dict)
