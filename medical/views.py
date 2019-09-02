from django.shortcuts import render, render_to_response, reverse, redirect, get_object_or_404
from django.http import HttpResponse
from medical.forms import DetailsForm
from medical.models import Details
from django.db.models import Q
from django.conf import settings

import urllib
import json

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

            age = request.POST['age']
            gender = request.POST['gender']
            country = request.POST['country']
            state = request.POST['state']
            self_employment = request.POST['self_employment']
            family_history = request.POST['family_history']
            wellness = request.POST['wellness']
            seek_help = request.POST['seek_help']
            anonymity = request.POST['anonymity']
            leave = request.POST['leave']
            mental_health_consequence = request.POST['mental_health_consequence']
            phys_health_consequence = request.POST['phys_health_consequence']
            work_interfere = request.POST['work_interfere']
            no_of_employee = request.POST['no_of_employee']
            remote_work = request.POST['remote_work']
            benefits = request.POST['benefits']
            care_options = "yes"
            mental_vs_physical = request.POST['mental_vs_physical']
            tech_company = request.POST['tech_company']
            obs_consequence = request.POST['obs_consequence']
            mental_health_interview = request.POST['mental_health_interview']
            phys_health_interview = request.POST['phys_health_interview']

            f = form.save(commit=False)

            data = {
                        "Inputs": {
                            "input1": {
                                "ColumnNames": [
                                    "Age",
                                    "Gender",
                                    "Country",
                                    "state",
                                    "self_employed",
                                    "family_history",
                                    "treatment",
                                    "work_interfere",
                                    "no_employees",
                                    "remote_work",
                                    "tech_company",
                                    "benefits",
                                    "care_options",
                                    "wellness_program",
                                    "seek_help",
                                    "anonymity",
                                    "leave",
                                    "mental_health_consequence",
                                    "phys_health_consequence",
                                    "mental_health_interview",
                                    "phys_health_interview",
                                    "mental_vs_physical",
                                    "obs_consequence"
                                ],
                                "Values": [
                                    [
                                        age,
                                        gender,
                                        "United States",
                                        "IN",
                                        self_employment,
                                        family_history,
                                        "No",
                                        work_interfere,
                                        "1-6",
                                        remote_work,
                                        tech_company,
                                        benefits,
                                        care_options,
                                        wellness,
                                        seek_help,
                                        anonymity,
                                        leave,
                                        mental_health_consequence,
                                        phys_health_consequence,
                                        mental_health_interview,
                                        phys_health_interview,
                                        mental_vs_physical,
                                        obs_consequence
                                    ]
                                ]
                            }
                        },
                        "GlobalParameters": {}
                    }

            body = str.encode(json.dumps(data))

            url = 'https://ussouthcentral.services.azureml.net/workspaces/58fe8794f95e4427965cd2c78f62fd6f/services/c55151a5c7b645119790bb34e2f09f74/execute?api-version=2.0&details=true'
            api_key = str(settings.MICROSOFT_AZURE_API_KEY)  # Replace this with the API key for the web service
            headers = {'Content-Type': 'application/json', 'Authorization': ('Bearer ' + api_key)}

            req = urllib.request.Request(url, body, headers)

            try:
                req = urllib.request.Request(url, body, headers)
                response = urllib.request.urlopen(req)

                result = response.read()
                reply = json.loads(result)
                print("result",reply['Results']['output1']['value']['Values'][0][-2])
                f.treatment_required = str(reply['Results']['output1']['value']['Values'][0][-2])
            except Exception as e:
                print(e)



            f.save()

            return redirect(reverse('medical:dashboard', args=(f.id,)))
        else:
            print(form.errors)


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
    f = get_object_or_404(Details, pk=acc_id)
    form = DetailsForm(request.POST or None, instance=f)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('medical:dashboard', args=(f.id,)))

    context_dict={'form': form, 'user' : f}
    return render(request, 'medical/new_entry.html', context=context_dict)


def dashboard(request, acc_id):
    user = Details.objects.get(pk=acc_id)


    context_dict = { 'user': user, 'google_api' :  str(settings.GOOGLE_MAPS_API_KEY) }
    return render(request, 'medical/dashboard.html', context=context_dict)



