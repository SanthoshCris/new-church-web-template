# Generated by Django 4.0.5 on 2022-08-28 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('luzChurchAdmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Moto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moto', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='OfficeHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_history', models.TextField()),
                ('church_office', models.IntegerField()),
                ('church_mobile', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='HomePageSection1',
        ),
    ]
