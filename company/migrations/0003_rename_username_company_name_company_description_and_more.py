# Generated by Django 4.1.3 on 2022-11-21 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_rename_hrname_company_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='username',
            new_name='name',
        ),
        migrations.AddField(
            model_name='company',
            name='description',
            field=models.CharField(default='comp', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='linkedin',
            field=models.URLField(default='https://google.com'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='location',
            field=models.CharField(default='india', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='url',
            field=models.URLField(default='https://google.com'),
            preserve_default=False,
        ),
    ]
