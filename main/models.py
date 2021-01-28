from django.db import models

class Bill(models.Model):
    id = models.AutoField(primary_key=True)
    money = models.IntegerField()
    date = models.CharField(max_length=200)
    url_image = models.CharField(max_length=1000)
    image = models.FileField(upload_to='app/image')
    def setF(self,money, date):
        self.money = money
        self.date = date
      
    def __str__(self):
        return f"{self.money} | {self.date} "


