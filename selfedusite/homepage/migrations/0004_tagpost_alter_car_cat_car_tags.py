# Generated by Django 4.2.1 on 2024-02-27 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_category_alter_car_is_published_car_cat'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='car',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='homepage.category'),
        ),
        migrations.AddField(
            model_name='car',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tags', to='homepage.tagpost'),
        ),
    ]
