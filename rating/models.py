from django.db import models
from django.conf import settings


RamenUser = settings.AUTH_USER_MODEL

class Ramen(models.Model):
    STYLE = (
        ('Cup', 'cup'),
        ('Pack', 'pack'),
        ('Tray', 'tray'),
        ('Bowl', 'bowl'),
    )

    brand = models.CharField(max_length=250, blank=False)
    variety = models.CharField(max_length=250)
    style = models.CharField(max_length=5, choices=STYLE)
    country = models.CharField(max_length=250)
    stars = models.FloatField(default=1)
    dateReview = models.DateTimeField()
    topTen = models.CharField(max_length=10)
    ramenuser = models.ForeignKey(RamenUser, on_delete=models.SET_NULL,
                                    default=1, null=True)
   

    
    def __str__(self):
        return self.brand  