from django.db import models

class Bill(models.Model):
    id = models.AutoField(primary_key=True)
    money = models.IntegerField()
    date = models.CharField(max_length=200)
    file_name = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.money} | {self.date} | {self.file_name}"


