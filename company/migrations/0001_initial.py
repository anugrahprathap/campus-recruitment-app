# Generated by Django 4.1.3 on 2022-11-15 16:40

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
            name='company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HRname', models.CharField(max_length=100)),
                ('comp_name', models.CharField(max_length=100)),
                ('mobile', models.BigIntegerField()),
                ('mail', models.EmailField(max_length=254)),
                ('login_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
