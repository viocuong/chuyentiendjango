from django.db import models

class Bill(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    money = models.IntegerField()
    date = models.CharField(max_length=200)
    url_image = models.CharField(max_length=1000)
    image = models.FileField()
    def setF(self,money, date, name):
        self.money = money
        self.date = date
        self.name = name
      
    def __str__(self):
        return f"{self.name} {self.money} | {self.date} "


