# Generated by Django 2.2.1 on 2019-05-20 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0005_categoria_outracategoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='nota',
            field=models.IntegerField(db_index=True, default=3, max_length=200),
            preserve_default=False,
        ),
    ]
