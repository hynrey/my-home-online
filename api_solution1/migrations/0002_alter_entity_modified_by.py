# Generated by Django 4.2 on 2023-04-19 15:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api_solution1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entity',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='modified_by_solution1', to=settings.AUTH_USER_MODEL),
        ),
    ]
