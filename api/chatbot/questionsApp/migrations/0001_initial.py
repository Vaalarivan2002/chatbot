# Generated by Django 5.0.3 on 2024-06-19 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('question_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('question', models.TextField(unique=True)),
                ('answer', models.TextField()),
            ],
        ),
    ]
