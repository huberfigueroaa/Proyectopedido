# Generated by Django 2.2 on 2019-04-02 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('envios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='envio',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.Cliente'),
        ),
    ]
