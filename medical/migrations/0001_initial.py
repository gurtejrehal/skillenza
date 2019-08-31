# Generated by Django 2.2.4 on 2019-08-31 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('age', models.IntegerField(default=0)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=25)),
                ('country', models.CharField(default='', max_length=25)),
                ('state', models.CharField(default='', max_length=25)),
                ('self_employment', models.BooleanField()),
                ('family_history', models.BooleanField()),
                ('treatment', models.BooleanField()),
                ('work_interfere', models.CharField(default='', max_length=25)),
                ('no_of_employee', models.IntegerField(default=0)),
                ('remote_work', models.BooleanField()),
                ('tech_company', models.BooleanField()),
                ('benefits', models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('dont_know', "Don't Know"), ('maybe', 'Maybe')], max_length=25)),
                ('wellness', models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('dont_know', "Don't Know"), ('maybe', 'Maybe')], max_length=25)),
                ('seek_help', models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('dont_know', "Don't Know"), ('maybe', 'Maybe')], max_length=25)),
                ('anonymity', models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('dont_know', "Don't Know"), ('maybe', 'Maybe')], max_length=25)),
                ('leave', models.CharField(choices=[('somewhat_easy', 'Somewhat easy'), ('somewhat difficult', 'Somewhat difficult'), ('dont_know', "Don't Know"), ('very_easy', 'Very Easy')], max_length=25)),
                ('mental_health_consequence', models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('dont_know', "Don't Know"), ('maybe', 'Maybe')], max_length=25)),
                ('phys_health_consequence', models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('dont_know', "Don't Know"), ('maybe', 'Maybe')], max_length=25)),
                ('mental_health_interview', models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('dont_know', "Don't Know"), ('maybe', 'Maybe')], max_length=25)),
                ('phys_health_interview', models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('dont_know', "Don't Know"), ('maybe', 'Maybe')], max_length=25)),
                ('mental_vs_physical', models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('dont_know', "Don't Know"), ('maybe', 'Maybe')], max_length=25)),
                ('obs_consequence', models.BooleanField()),
            ],
        ),
    ]
