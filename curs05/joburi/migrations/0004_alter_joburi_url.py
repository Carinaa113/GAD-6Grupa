
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joburi', '0003_alter_joburi_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joburi',
            name='url',
            field=models.URLField(),
        ),
    ]
