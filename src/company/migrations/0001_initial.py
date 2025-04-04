# Generated by Django 4.2.20 on 2025-03-25 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Deleted At')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CompanyProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Deleted At')),
                ('address', models.TextField(blank=True, null=True)),
                ('logo_url', models.URLField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('certifications', models.TextField(blank=True, null=True)),
                ('carbon_footprint_details', models.TextField(blank=True, null=True)),
                ('manufacturing_capacity', models.TextField(blank=True, null=True)),
                ('moq_policy', models.TextField(blank=True, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('social_media_links', models.JSONField(blank=True, null=True)),
                ('established_year', models.IntegerField(blank=True, null=True)),
                ('number_of_employees', models.IntegerField(blank=True, null=True)),
                ('annual_revenue', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('quality_standards', models.TextField(blank=True, null=True)),
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='company.company')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
