# Generated by Django 3.0.3 on 2020-06-11 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('laundry_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category_name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catg_name', models.CharField(max_length=265, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('washing_price', models.CharField(max_length=264)),
                ('dryclean_price', models.CharField(max_length=255)),
                ('item_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laundry_app.Category_name')),
            ],
        ),
        migrations.RemoveField(
            model_name='webpage',
            name='topic',
        ),
        migrations.DeleteModel(
            name='AccessRecord',
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
        migrations.DeleteModel(
            name='Webpage',
        ),
    ]
