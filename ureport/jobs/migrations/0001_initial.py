# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('orgs', '0008_org_timezone'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='JobSource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True, help_text=b'Whether this item is active, use this instead of deleting')),
                ('created_on', models.DateTimeField(help_text=b'When this item was originally created', auto_now_add=True)),
                ('modified_on', models.DateTimeField(help_text=b'When this item was last modified', auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('source_type', models.CharField(max_length=1, choices=[(b'T', b'Twitter'), (b'F', b'Facebook'), (b'R', b'RSS')])),
                ('source_url', models.URLField()),
                ('widget_id', models.CharField(max_length=50, null=True, blank=True)),
                ('is_featured', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(related_name='jobs_jobsource_creations', to=settings.AUTH_USER_MODEL, help_text=b'The user which originally created this item')),
                ('modified_by', models.ForeignKey(related_name='jobs_jobsource_modifications', to=settings.AUTH_USER_MODEL, help_text=b'The user which last modified this item')),
                ('org', models.ForeignKey(help_text='The organization this job source is for', to='orgs.Org')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
