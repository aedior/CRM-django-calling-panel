from django.db import models

# Create your models here.

class Typephone(models.IntegerChoices):
    num0=1,"زنگ نزده شده"
    num1=2,"جواب نداده"
    num2=3,"جواب داده"

class Typestatus(models.IntegerChoices):
    num0=1,"نامشخص"
    num1=2,"جلسه"
    num2=3,"دوره"



class TypeMoshtari(models.Model):
    class Meta:
        verbose_name="خدمات"
        verbose_name_plural="خدمات"

    name = models.CharField(max_length=1000, verbose_name="نام")
    moshtari = models.ForeignKey(to="afrad.Moshtari", verbose_name="مشتری", on_delete=models.CASCADE)

class Moshtari(models.Model):

    class Meta:
        verbose_name="مشتری"
        verbose_name_plural="مشتری"

    name = models.CharField(max_length=2000, verbose_name="نام و نام خانوادگی")
    phone = models.IntegerField("شماره تلفن")
    statusphone = models.IntegerField(default=1, choices=Typephone, verbose_name="وضعیت تماس")
    status = models.IntegerField(default=1, choices=Typestatus, verbose_name="وضعیت مشتری")
    desc = models.TextField(max_length=10000, verbose_name="کپشن", null=True, blank=True)
    variz = models.BooleanField(verbose_name="اتمام پرداخت", default=False)
    varizshode = models.IntegerField(verbose_name="واریزی", null=True, blank=True)
    behkar = models.IntegerField(verbose_name="بدهکار", null=True, blank=True)


    def __str__(self):
        return self.name