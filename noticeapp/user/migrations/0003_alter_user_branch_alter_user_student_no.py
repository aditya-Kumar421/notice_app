# Generated by Django 5.0.6 on 2024-06-03 10:55

import user.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_branch_user_created_user_student_no_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='branch',
            field=models.CharField(choices=[('CSE', 'CSE'), ('CS', 'CS'), ('CSE(AIML)', 'CSE-AIML'), ('CSE(DS)', 'CSE-DS'), ('CSE(Hindi)', 'CS(Hindi)'), ('AIML', 'AIML'), ('IT', 'IT'), ('CSIT', 'CS&IT'), ('ECE', 'ECE'), ('EN', 'EN'), ('ME', 'ME'), ('CIVIL', 'CE')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='student_no',
            field=models.IntegerField(null=True, validators=[user.models.validate_Student_digits]),
        ),
    ]