# Generated by Django 4.2.7 on 2023-12-05 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('severity', models.CharField(choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')], default='Low', max_length=10)),
                ('ticket_title', models.CharField(max_length=50)),
                ('ticket_description', models.TextField()),
                ('ticket_id', models.CharField(max_length=15, unique=True)),
                ('is_resolved', models.BooleanField(default=False)),
                ('is_assigned_to_leader', models.BooleanField(default=False)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='project.project')),
            ],
        ),
    ]
