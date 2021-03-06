# Generated by Django 3.2.6 on 2021-09-07 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fav_team_form', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forminfo',
            name='place_of_birth',
            field=models.CharField(choices=[('', ''), ('Andijon', 'Andijon viloyati'), ('Buxoro', 'Buxoro viloyati'), ('Jizzax', 'Jizzax viloyati'), ('Qashqadaryo', 'Qashqadaryo viloyati'), ('Navoiy', 'Navoiy viloyati'), ('Namangan', 'Namangan viloyati'), ('Samarqand', 'Samarqand viloyati'), ('Surxondaryo', 'Surxondaryo viloyati'), ('Sirdaryo', 'Sirdaryo viloyati'), ('Toshkent vil', 'Toshkent viloyati'), ('Toshkent sh', 'Toshkent shahri'), ('Fargʻona', 'Fargʻona viloyati'), ('Xorazm', 'Xorazm viloyati'), ('Qoraqalpogʻiston', 'Qoraqalpogʻiston Respublikasi')], max_length=50, verbose_name="Tug'ilgan Joyi*"),
        ),
        migrations.AlterField(
            model_name='forminfo',
            name='place_of_residence',
            field=models.CharField(choices=[('', ''), ('Andijon', 'Andijon viloyati'), ('Buxoro', 'Buxoro viloyati'), ('Jizzax', 'Jizzax viloyati'), ('Qashqadaryo', 'Qashqadaryo viloyati'), ('Navoiy', 'Navoiy viloyati'), ('Namangan', 'Namangan viloyati'), ('Samarqand', 'Samarqand viloyati'), ('Surxondaryo', 'Surxondaryo viloyati'), ('Sirdaryo', 'Sirdaryo viloyati'), ('Toshkent vil', 'Toshkent viloyati'), ('Toshkent sh', 'Toshkent shahri'), ('Fargʻona', 'Fargʻona viloyati'), ('Xorazm', 'Xorazm viloyati'), ('Qoraqalpogʻiston', 'Qoraqalpogʻiston Respublikasi')], max_length=50, verbose_name='Yashash Joyi*'),
        ),
    ]
