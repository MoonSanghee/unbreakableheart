# Generated by Django 3.2.13 on 2022-12-05 12:57


import articles.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('music', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(validators=[articles.models.validate_text])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('picture', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='images/')),
                ('disclosure', models.BooleanField(default=False)),
                ('feelings', models.CharField(choices=[('😃', '😃'), ('😄', '😄'), ('🤣', '🤣'), ('😍', '😍'), ('🥴', '🥴'), ('🤪', '🤪'), ('😐', '😐'), ('🙄', '🙄'), ('😔', '😔'), ('😪', '😪'), ('😦', '😦'), ('😰', '😰'), ('😭', '😭'), ('😱', '😱'), ('😣', '😣'), ('😩', '😩'), ('😤', '😤'), ('🥱', '🥱'), ('🥵', '🥵'), ('🥶', '🥶')], max_length=10)),
                ('music_start', models.IntegerField(default=0)),
                ('song', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='music.song')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=160, validators=[articles.models.validate_text])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('articles', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.articles')),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CommentDeclaration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.comment')),
                ('reported', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_writer', to=settings.AUTH_USER_MODEL)),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_reporter', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ArticlesDeclaration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
                ('articles', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.articles')),
                ('reported', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles_writer', to=settings.AUTH_USER_MODEL)),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles_reporter', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='commentdeclaration',
            constraint=models.UniqueConstraint(fields=('reporter', 'comment'), name='only_one_report2'),
        ),
        migrations.AddConstraint(
            model_name='articlesdeclaration',
            constraint=models.UniqueConstraint(fields=('reporter', 'articles'), name='only_one_report1'),
        ),
    ]
