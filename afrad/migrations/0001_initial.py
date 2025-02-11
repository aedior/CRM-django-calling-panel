# Generated by Django 5.1.4 on 2024-12-09 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Moshtari',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2000, verbose_name='نام و نام خانوادگی')),
                ('phone', models.IntegerField(verbose_name='شماره تلفن')),
                ('statusphone', models.IntegerField(choices=[(1, 'زنگ نزده شده'), (2, 'جواب نداده'), (3, 'جواب داده')], default=1, verbose_name='وضعیت تماس')),
                ('status', models.IntegerField(choices=[(1, 'نامشخص'), (2, 'جلسه'), (3, 'دوره')], default=1, verbose_name='وضعیت مشتری')),
                ('desc', models.TextField(max_length=10000, verbose_name='کپشن')),
            ],
        ),
    ]
