# Generated by Django 2.2.4 on 2019-08-18 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.CharField(max_length=500)),
                ('last_updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]