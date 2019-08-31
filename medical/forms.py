from django import forms
from medical.models import Details

class DetailsForm(forms.ModelForm):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )

    OPTIONS = (
        ('yes', 'Yes'),
        ('no', 'No'),
        ('dont_know', 'Don\'t Know'),
        ('maybe', 'Maybe')
    )

    WORK = (
        ('often', 'Often'),
        ('rarely', 'Rarely'),
        ('sometimes', 'Sometimes'),
        ('never', 'Never')
    )

    DIFFICULTY = (
        ('somewhat_easy', 'Somewhat easy'),
        ('somewhat difficult', 'Somewhat difficult'),
        ('dont_know', 'Don\'t Know'),
        ('very_easy', 'Very Easy')
    )

    name = forms.CharField(help_text="Your full name", max_length=128, widget=forms.TextInput(attrs={'placeholder': 'Full name'}))
    age = forms.IntegerField(initial=0)
    gender = forms.ChoiceField(required=True, widget=forms.RadioSelect(), choices=GENDER_CHOICES)
    country = forms.CharField(help_text="Country", max_length=128, widget=forms.TextInput(attrs={'placeholder': 'Country'}))
    state = forms.CharField(help_text="State", max_length=128, widget=forms.TextInput(attrs={'placeholder': 'State'}))

    self_employment = forms.BooleanField(required=True, initial=False)
    family_history = forms.BooleanField(required=True, initial=False)
    work_interfere = forms.ChoiceField(required=True, widget=forms.RadioSelect(), choices=WORK)
    no_of_employee = forms.IntegerField(initial=0)
    remote_work = forms.BooleanField(required=True, initial=False)
    tech_company = forms.BooleanField(required=True, initial=False)

    benefits = forms.ChoiceField(required=True, widget=forms.RadioSelect(), choices=OPTIONS)
    wellness = forms.ChoiceField(required=True, widget=forms.RadioSelect(), choices=OPTIONS)
    seek_help = forms.ChoiceField(required=True, widget=forms.RadioSelect(), choices=OPTIONS)
    anonymity = forms.ChoiceField(required=True, widget=forms.RadioSelect(), choices=OPTIONS)
    leave = forms.ChoiceField(required=True, widget=forms.RadioSelect(), choices=DIFFICULTY)

    mental_health_consequence = forms.ChoiceField(required=True, widget=forms.RadioSelect(), choices=OPTIONS)
    phys_health_consequence = forms.ChoiceField(required=True, widget=forms.RadioSelect(), choices=OPTIONS)
    mental_health_interview = forms.ChoiceField(required=True, widget=forms.RadioSelect(), choices=OPTIONS)
    phys_health_interview = forms.ChoiceField(required=True, widget=forms.RadioSelect(), choices=OPTIONS)
    mental_vs_physical = forms.ChoiceField(required=True, widget=forms.RadioSelect(), choices=OPTIONS)
    obs_consequence = forms.BooleanField(required=True, initial=False)



    class Meta:
        model = Details
        exclude = ('treatment_required',)