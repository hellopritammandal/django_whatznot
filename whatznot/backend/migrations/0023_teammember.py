# Generated by Django 4.2.4 on 2023-09-04 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0022_portfolio_is_featured'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='team_members/')),
            ],
        ),
    ]
