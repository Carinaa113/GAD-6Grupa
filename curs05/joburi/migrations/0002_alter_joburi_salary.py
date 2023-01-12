from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joburi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joburi',
            name='salary',
            field=models.CharField(max_length=100),
        ),
    ]
