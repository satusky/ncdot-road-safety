# Generated by Django 3.1.1 on 2020-10-16 00:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rs_core', '0002_routeimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnnotationSet',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('pt', 'Point'), ('cont', 'Continuous')], default='pt', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ImageAnnotation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_base_name', models.CharField(db_index=True, max_length=20)),
                ('annotation_name', models.CharField(max_length=100)),
                ('pred_centainty_score', models.FloatField(default=-1)),
                ('pred_timestamp', models.DateTimeField(blank=True, null=True)),
                ('feature_present', models.BooleanField(blank=True, null=True)),
                ('annotator_timestamp', models.DateTimeField(blank=True, null=True)),
                ('comment', models.CharField(blank=True, max_length=1000, null=True)),
                ('annotator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('image_base_name', 'annotation_name', 'annotator')},
            },
        ),
    ]
