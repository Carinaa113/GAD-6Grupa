
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joburi', '0004_alter_joburi_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joburi',
            name='url',
            field=models.URLField(max_length=100),
        ),
    ]
