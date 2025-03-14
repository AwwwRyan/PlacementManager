# Generated by Django 5.1.6 on 2025-03-05 10:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0002_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testresult',
            name='student',
            field=models.ForeignKey(db_column='student_username', limit_choices_to={'role': 'student'}, on_delete=django.db.models.deletion.CASCADE, to='users.customuser', to_field='username'),
        ),
    ]
