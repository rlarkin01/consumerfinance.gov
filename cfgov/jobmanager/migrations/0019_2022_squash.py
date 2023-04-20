# Generated by Django 3.2.12 on 2022-03-14 23:58

import django.db.models.deletion
from django.db import migrations, models

import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('jobmanager', '0018_recreated_2'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewRegion',
            fields=[
                ('name', models.CharField(max_length=255)),
                ('abbreviation', models.CharField(max_length=2, primary_key=True, serialize=False)),
            ],
            options={
                'ordering': ('abbreviation',),
            },
        ),
        migrations.CreateModel(
            name='NewState',
            fields=[
                ('name', models.CharField(max_length=255)),
                ('abbreviation', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('region', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.PROTECT, related_name='states', to='jobmanager.newregion')),
            ],
            options={
                'ordering': ('abbreviation',),
            },
        ),
        migrations.CreateModel(
            name='NewOffice',
            fields=[
                ('name', models.CharField(max_length=255)),
                ('abbreviation', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='jobmanager.newstate')),
            ],
            options={
                'ordering': ('abbreviation',),
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='joblistingpage',
            name='offices',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, related_name='job_listings', to='jobmanager.NewOffice'),
        ),
        migrations.AddField(
            model_name='joblistingpage',
            name='regions',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, related_name='job_listings', to='jobmanager.NewRegion'),
        ),
        migrations.CreateModel(
            name='MajorCity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('region', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.PROTECT, related_name='major_cities', to='jobmanager.newregion')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='jobmanager.newstate')),
            ],
            options={
                'ordering': ('state', 'name'),
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='joblistingpage',
            name='location',
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='JobLocation',
        ),
        migrations.DeleteModel(
            name='Office',
        ),
        migrations.DeleteModel(
            name='Region',
        ),
        migrations.DeleteModel(
            name='State',
        ),
        migrations.RenameModel(
            old_name='NewOffice',
            new_name='Office',
        ),
        migrations.RenameModel(
            old_name='NewRegion',
            new_name='Region',
        ),
        migrations.RenameModel(
            old_name='NewState',
            new_name='State',
        ),
        migrations.AlterField(
            model_name='joblistingpage',
            name='allow_remote',
            field=models.BooleanField(default=False, verbose_name='Office location can also be remote'),
        ),
        migrations.AlterField(
            model_name='applicanttype',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='emailapplicationlink',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='grade',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='gradepanel',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='jobcategory',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='joblength',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='servicetype',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='usajobsapplicationlink',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
