# Generated by Django 3.2.13 on 2022-12-06 10:51

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_claimowner_claimerpostid'),
    ]

    operations = [
        migrations.AddField(
            model_name='claimowner',
            name='postFileImg',
            field=models.ImageField(blank=True, null=True, upload_to=home.models.filepath),
        ),
    ]
