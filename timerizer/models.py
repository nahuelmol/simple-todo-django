from django.db import models

class ImportantDate(models.Model):
    year = models.IntegerField()
    week_day = models.IntegerField()
    date_number = models.IntegerField()
    month = models.CharField()
    bisiesto = models.BooleanField()
    
    def __str__(self):
        return self.year
    
my_month_b = ImportantDate.objects.all()
coincidens = my_month_b.filter(month = Agost, day = 9)
