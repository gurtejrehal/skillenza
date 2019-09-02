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

    BOOLEAN_CHOICE = (
        ('yes', 'yes'),
        ('no', 'no')
    )

    name = forms.CharField(help_text="Your full name", max_length=128, widget=forms.TextInput(attrs={'placeholder': 'Full name'}))
    age = forms.IntegerField(initial=0)
    gender = forms.ChoiceField(required=True, widget=forms.RadioSelect(), choices=GENDER_CHOICES)
    country = forms.CharField(help_text="Country", max_length=128, widget=forms.TextInput(attrs={'placeholder': 'Country'}))
    state = forms.CharField(help_text="State", max_length=128, widget=forms.TextInput(attrs={'placeholder': 'State'}))

    self_employment = forms.ChoiceField(required=True, widget=forms.RadioSelect(), choices=BOOLEAN_CHOICE)
    family_history = forms.ChoiceField(required=True, widget=forms.RadioSelect(), choices=BOOLEAN_CHOICE)
    work_interfere = forms.ChoiceField(required=True, widget=forms.RadioSelect(), choices=WORK)
    no_of_employee = forms.IntegerField(required=False, initial=0)
    remote_work = forms.ChoiceField(required=True, widget=forms.RadioSelect(), choices=BOOLEAN_CHOICE)
    tech_company = forms.ChoiceField(required=True, widget=forms.RadioSelect(), choices=BOOLEAN_CHOICE)

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
    obs_consequence = forms.ChoiceField(required=True, widget=forms.RadioSelect(), choices=BOOLEAN_CHOICE)



    class Meta:
        model = Details
        exclude = ('treatment_required',)