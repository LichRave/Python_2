# Generated by Django 5.0.1 on 2024-05-22 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('c_viewer', '0004_alter_country_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='region',
            field=models.CharField(choices=[('WESTERN EUROPE', 'WESTERN EUROPE'), ('NEAR EAST', 'NEAR EAST'), ('C.W. OF IND. STATES', 'C.W. OF IND. STATES'), ('OCEANIA', 'OCEANIA'), ('NORTHERN AFRICA', 'NORTHERN AFRICA'), ('LATIN AMER. & CARIB', 'LATIN AMER. & CARIB'), ('BALTICS', 'BALTICS'), ('EASTERN EUROPE', 'EASTERN EUROPE'), ('NORTHERN AMERICA', 'NORTHERN AMERICA'), ('SUB-SAHARAN AFRICA', 'SUB-SAHARAN AFRICA'), ('ASIA (EX. NEAR EAST)', 'ASIA (EX. NEAR EAST)')], max_length=500),
        ),
    ]
