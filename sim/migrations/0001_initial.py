# Generated by Django 2.0.1 on 2018-01-03 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Password', models.CharField(max_length=10, verbose_name='password')),
                ('studentInfo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tm.StudentInfo', to_field='SerialNum')),
            ],
        ),
    ]
