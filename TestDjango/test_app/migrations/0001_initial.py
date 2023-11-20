# Generated by Django 4.2.6 on 2023-11-19 23:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name_author', models.CharField(max_length=100)),
                ('second_name_author', models.CharField(max_length=100)),
                ('birthday', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Testmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname_test', models.CharField(max_length=100)),
                ('lastname_test', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('model_img', models.ImageField(upload_to='img/')),
            ],
        ),
        migrations.CreateModel(
            name='Magazine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('num_pages', models.PositiveIntegerField()),
                ('issue_number', models.PositiveIntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.author')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('num_pages', models.PositiveIntegerField()),
                ('volume_number', models.PositiveIntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.author')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='author',
            name='libraries',
            field=models.ManyToManyField(related_name='authors', to='test_app.library'),
        ),
    ]
