# Generated by Django 3.0.6 on 2020-05-28 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200527_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='bgcolor',
            field=models.CharField(blank=True, default='black', max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='color',
            field=models.CharField(blank=True, default='blue', max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='custom_design',
            field=models.ImageField(blank=True, default='shirt.jpeg', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='item',
            name='instruction',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='iscustom',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='print_text',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='shape',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='size',
            field=models.CharField(blank=True, choices=[('S', 'SMALL'), ('L', 'LARGE'), ('XL', 'EXTRA LARGE'), ('2XL', '2XL'), ('3XL', '3XL'), ('4XL', '4XL')], default='L', max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='textcolor',
            field=models.CharField(blank=True, default='white', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='active',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='featured',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]