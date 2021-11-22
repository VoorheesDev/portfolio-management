# Generated by Django 3.2.8 on 2021-11-11 15:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0004_alter_project_is_private'),
    ]

    operations = [
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Set name')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_sets', to=settings.AUTH_USER_MODEL)),
                ('projects', models.ManyToManyField(to='projects.Project')),
            ],
            options={
                'verbose_name_plural': 'Sets',
                'unique_together': {('name', 'author')},
            },
        ),
    ]