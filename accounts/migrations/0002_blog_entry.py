# Generated by Django 4.0 on 2022-01-03 23:58

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('tagline', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=255)),
                ('body_text', models.TextField()),
                ('pub_date', models.DateField()),
                ('mod_date', models.DateField(default=datetime.date.today)),
                ('number_of_comments', models.IntegerField(default=0)),
                ('number_of_pingbacks', models.IntegerField(default=0)),
                ('rating', models.IntegerField(default=5)),
                ('authors', models.ManyToManyField(to='accounts.Author')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.blog')),
            ],
        ),
    ]