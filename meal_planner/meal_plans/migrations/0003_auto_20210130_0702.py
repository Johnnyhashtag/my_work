# Generated by Django 3.1.5 on 2021-01-30 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal_plans', '0002_auto_20210130_0633'),
    ]

    operations = [
        migrations.AddField(
            model_name='weekdays',
            name='session_of_day',
            field=models.CharField(choices=[('BFAST', 'Breakfast'), ("L'NCH", 'Lunch'), ("D'NNER", 'Dinner'), ("D'SERT", 'Dessert')], default='BFAST', max_length=9),
        ),
        migrations.AlterField(
            model_name='weekdays',
            name='days_of_the_week',
            field=models.CharField(choices=[('SUN', 'Sunday'), ('MON', 'Monday'), ('TUE', 'Tuesday'), ('WED', 'Wednesday'), ('THURS', 'Thursday'), ('FRI', 'Friday'), ('SAT', 'Saturday')], default='SUN', max_length=6),
        ),
    ]