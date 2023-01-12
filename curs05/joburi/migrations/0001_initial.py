from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Joburi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField()),
                ('url', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('salary', models.IntegerField()),
                ('currency', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=1)),
            ],
        ),
    ]
