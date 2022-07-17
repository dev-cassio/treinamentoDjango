# Generated by Django 4.0.6 on 2022-07-17 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacao', '0003_rename_cargo_cargos'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='cargo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='autenticacao.cargos'),
            preserve_default=False,
        ),
    ]
