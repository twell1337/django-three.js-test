# Generated by Django 4.2.4 on 2024-05-22 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shape',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('1', 'Box')], max_length=1)),
                ('color', models.CharField(help_text='hex', max_length=7)),
            ],
        ),
    ]