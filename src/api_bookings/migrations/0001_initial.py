# Generated by Django 3.1.2 on 2020-10-05 15:48

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookingModels',
            fields=[
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Cancel', 'Cancel'), ('Finish', 'Finish')], default='Pending', max_length=100)),
                ('is_payed', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'fb_bookings',
            },
        ),
    ]