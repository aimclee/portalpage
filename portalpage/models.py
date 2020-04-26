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
    contents = (
        ('Thời trang nữ','Thời trang nữ'),
        ('Thời trang nam','Thời trang nam'),
        ('Công nghẹ','Công nghẹ'),
        ('Đời sống','Đời sống'),
        ('Ô-tô/Xe máy','Ô-tô/Xe máy')
    )
    category = models.CharField(max_length=200, choices = contents, default = 'Thời trang nữ',)
    title = models.CharField(max_length=200)
    link = models.TextField()
    price = models.IntegerField()
    img = models.FileField(null=False)
    
    def __str__(self):
        return self.title

class reigsterCount(models.Model):
    count = models.IntegerField()
    def __str__(self):
        return self.title