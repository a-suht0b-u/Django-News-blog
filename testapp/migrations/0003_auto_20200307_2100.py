# Generated by Django 3.0.2 on 2020-03-07 19:00

from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.PROTECT, to='testapp.Rubric'),
        ),
    ]
