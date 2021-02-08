from django.db import models
from django.db.models.fields import CharField


# Create your models here.

class WeekDays(models.Model):
    """ A meal planner model for s7 days of the week."""

    SUNDAY = 'SUN'
    MONDAY = 'MON'
    TUESDAY = 'TUE'
    WEDNESDAY = 'WED'
    THURSDAY = 'THURS'
    FRIDAY = 'FRI'
    SATURDAY = 'SAT'
    BREAKFAST = 'BFAST'
    LUNCH = "L'NCH"
    DINNER = "D'NNER"
    DESSERT = "D'SERT"
    DAYS_OF_THE_WEEK_CHOICES = [
        (SUNDAY, 'Sunday'),
        (MONDAY, 'Monday'),
        (TUESDAY, 'Tuesday'),
        (WEDNESDAY, 'Wednesday'),
        (THURSDAY, 'Thursday'),
        (FRIDAY, 'Friday'),
        (SATURDAY, 'Saturday'),
    ]

    MEAL_SESSION = [
        (BREAKFAST, 'Breakfast'),
        (LUNCH, 'Lunch'),
        (DINNER, 'Dinner'),
        (DESSERT, 'Dessert'),
    ]
    
    

    days_of_the_week = models.CharField(
        max_length=6,
        choices=DAYS_OF_THE_WEEK_CHOICES,
        default = SUNDAY
    )

    session_of_day = models.CharField(
        max_length=9,
        choices = MEAL_SESSION,
        default= BREAKFAST
    )

    meal = models.TextField(default= 'Please enter meal info and recipe',
    )

    

    def __str__(self):
        """ String representation of the WeekDays Model"""
        return f"{self.days_of_the_week} {self.session_of_day}"


#class Meal(models.Model):

    """Model representation of meal"""
    # meal_of_the_day = models.TextField()
    # day_of_week = models.ForeignKey(WeekDays, on_delete=models.CASCADE)
    
    # meal_of_the_day = models.TextField()
    #def __str__(self):
        #"""String representation of the Meal model"""
        #return self.meal_of_the_day

