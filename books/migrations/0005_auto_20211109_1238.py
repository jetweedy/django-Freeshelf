# Generated by Django 3.2.9 on 2021-11-09 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20211109_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='favorite_books',
            field=models.ManyToManyField(to='books.Book'),
        ),
        migrations.DeleteModel(
            name='FavoriteBooks',
        ),
    ]