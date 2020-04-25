from django.db import models

class mainBanner(models.Model):
    title = models.CharField(max_length=200)
    link = models.TextField()
    img = models.FileField(null=False)
    
    def __str__(self):
        return self.title

class rollingBanner(models.Model):
    title = models.CharField(max_length=200)
    link = models.TextField()
    img = models.FileField(null=False)
    
    def __str__(self):
        return self.title

class subBanner(models.Model):
    title = models.CharField(max_length=200)
    link = models.TextField()
    img = models.FileField(null=False)
    
    def __str__(self):
        return self.title

class accessTrade(models.Model):
    category = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    link = models.TextField()
    price = models.CharField(max_length=200)
    img = models.FileField(null=False)
    
    def __str__(self):
        return self.title