# Generated by Django 2.0 on 2018-03-04 02:56

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
                ('SerialNum', models.CharField(max_length=15, verbose_name='学号')),
                ('Password', models.CharField(max_length=15, verbose_name='密码')),
                ('Email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='邮箱')),
                ('studentInfo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tm.StudentInfo')),
            ],
        ),
    ]
