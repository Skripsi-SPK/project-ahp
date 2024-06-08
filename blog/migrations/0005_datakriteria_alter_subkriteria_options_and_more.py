# Generated by Django 5.0.2 on 2024-06-07 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_subkriteria_alter_kriteria_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataKriteria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(blank=True, max_length=100, null=True)),
                ('absensi', models.IntegerField(default=0)),
                ('skill', models.IntegerField(default=0)),
                ('tanggung_jawab', models.IntegerField(default=0)),
                ('loyalitas', models.IntegerField(default=0)),
                ('pelanggaran', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'DataKriteria',
            },
        ),
        migrations.AlterModelOptions(
            name='subkriteria',
            options={'verbose_name_plural': 'SubKriteria'},
        ),
        migrations.AlterField(
            model_name='subkriteria',
            name='nilai',
            field=models.IntegerField(default=0),
        ),
    ]