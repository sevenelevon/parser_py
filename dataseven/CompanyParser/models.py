from django.db import models
from .utils import get_link_data

class Item(models.Model):
    name = models.CharField(max_length=220, blank=True)
    url = models.URLField()
    date = models.CharField(max_length=220, blank=True)
    NameCompany = models.CharField(max_length=220, blank=True)
    cityCompany = models.CharField(max_length=220, blank=True)
    SiteCompany = models.CharField(max_length=220, blank=True)
    ActivityCompany = models.CharField(max_length=220, blank=True)
    notification = models.CharField(max_length=220, blank=True)
    curent_value = models.CharField(max_length=220, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.name)
            
    def save(self, *args, **kwargs):
        name, company, date, NameCompany, cityCompany, SiteCompany, ActivityCompany, notification = get_link_data(self.url)
        self.date = date
        self.NameCompany = NameCompany
        self.cityCompany = cityCompany
        self.SiteCompany = SiteCompany
        self.ActivityCompany = ActivityCompany
        self.notification = notification
        self.name = name
        self.curent_value = company
        
        super().save(*args, **kwargs)