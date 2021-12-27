# Generated by Django 4.0 on 2021-12-15 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_alter_employees_experience'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employees',
            name='experience',
        ),
        migrations.AlterField(
            model_name='employees',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='employee', to='staff.department'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='employee', to='staff.post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='post', to='staff.department'),
        ),
    ]