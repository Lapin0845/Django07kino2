from django.db import models

# Create your models here.
class Focus(models.Model):
    name = models.CharField(max_length=20, verbose_name='Направленность')

    def __str__(self):
        return self.name

class Director(models.Model):
    fname = models.CharField(max_length=20, verbose_name='Имя')
    lname = models.CharField(max_length=20, verbose_name='Фамилия')

    def __str__(self):
        return f'{self.fname}, {self.lname}'

class Doctor(models.Model):
    fname = models.CharField(max_length=20, verbose_name='Имя')
    lname = models.CharField(max_length=20, verbose_name='Фамилия')

    def __str__(self):
        return self.lname

class Status(models.Model):
    vibor = (('Профилактика', 'Профилактика'),('Лечение'))
    name = models.CharField(max_length=20, verbose_name='Заболевание')

    def __str__(self):
        return self.name

class Street(models.Model):
    name = models.CharField(max_length=20, verbose_name='Улица')

    def __str__(self):
        return self.name

class Reception(models.Model):
    choise = (('Первичный 1000р', 'Первичный 1000р'), ('Второй 700р', 'Второй 700р'))
    rate = models.CharField(max_length=20, choices=choise, verbose_name='Прием')

    def __str__(self):
        return self.rate

class Vetclinika(models.Model):
    title = models.CharField(max_length=20, verbose_name='Название')
    focus = models.ForeignKey(Focus, on_delete=models.SET_DEFAULT, default=1)
    rating = models.FloatField(verbose_name='Оценка')
    street = models.ForeignKey(Street, on_delete=models.SET_NULL, null=True)
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=500, verbose_name='Описание')
    recep = models.ForeignKey(Reception, on_delete=models.SET_NULL, null=True)
    doct = models.ManyToManyField(Doctor, verbose_name='Врачи')
    status = models.ForeignKey(Status, on_delete=models.SET_DEFAULT,default=1)

    def __str__(self):
        return self.title

    def display_doctors(self):
        res=''
        for a in self.d.all():
            res+=a.lname+' '
        return res
    display_doctors.short_discription='Врач'