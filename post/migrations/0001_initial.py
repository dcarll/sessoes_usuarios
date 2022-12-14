# Generated by Django 4.1 on 2022-08-05 01:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Base',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('data_publicacao', models.DateField(auto_now=True, verbose_name='Publicacao')),
            ],
        ),
        migrations.CreateModel(
            name='Postagem',
            fields=[
                ('base_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='post.base')),
                ('titulo', models.CharField(max_length=255)),
                ('conteudo', models.TextField()),
                ('autor', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Autor')),
            ],
            bases=('post.base',),
        ),
    ]
