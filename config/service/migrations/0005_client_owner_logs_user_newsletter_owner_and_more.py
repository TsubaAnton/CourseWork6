# Generated by Django 4.2 on 2024-05-15 19:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('service', '0004_alter_logs_newsletter'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Владелец'),
        ),
        migrations.AddField(
            model_name='logs',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='newsletter',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Владелец'),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='clients',
            field=models.ManyToManyField(to='service.client', verbose_name='Клиенты рассылки'),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='message',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='service.message', verbose_name='Сообщения'),
        ),
    ]
