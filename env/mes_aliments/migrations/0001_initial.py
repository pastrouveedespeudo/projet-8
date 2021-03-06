# Generated by Django 2.2.1 on 2019-05-04 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_categorie', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='aliment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_aliment', models.CharField(max_length=100)),
                ('code_product_food', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('nutriscore', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
                ('name_store', models.CharField(max_length=100)),
                ('name_brand', models.CharField(max_length=100)),
                ('id_categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mes_aliments.categorie')),
            ],
        ),
    ]
