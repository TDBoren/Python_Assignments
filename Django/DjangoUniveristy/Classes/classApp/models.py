from django.db import models


class djangoClasses(models.Model):
    title = models.CharField(max_length=60, default="", blank=True, null=False)
    courseNumber = models.IntegerField(max_length=60, default="", blank=True, null=False)
    instructorName = models.CharField(max_length=60, default="", blank=True, null=False)
    duration = models.DecimalField(default=0.00, max_digits=1000, decimal_places=2, blank=True, null=False)


