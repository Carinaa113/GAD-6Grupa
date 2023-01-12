from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joburi', '0002_alter_joburi_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joburi',
            name='description',
            field=models.TextField(),
        ),
    ]
