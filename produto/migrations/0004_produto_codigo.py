# Generated by Django 2.2.1 on 2019-05-19 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0003_categoria_destaque'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='codigo',
            field=models.CharField(db_index=True, default='ircs2019', max_length=200),
            preserve_default=False,
        ),
    ]
