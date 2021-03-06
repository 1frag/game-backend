# Generated by Django 2.2.4 on 2019-08-25 01:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BotGame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.IntegerField()),
                ('alpha', models.IntegerField()),
                ('speed', models.FloatField()),
                ('path', models.IntegerField()),
                ('cnt_stops', models.IntegerField()),
                ('begin_latit', models.FloatField()),
                ('begin_long', models.FloatField()),
                ('end_latit', models.FloatField()),
                ('end_long', models.FloatField()),
                ('user_latit', models.FloatField()),
                ('user_long', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('cost', models.IntegerField(default=1)),
                ('size', models.IntegerField(default=15)),
                ('taken', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=4, unique=True)),
                ('duration', models.IntegerField(null=True)),
                ('type_game', models.IntegerField()),
                ('cnt_gamers', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('CR', 'CREATED'), ('IN', 'INITIALIZED'), ('ST', 'STARTED'), ('FN', 'FINISHED'), ('AR', 'ARCHIVED')], default='CR', max_length=2)),
                ('time_end_game', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gamer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True)),
                ('password', models.CharField(max_length=120)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('date_sign_up', models.DateTimeField(auto_now_add=True)),
                ('sex', models.IntegerField(blank=True, default=0, null=True)),
                ('money', models.IntegerField(default=0)),
                ('rating', models.IntegerField(default=0)),
                ('is_superuser', models.BooleanField(default=0)),
                ('mileage', models.IntegerField(default=0)),
                ('hints', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='GiG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('status', models.CharField(choices=[('AC', 'ACTIVE'), ('NA', 'DISCONNECTED'), ('BL', 'BLOCKED')], default='AC', max_length=2)),
                ('color', models.IntegerField()),
                ('radius', models.IntegerField(null=True)),
                ('chief', models.BooleanField(default=False)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tmp_name.Game')),
                ('gamer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tmp_name.Gamer')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('gg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tmp_name.GiG')),
            ],
        ),
    ]
