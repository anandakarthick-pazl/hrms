# Generated by Django 4.2.11 on 2025-02-14 06:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accessibility', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='defaultaccessibility',
            name='employees',
            field=models.ManyToManyField(blank=True, related_name='default_accessibility', to='employee.employee'),
        ),
        migrations.AddField(
            model_name='defaultaccessibility',
            name='modified_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='Modified By'),
        ),
    ]
