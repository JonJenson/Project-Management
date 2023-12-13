# Generated by Django 4.2.7 on 2023-12-05 14:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0003_rename_project_name_project_project_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='engineers',
        ),
        migrations.RemoveField(
            model_name='project',
            name='team_leaders',
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('engineers', models.ManyToManyField(limit_choices_to={'is_engineer': True}, related_name='assigned_teams', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='project.project')),
                ('team_leader', models.ForeignKey(limit_choices_to={'is_teamleader': True}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
