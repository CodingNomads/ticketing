# Generated by Django 2.2 on 2019-04-10 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='lmgtfy',
            field=models.CharField(default='http://lmgtfy.com/?q=what%27s+the+time%3F', max_length=200),
            preserve_default=False,
        ),
    ]
