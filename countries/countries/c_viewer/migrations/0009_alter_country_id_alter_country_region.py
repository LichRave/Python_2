# Generated by Django 5.0.1 on 2024-05-22 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('c_viewer', '0008_alter_country_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='country',
            name='region',
            field=models.CharField(choices=[('WESTERN EUROPE', 'WESTERN EUROPE'), ('ASIA (EX. NEAR EAST)', 'ASIA (EX. NEAR EAST)'), ('EASTERN EUROPE', 'EASTERN EUROPE'), ('BALTICS', 'BALTICS'), ('SUB-SAHARAN AFRICA', 'SUB-SAHARAN AFRICA'), ('LATIN AMER. & CARIB', 'LATIN AMER. & CARIB'), ('OCEANIA', 'OCEANIA'), ('C.W. OF IND. STATES', 'C.W. OF IND. STATES'), ('NORTHERN AFRICA', 'NORTHERN AFRICA'), ('NORTHERN AMERICA', 'NORTHERN AMERICA'), ('NEAR EAST', 'NEAR EAST')], max_length=500),
        ),
    ]
