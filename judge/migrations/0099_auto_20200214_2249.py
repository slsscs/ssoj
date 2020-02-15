# Generated by Django 2.2.7 on 2020-02-14 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0098_auto_20191124_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='judge',
            name='auth_key',
            field=models.CharField(help_text='A key to authenticate this judge', max_length=100, verbose_name='authentication key'),
        ),
        migrations.AlterField(
            model_name='language',
            name='description',
            field=models.TextField(blank=True, help_text='Use this field to inform users of quirks with your environment, additional restrictions, etc.', verbose_name='language description'),
        ),
    ]