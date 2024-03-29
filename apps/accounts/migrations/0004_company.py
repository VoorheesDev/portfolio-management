# Generated by Django 3.2.8 on 2022-11-18 10:02

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_email_confirmed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Company name')),
                ('logo', models.ImageField(upload_to='company_logos/', verbose_name='Company logo')),
                ('year_founded', models.IntegerField(validators=[django.core.validators.MinValueValidator(1950), django.core.validators.MaxValueValidator(2022)])),
                ('website', models.URLField(verbose_name='Company website')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Contact email')),
                ('slogan', models.CharField(max_length=255, verbose_name='Company slogan')),
                ('description', models.TextField(verbose_name='Description')),
                ('founder', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='founder_company', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Companies',
            },
        ),
    ]
