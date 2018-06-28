# Generated by Django 2.0.6 on 2018-06-27 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mineral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('image_filename', models.CharField(max_length=255, null=True)),
                ('image_caption', models.CharField(max_length=255, null=True)),
                ('category', models.CharField(max_length=255, null=True)),
                ('formula', models.CharField(max_length=255, null=True)),
                ('strunz_classification', models.CharField(max_length=255, null=True)),
                ('crystal_system', models.CharField(max_length=255, null=True)),
                ('unit_cell', models.CharField(max_length=255, null=True)),
                ('color', models.CharField(max_length=255, null=True)),
                ('crystal_symmetry', models.CharField(max_length=255, null=True)),
                ('cleavage', models.CharField(max_length=255, null=True)),
                ('mohs_scale_hardness', models.CharField(max_length=255, null=True)),
                ('luster', models.CharField(max_length=255, null=True)),
                ('streak', models.CharField(max_length=255, null=True)),
                ('diaphaneity', models.CharField(max_length=255, null=True)),
                ('optical_properties', models.CharField(max_length=255, null=True)),
                ('refractive_index', models.CharField(max_length=255, null=True)),
                ('crystal_habit', models.CharField(max_length=255, null=True)),
                ('specific_gravity', models.CharField(max_length=255, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
