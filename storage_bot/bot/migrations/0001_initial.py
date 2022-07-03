# Generated by Django 4.0.5 on 2022-07-03 19:47

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='Номер')),
                ('temperature', models.CharField(max_length=20, verbose_name='Температура')),
                ('height', models.FloatField(verbose_name='Высота')),
                ('floor', models.IntegerField(verbose_name='Этаж')),
                ('size', models.CharField(max_length=100, verbose_name='Размер')),
                ('price', models.FloatField(verbose_name='Цена')),
            ],
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100, verbose_name='Адрес')),
                ('work_time', models.CharField(max_length=50, verbose_name='Режим работы')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_id', models.IntegerField(null=True, verbose_name='ID пользователя в Telegram')),
                ('name', models.CharField(blank=True, max_length=50, verbose_name='Имя')),
                ('surname', models.CharField(blank=True, max_length=50, verbose_name='Фамилия')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Электронная почта')),
                ('address', models.CharField(blank=True, max_length=100, verbose_name='Адрес')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, region=None, verbose_name='Номер телефона')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(null=True, verbose_name='Дата создания')),
                ('measurer', models.BooleanField(default=False, verbose_name='Нужен ли замерщик')),
                ('comment', models.CharField(blank=True, max_length=100, verbose_name='Комментарий')),
                ('lease_time', models.DateTimeField(verbose_name='Дата окончания аренды')),
                ('cell', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='bot.cell', verbose_name='Ячейка')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='bot.user', verbose_name='Заказчик')),
            ],
        ),
        migrations.AddField(
            model_name='cell',
            name='storage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cells', to='bot.storage', verbose_name='Склад'),
        ),
    ]
