# Generated by Django 2.2.4 on 2019-08-13 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='question_tags', to='questions.Tag'),
        ),
    ]