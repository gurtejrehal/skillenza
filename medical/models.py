from django.db import models
from django import forms

class Details(models.Model):
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

    # gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect())
    name = models.CharField(max_length=25)
    age = models.IntegerField(default=0)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=25)
    country = models.CharField(default='', max_length=25)
    state = models.CharField(default='', max_length=25)
    self_employment = models.BooleanField()
    family_history = models.BooleanField()
    work_interfere = models.CharField(default='', max_length=25, choices=WORK)
    no_of_employee = models.IntegerField(default=0)
    remote_work = models.BooleanField()
    tech_company = models.BooleanField()
    benefits = models.CharField(choices=OPTIONS, max_length=25)
    wellness = models.CharField(choices=OPTIONS, max_length=25)
    seek_help = models.CharField(choices=OPTIONS, max_length=25)
    anonymity = models.CharField(choices=OPTIONS, max_length=25)
    leave = models.CharField(choices=DIFFICULTY, max_length=25)
    mental_health_consequence = models.CharField(choices=OPTIONS, max_length=25)
    phys_health_consequence = models.CharField(choices=OPTIONS, max_length=25)
    mental_health_interview = models.CharField(choices=OPTIONS, max_length=25)
    phys_health_interview = models.CharField(choices=OPTIONS, max_length=25)
    mental_vs_physical = models.CharField(choices=OPTIONS, max_length=25)
    obs_consequence = models.BooleanField()
    treatment_required = models.CharField(default='', max_length=5)

    class Meta:
        verbose_name_plural = 'Details'

    def __str__(self):
        return self.name






