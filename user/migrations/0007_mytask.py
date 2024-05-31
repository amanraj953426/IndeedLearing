# Generated by Django 3.2.4 on 2023-09-23 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_delete_mytask'),
    ]

    operations = [
        migrations.CreateModel(
            name='mytask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('task_file', models.FileField(null=True, upload_to='static/task')),
                ('added_date', models.DateField(null=True)),
                ('taskbatch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.batch')),
            ],
        ),
    ]
