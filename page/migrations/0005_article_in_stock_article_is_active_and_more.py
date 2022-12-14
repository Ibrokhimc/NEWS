# Generated by Django 4.1 on 2022-08-24 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0004_alter_categories_name_alter_categories_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='in_stock',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='article',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='Category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='page.categories'),
        ),
    ]
