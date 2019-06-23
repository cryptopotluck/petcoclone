# Generated by Django 2.2.2 on 2019-06-23 20:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CreatePet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet_name', models.CharField(max_length=25)),
                ('pet_bread', models.CharField(blank=True, max_length=25)),
                ('pet_type', models.CharField(choices=[('Dog', 'Dog'), ('Cat', 'Cat'), ('Reptile', 'Reptile'), ('Aquatic', 'Aquatic'), ('Rodent', 'Rodent'), ('Outdoor', 'Outdoor'), ('Exotic', 'Exotic')], default='Dog', max_length=50)),
                ('birthday', models.DateField(blank=True, default='1996-07-10')),
                ('pet_profile_pic', models.ImageField(blank=True, default='profile/default/dog_default.jpeg', upload_to='dog/%Y/%m/%d/')),
                ('about_pet', models.TextField(blank=True)),
                ('owner', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
