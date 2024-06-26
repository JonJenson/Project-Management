# Generated by Django 4.2.7 on 2023-12-10 09:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0007_alter_project_customer_alter_project_manager_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teamleader',
            name='user',
            field=models.ForeignKey(limit_choices_to={'is_teamleader': True}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
