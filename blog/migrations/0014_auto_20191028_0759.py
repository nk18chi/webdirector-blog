# Generated by Django 2.2.5 on 2019-10-28 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20191028_0719'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcategory',
            name='description_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blogcategory',
            name='description_ja',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blogcategory',
            name='name_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='blogcategory',
            name='name_ja',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='seo_description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='seo_description_ja',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='blogtag',
            name='description_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blogtag',
            name='description_ja',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blogtag',
            name='name_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='blogtag',
            name='name_ja',
            field=models.CharField(max_length=200, null=True),
        ),
    ]