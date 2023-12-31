# Generated by Django 3.2.21 on 2023-09-27 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='colour',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='developer',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='genre',
            field=models.CharField(choices=[('Action', 'Action'), ('Adventure', 'Adventure'), ('RPG', 'Role-Playing Game'), ('Simulation', 'Simulation'), ('Strategy', 'Strategy'), ('Sports', 'Sports'), ('Puzzle', 'Puzzle'), ('Platformer', 'Platformer'), ('Fighting', 'Fighting'), ('Horror', 'Horror')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='manufacturer',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='pgi_certificate',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='players',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='publisher',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='release_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='storage',
            field=models.CharField(max_length=254, null=True),
        ),
    ]
