# Generated by Django 3.0.5 on 2020-06-02 21:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fitness', '0004_auto_20200601_1650'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='exerciseinstance',
            name='type',
        ),
        migrations.AddField(
            model_name='exercise',
            name='type',
            field=models.CharField(choices=[('db', 'Dumbbell'), ('bb', 'Barbell'), ('bw', 'Bodyweight')], default='db', help_text='Enter "db", "bb" or "bw"', max_length=15),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='name',
            field=models.CharField(help_text='Enter a name for the exercise (e.g. Bench Press).', max_length=100),
        ),
        migrations.DeleteModel(
            name='WorkoutInstance',
        ),
        migrations.AddField(
            model_name='workout',
            name='exercises',
            field=models.ManyToManyField(to='fitness.Exercise'),
        ),
        migrations.AddField(
            model_name='workout',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
