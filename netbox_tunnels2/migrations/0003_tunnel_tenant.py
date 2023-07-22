# Generated by Django 4.1.9 on 2023-07-22 01:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tenancy', '0010_tenant_relax_uniqueness'),
        ('netbox_tunnels2', '0002_alter_tunnel_b_pub_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='tunnel',
            name='tenant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='tenancy.tenant'),
        ),
    ]
