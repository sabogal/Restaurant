# Generated by Django 4.0.2 on 2024-04-24 00:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_creation', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_updated', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=30, unique=True)),
                ('description', models.TextField(blank=True, null=True, verbose_name='tipo de daño')),
                ('price', models.PositiveIntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('user_creation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_creation', to=settings.AUTH_USER_MODEL)),
                ('user_updated', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
                'db_table': 'products',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='WorkOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_creation', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_updated', models.DateTimeField(auto_now=True, null=True)),
                ('price', models.PositiveIntegerField(verbose_name='precio')),
                ('description', models.TextField(blank=True, null=True, verbose_name='descripcion')),
                ('state', models.PositiveIntegerField(choices=[(1, 'Procesado'), (2, 'Listo')], verbose_name='estado')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'order',
                'verbose_name_plural': 'order',
                'db_table': 'orders',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='WorkOrderProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_creation', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_updated', models.DateTimeField(auto_now=True, null=True)),
                ('amount', models.PositiveBigIntegerField(verbose_name='cantidad')),
                ('is_active', models.BooleanField(default=True)),
                ('fk_products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work_order.products', verbose_name='Productos')),
                ('fk_workorder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work_order.workorder', verbose_name='Productos')),
                ('user_creation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_creation', to=settings.AUTH_USER_MODEL)),
                ('user_updated', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'orden de trabajo producto',
                'verbose_name_plural': 'ordenes de trabajo productos',
                'db_table': 'work_order_products',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='workorder',
            name='fk_products',
            field=models.ManyToManyField(through='work_order.WorkOrderProducts', to='work_order.Products', verbose_name='productos'),
        ),
        migrations.AddField(
            model_name='workorder',
            name='user_creation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_creation', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='workorder',
            name='user_updated',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_updated', to=settings.AUTH_USER_MODEL),
        ),
    ]
