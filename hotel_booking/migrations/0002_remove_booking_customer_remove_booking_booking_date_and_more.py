# Generated by Django 5.1.3 on 2024-11-17 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_booking', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='booking_date',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='check_in_date',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='check_out_date',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='total_price',
        ),
        migrations.RemoveField(
            model_name='room',
            name='availability',
        ),
        migrations.RemoveField(
            model_name='room',
            name='price_per_night',
        ),
        migrations.RemoveField(
            model_name='room',
            name='room_number',
        ),
        migrations.RemoveField(
            model_name='room',
            name='room_type',
        ),
        migrations.AddField(
            model_name='booking',
            name='duration',
            field=models.PositiveIntegerField(default=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='name',
            field=models.CharField(default='nexus gk', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='total_cost',
            field=models.DecimalField(decimal_places=2, default=5000, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='description',
            field=models.TextField(default='good condition'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='name',
            field=models.CharField(default='nexus gk', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='price',
            field=models.DecimalField(decimal_places=2, default=12000, max_digits=10),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
