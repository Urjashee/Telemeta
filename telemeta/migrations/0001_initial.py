# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import telemeta.models.fields
import telemeta.models.collection
import dirtyfields.dirtyfields
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AcquisitionMode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', telemeta.models.fields.CharField(default=b'', unique=True, max_length=250, verbose_name='value', blank=True)),
                ('notes', telemeta.models.fields.TextField(default=b'', verbose_name='notes', blank=True)),
            ],
            options={
                'ordering': ['value'],
                'db_table': 'acquisition_modes',
                'verbose_name': 'mode of acquisition',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.CreateModel(
            name='AdConversion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', telemeta.models.fields.CharField(default=b'', unique=True, max_length=250, verbose_name='value', blank=True)),
                ('notes', telemeta.models.fields.TextField(default=b'', verbose_name='notes', blank=True)),
            ],
            options={
                'ordering': ['value'],
                'db_table': 'ad_conversions',
                'verbose_name': 'A/D conversion',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.CreateModel(
            name='ContextKeyword',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', telemeta.models.fields.CharField(default=b'', unique=True, max_length=250, verbose_name='value', blank=True)),
                ('notes', telemeta.models.fields.TextField(default=b'', verbose_name='notes', blank=True)),
            ],
            options={
                'ordering': ['value'],
                'db_table': 'context_keywords',
                'verbose_name': 'keyword',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.CreateModel(
            name='CopyType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', telemeta.models.fields.CharField(default=b'', unique=True, max_length=250, verbose_name='value', blank=True)),
                ('notes', telemeta.models.fields.TextField(default=b'', verbose_name='notes', blank=True)),
            ],
            options={
                'ordering': ['value'],
                'db_table': 'copy_type',
                'verbose_name': 'copy type',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.CreateModel(
            name='Criteria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='key', blank=True)),
                ('value', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='value', blank=True)),
            ],
            options={
                'db_table': 'search_criteria',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.CreateModel(
            name='EthnicGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', telemeta.models.fields.CharField(default=b'', unique=True, max_length=250, verbose_name='value', blank=True)),
                ('notes', telemeta.models.fields.TextField(default=b'', verbose_name='notes', blank=True)),
            ],
            options={
                'ordering': ['value'],
                'db_table': 'ethnic_groups',
                'verbose_name': 'population / social group',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.CreateModel(
            name='EthnicGroupAlias',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='name', blank=True)),
                ('ethnic_group', telemeta.models.fields.ForeignKey(related_name='aliases', verbose_name='population / social group', to='telemeta.EthnicGroup')),
            ],
            options={
                'ordering': ['ethnic_group__value'],
                'db_table': 'ethnic_group_aliases',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.CreateModel(
            name='Format',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('original_code', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='original code', blank=True)),
                ('original_number', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='original number', blank=True)),
                ('original_status', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='original status', blank=True)),
                ('original_state', telemeta.models.fields.TextField(default=b'', verbose_name='technical properties / conservation state', blank=True)),
                ('original_comments', telemeta.models.fields.TextField(default=b'', verbose_name='comments / notes', blank=True)),
                ('original_audio_quality', telemeta.models.fields.TextField(default=b'', verbose_name='audio quality', blank=True)),
                ('recording_system', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='recording system', blank=True)),
                ('tape_thickness', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='tape thickness (um)', blank=True)),
                ('tape_reference', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='tape reference', blank=True)),
                ('sticker_presence', telemeta.models.fields.BooleanField(default=False, verbose_name='sticker presence')),
            ],
            options={
                'db_table': 'media_formats',
                'verbose_name': 'format',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.CreateModel(
            name='GenericStyle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', telemeta.models.fields.CharField(default=b'', unique=True, max_length=250, verbose_name='value', blank=True)),
                ('notes', telemeta.models.fields.TextField(default=b'', verbose_name='notes', blank=True)),
            ],
            options={
                'ordering': ['value'],
                'db_table': 'generic_styles',
                'verbose_name': 'generic style',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.CreateModel(
            name='IdentifierType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', telemeta.models.fields.CharField(default=b'', unique=True, max_length=250, verbose_name='value', blank=True)),
                ('notes', telemeta.models.fields.TextField(default=b'', verbose_name='notes', blank=True)),
            ],
            options={
                'ordering': ['value'],
                'db_table': 'identifier_type',
                'verbose_name': 'identifier type',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='name', blank=True)),
                ('notes', telemeta.models.fields.TextField(default=b'', verbose_name='notes', blank=True)),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'instruments',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.CreateModel(
            name='InstrumentAlias',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='name', blank=True)),
                ('notes', telemeta.models.fields.TextField(default=b'', verbose_name='notes', blank=True)),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'instrument_aliases',
                'verbose_name_plural': 'instrument aliases',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.CreateModel(
            name='InstrumentAliasRelation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('alias', telemeta.models.fields.ForeignKey(related_name='other_name', verbose_name='alias', to='telemeta.InstrumentAlias')),
                ('instrument', telemeta.models.fields.ForeignKey(related_name='relation', verbose_name='instrument', to='telemeta.Instrument')),
            ],
            options={
                'db_table': 'instrument_alias_relations',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.CreateModel(
            name='InstrumentRelation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('instrument', telemeta.models.fields.ForeignKey(related_name='parent_relation', verbose_name='instrument', to='telemeta.Instrument')),
                ('parent_instrument', telemeta.models.fields.ForeignKey(related_name='child_relation', verbose_name='parent instrument', to='telemeta.Instrument')),
            ],
            options={
                'db_table': 'instrument_relations',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identifier', telemeta.models.fields.CharField(default=b'', max_length=3, verbose_name='identifier', blank=True)),
                ('part2B', telemeta.models.fields.CharField(default=b'', max_length=3, verbose_name='equivalent ISO 639-2 identifier (bibliographic)', blank=True)),
                ('part2T', telemeta.models.fields.CharField(default=b'', max_length=3, verbose_name='equivalent ISO 639-2 identifier (terminologic)', blank=True)),
                ('part1', telemeta.models.fields.CharField(default=b'', max_length=1, verbose_name='equivalent ISO 639-1 identifier', blank=True)),
                ('scope', telemeta.models.fields.CharField(default=b'', max_length=1, verbose_name='scope', blank=True, choices=[(b'I', b'Individual'), (b'M', b'Macrolanguage'), (b'S', b'Special')])),
                ('type', telemeta.models.fields.CharField(default=b'', max_length=1, verbose_name='type', blank=True, choices=[(b'A', b'Ancient'), (b'C', b'Constructed'), (b'E', b'Extinct'), (b'H', b'Historical'), (b'L', b'Living'), (b'S', b'Special')])),
                ('name', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='name', blank=True)),
                ('comment', telemeta.models.fields.TextField(default=b'', verbose_name='comment', blank=True)),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'languages',
                'verbose_name_plural': 'languages',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.CreateModel(
            name='LegalRight',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', telemeta.models.fields.CharField(default=b'', unique=True, max_length=250, verbose_name='value', blank=True)),
                ('notes', telemeta.models.fields.TextField(default=b'', verbose_name='notes', blank=True)),
            ],
            options={
                'ordering': ['value'],
                'db_table': 'legal_rights',
                'verbose_name': 'legal rights',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', telemeta.models.fields.CharField(default=b'', unique=True, max_length=150, verbose_name='name', blank=True)),
                ('type', telemeta.models.fields.IntegerField(default=0, blank=True, verbose_name='type', db_index=True, choices=[(2, 'country'), (1, 'continent'), (0, 'other')])),
                ('latitude', telemeta.models.fields.FloatField(default=None, null=True, blank=True)),
                ('longitude', telemeta.models.fields.FloatField(default=None, null=True, blank=True)),
                ('is_authoritative', telemeta.models.fields.BooleanField(default=False, verbose_name='authoritative')),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'locations',
                'verbose_name': 'location',
                'verbose_name_plural': 'locations',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.CreateModel(
            name='LocationAlias',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('alias', telemeta.models.fields.CharField(default=b'', max_length=150, verbose_name='alias', blank=True)),
                ('is_authoritative', telemeta.models.fields.BooleanField(default=False, verbose_name='authoritative')),
                ('location', telemeta.models.fields.ForeignKey(related_name='aliases', verbose_name='location', to='telemeta.Location')),
            ],
            options={
                'ordering': ['alias'],
                'db_table': 'location_aliases',
                'verbose_name_plural': 'location aliases',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.CreateModel(
            name='LocationRelation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_direct', telemeta.models.fields.BooleanField(default=False, db_index=True)),
                ('is_authoritative', telemeta.models.fields.BooleanField(default=False, verbose_name='authoritative')),
                ('ancestor_location', telemeta.models.fields.ForeignKey(related_name='descendant_relations', verbose_name='ancestor location', to='telemeta.Location')),
                ('location', telemeta.models.fields.ForeignKey(related_name='ancestor_relations', verbose_name='location', to='telemeta.Location')),
            ],
            options={
                'ordering': ['ancestor_location__name'],
                'db_table': 'location_relations',
                'verbose_name_plural': 'location relations',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.CreateModel(
            name='LocationType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', telemeta.models.fields.CharField(default=b'', unique=True, max_length=64, verbose_name='identifier', blank=True)),
                ('name', telemeta.models.fields.CharField(default=b'', max_length=150, verbose_name='name', blank=True)),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'location_types',
                'verbose_name_plural': 'location types',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.CreateModel(
            name='MediaCollection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='title', blank=True)),
                ('alt_title', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='original title / translation', blank=True)),
                ('creator', telemeta.models.fields.CharField(default=b'', help_text='First name, Last name ; First name, Last name', max_length=250, verbose_name='depositor / contributor', blank=True)),
                ('description', telemeta.models.fields.TextField(default=b'', verbose_name='description', blank=True)),
                ('recorded_from_year', telemeta.models.fields.IntegerField(default=0, help_text='YYYY', verbose_name='recording year (from)', blank=True)),
                ('recorded_to_year', telemeta.models.fields.IntegerField(default=0, help_text='YYYY', verbose_name='recording year (until)', blank=True)),
                ('year_published', telemeta.models.fields.IntegerField(default=0, help_text='YYYY', verbose_name='year published', blank=True)),
                ('public_access', telemeta.models.fields.CharField(default=b'metadata', max_length=16, verbose_name='access type', blank=True, choices=[(b'none', 'none'), (b'metadata', 'metadata'), (b'mixed', 'mixed'), (b'full', 'full')])),
                ('collector', telemeta.models.fields.CharField(default=b'', help_text='First name, Last name ; First name, Last name', max_length=250, verbose_name='recordist', blank=True)),
                ('publisher_serial', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='publisher serial number', blank=True)),
                ('booklet_author', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='booklet author', blank=True)),
                ('reference', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='publisher reference', blank=True)),
                ('external_references', telemeta.models.fields.TextField(default=b'', verbose_name='bibliographic references', blank=True)),
                ('auto_period_access', telemeta.models.fields.BooleanField(default=True, verbose_name='automatic access after a rolling period')),
                ('code', telemeta.models.fields.CharField(default=b'', validators=[telemeta.models.collection.is_valid_collection_code], max_length=250, blank=True, unique=True, verbose_name='code')),
                ('old_code', telemeta.models.fields.CharField(default=None, max_length=250, null=True, verbose_name='old code', blank=True)),
                ('cnrs_contributor', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='CNRS depositor', blank=True)),
                ('booklet_description', telemeta.models.fields.TextField(default=b'', verbose_name='related documentation', blank=True)),
                ('alt_copies', telemeta.models.fields.TextField(default=b'', verbose_name='copies', blank=True)),
                ('comment', telemeta.models.fields.TextField(default=b'', verbose_name='comment', blank=True)),
                ('archiver_notes', telemeta.models.fields.TextField(default=b'', verbose_name='archiver notes', blank=True)),
                ('items_done', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='items finished', blank=True)),
                ('collector_is_creator', telemeta.models.fields.BooleanField(default=False, verbose_name='recordist identical to depositor')),
                ('is_published', telemeta.models.fields.BooleanField(default=False, verbose_name='published')),
                ('conservation_site', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='conservation site', blank=True)),
                ('approx_duration', telemeta.models.fields.DurationField(default=b'0', help_text=b'hh:mm:ss', verbose_name='estimated duration', blank=True)),
                ('physical_items_num', telemeta.models.fields.IntegerField(default=0, verbose_name='number of components (medium / piece)', blank=True)),
                ('alt_ids', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='copies (obsolete field)', blank=True)),
                ('travail', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='archiver notes (obsolete field)', blank=True)),
                ('acquisition_mode', telemeta.models.fields.WeakForeignKey(related_name='collections', default=None, blank=True, to='telemeta.AcquisitionMode', null=True, verbose_name='mode of acquisition')),
                ('ad_conversion', telemeta.models.fields.WeakForeignKey(related_name='collections', default=None, blank=True, to='telemeta.AdConversion', null=True, verbose_name='digitization')),
                ('copy_type', telemeta.models.fields.WeakForeignKey(related_name='collections', default=None, blank=True, to='telemeta.CopyType', null=True, verbose_name='copy type')),
                ('legal_rights', telemeta.models.fields.WeakForeignKey(related_name='collections', default=None, blank=True, to='telemeta.LegalRight', null=True, verbose_name='legal rights')),
            ],
            options={
                'ordering': ['code'],
                'db_table': 'media_collections',
                'verbose_name': 'collection',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.CreateModel(
            name='MediaCollectionIdentifier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identifier', models.CharField(unique=True, max_length=255, verbose_name='identifier', blank=True)),
                ('date_add', models.DateTimeField(auto_now_add=True, verbose_name='date added')),
                ('date_first', models.DateTimeField(verbose_name='date of first attribution')),
                ('date_last', models.DateTimeField(verbose_name='date of last attribution')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='date modified')),
                ('notes', models.TextField(null=True, verbose_name='notes')),
                ('collection', telemeta.models.fields.ForeignKey(related_name='identifiers', verbose_name='collection', to='telemeta.MediaCollection')),
                ('type', telemeta.models.fields.WeakForeignKey(default=None, blank=True, to='telemeta.IdentifierType', null=True, verbose_name='type')),
            ],
            options={
                'db_table': 'media_collection_identifier',
                'verbose_name': 'collection identifier',
                'verbose_name_plural': 'collection identifiers',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.CreateModel(
            name='MediaCollectionRelated',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='title', blank=True)),
                ('date', models.DateTimeField(auto_now=True, verbose_name='date')),
                ('description', telemeta.models.fields.TextField(default=b'', verbose_name='description', blank=True)),
                ('mime_type', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='mime_type', blank=True)),
                ('url', telemeta.models.fields.CharField(default=b'', max_length=500, verbose_name='url', blank=True)),
                ('credits', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='credits', blank=True)),
                ('file', telemeta.models.fields.FileField(db_column=b'filename', default=b'', upload_to=b'items/%Y/%m/%d', max_length=255, blank=True, verbose_name='file')),
                ('collection', telemeta.models.fields.ForeignKey(related_name='related', verbose_name='collection', to='telemeta.MediaCollection')),
            ],
            options={
                'db_table': 'media_collection_related',
                'verbose_name': 'collection related media',
                'verbose_name_plural': 'collection related media',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.CreateModel(
            name='MediaCorpus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250, verbose_name='title')),
                ('description', models.CharField(max_length=250, null=True, verbose_name='description_old', blank=True)),
                ('descriptions', models.TextField(verbose_name='description', blank=True)),
                ('code', models.CharField(unique=True, max_length=250, verbose_name='code')),
                ('public_access', models.CharField(default=b'metadata', max_length=16, verbose_name='public access', choices=[(b'none', 'none'), (b'metadata', 'metadata'), (b'mixed', 'mixed'), (b'full', 'full')])),
                ('recorded_from_year', telemeta.models.fields.IntegerField(default=0, help_text='YYYY', verbose_name='recording year (from)', blank=True)),
                ('recorded_to_year', telemeta.models.fields.IntegerField(default=0, help_text='YYYY', verbose_name='recording year (until)', blank=True)),
                ('children', models.ManyToManyField(related_name='corpus', verbose_name='collections', to='telemeta.MediaCollection', blank=True)),
            ],
            options={
                'ordering': ['code'],
                'db_table': 'media_corpus',
                'verbose_name': 'corpus',
                'verbose_name_plural': 'corpus',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.CreateModel(
            name='MediaCorpusRelated',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='title', blank=True)),
                ('date', models.DateTimeField(auto_now=True, verbose_name='date')),
                ('description', telemeta.models.fields.TextField(default=b'', verbose_name='description', blank=True)),
                ('mime_type', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='mime_type', blank=True)),
                ('url', telemeta.models.fields.CharField(default=b'', max_length=500, verbose_name='url', blank=True)),
                ('credits', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='credits', blank=True)),
                ('file', telemeta.models.fields.FileField(db_column=b'filename', default=b'', upload_to=b'items/%Y/%m/%d', max_length=255, blank=True, verbose_name='file')),
                ('resource', telemeta.models.fields.ForeignKey(related_name='related', verbose_name='corpus', to='telemeta.MediaCorpus')),
            ],
            options={
                'db_table': 'media_corpus_related',
                'verbose_name': 'corpus related media',
                'verbose_name_plural': 'corpus related media',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.CreateModel(
            name='MediaFonds',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250, verbose_name='title')),
                ('description', models.CharField(max_length=250, null=True, verbose_name='description_old', blank=True)),
                ('descriptions', models.TextField(verbose_name='description', blank=True)),
                ('code', models.CharField(unique=True, max_length=250, verbose_name='code')),
                ('public_access', models.CharField(default=b'metadata', max_length=16, verbose_name='public access', choices=[(b'none', 'none'), (b'metadata', 'metadata'), (b'mixed', 'mixed'), (b'full', 'full')])),
                ('children', models.ManyToManyField(related_name='fonds', verbose_name='corpus', to='telemeta.MediaCorpus', blank=True)),
            ],
            options={
                'ordering': ['code'],
                'db_table': 'media_fonds',
                'verbose_name': 'fonds',
                'verbose_name_plural': 'fonds',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.CreateModel(
            name='MediaFondsRelated',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='title', blank=True)),
                ('date', models.DateTimeField(auto_now=True, verbose_name='date')),
                ('description', telemeta.models.fields.TextField(default=b'', verbose_name='description', blank=True)),
                ('mime_type', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='mime_type', blank=True)),
                ('url', telemeta.models.fields.CharField(default=b'', max_length=500, verbose_name='url', blank=True)),
                ('credits', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='credits', blank=True)),
                ('file', telemeta.models.fields.FileField(db_column=b'filename', default=b'', upload_to=b'items/%Y/%m/%d', max_length=255, blank=True, verbose_name='file')),
                ('resource', telemeta.models.fields.ForeignKey(related_name='related', verbose_name='fonds', to='telemeta.MediaFonds')),
            ],
            options={
                'db_table': 'media_fonds_related',
                'verbose_name': 'fonds related media',
                'verbose_name_plural': 'fonds related media',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.CreateModel(
            name='MediaItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='title', blank=True)),
                ('alt_title', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='original title / translation', blank=True)),
                ('collector', telemeta.models.fields.CharField(default=b'', help_text='First name, Last name ; First name, Last name', max_length=250, verbose_name='collector', blank=True)),
                ('recorded_from_date', telemeta.models.fields.DateField(default=None, help_text='YYYY-MM-DD', null=True, verbose_name='recording date (from)', blank=True)),
                ('recorded_to_date', telemeta.models.fields.DateField(default=None, help_text='YYYY-MM-DD', null=True, verbose_name='recording date (until)', blank=True)),
                ('public_access', telemeta.models.fields.CharField(default=b'metadata', max_length=16, verbose_name='access type', blank=True, choices=[(b'none', 'none'), (b'metadata', 'metadata'), (b'full', 'full')])),
                ('location_comment', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='location details', blank=True)),
                ('cultural_area', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='cultural area', blank=True)),
                ('language', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='language', blank=True)),
                ('context_comment', telemeta.models.fields.TextField(default=b'', verbose_name='Ethnographic context', blank=True)),
                ('moda_execut', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='implementing rules', blank=True)),
                ('author', telemeta.models.fields.CharField(default=b'', help_text='First name, Last name ; First name, Last name', max_length=250, verbose_name='author / compositor', blank=True)),
                ('depositor', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='depositor', blank=True)),
                ('code', telemeta.models.fields.CharField(default=b'', max_length=250, blank=True, help_text='CollectionCode_ItemCode', unique=True, verbose_name='code')),
                ('old_code', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='original code', blank=True)),
                ('track', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='item number', blank=True)),
                ('collector_selection', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='collector selection', blank=True)),
                ('collector_from_collection', telemeta.models.fields.BooleanField(default=False, verbose_name='collector as in collection')),
                ('creator_reference', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='creator reference', blank=True)),
                ('external_references', telemeta.models.fields.TextField(default=b'', verbose_name='published references', blank=True)),
                ('auto_period_access', telemeta.models.fields.BooleanField(default=True, verbose_name='automatic access after a rolling period')),
                ('comment', telemeta.models.fields.TextField(default=b'', verbose_name='remarks', blank=True)),
                ('approx_duration', telemeta.models.fields.DurationField(default=b'0', help_text='hh:mm:ss', verbose_name='approximative duration', blank=True)),
                ('mimetype', telemeta.models.fields.CharField(default=b'', max_length=255, verbose_name='mime type', blank=True)),
                ('file', telemeta.models.fields.FileField(db_column=b'filename', default=b'', upload_to=b'items/%Y/%m/%d', max_length=1024, blank=True, verbose_name='file')),
                ('url', models.URLField(max_length=512, verbose_name='URL', blank=True)),
                ('recordist', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='recordist', blank=True)),
                ('digitalist', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='digitalist', blank=True)),
                ('digitization_date', telemeta.models.fields.DateField(default=None, null=True, verbose_name='digitization date', blank=True)),
                ('publishing_date', telemeta.models.fields.DateField(default=None, null=True, verbose_name='publishing date', blank=True)),
                ('scientist', telemeta.models.fields.CharField(default=b'', help_text='First name, Last name ; First name, Last name', max_length=250, verbose_name='scientist', blank=True)),
                ('summary', telemeta.models.fields.TextField(default=b'', verbose_name='summary', blank=True)),
                ('contributor', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='contributor', blank=True)),
                ('collection', telemeta.models.fields.ForeignKey(related_name='items', verbose_name='collection', to='telemeta.MediaCollection')),
                ('ethnic_group', telemeta.models.fields.WeakForeignKey(related_name='items', default=None, blank=True, to='telemeta.EthnicGroup', null=True, verbose_name='population / social group')),
                ('generic_style', telemeta.models.fields.WeakForeignKey(related_name='items', default=None, blank=True, to='telemeta.GenericStyle', null=True, verbose_name='generic style')),
                ('language_iso', telemeta.models.fields.ForeignKey(related_name='items', on_delete=django.db.models.deletion.SET_NULL, default=None, blank=True, to='telemeta.Language', null=True, verbose_name='Language (ISO norm)')),
                ('location', telemeta.models.fields.WeakForeignKey(default=None, blank=True, to='telemeta.Location', null=True, verbose_name='location')),
            ],
            options={
                'db_table': 'media_items',
                'verbose_name': 'item',
                'permissions': (('can_play_all_items', 'Can play all media items'), ('can_download_all_items', 'Can download all media items')),
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.CreateModel(
            name='MediaItemAnalysis',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('analyzer_id', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='id', blank=True)),
                ('name', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='name', blank=True)),
                ('value', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='value', blank=True)),
                ('unit', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='unit', blank=True)),
                ('item', telemeta.models.fields.ForeignKey(related_name='analysis', verbose_name='item', to='telemeta.MediaItem')),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'media_analysis',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.CreateModel(
            name='MediaItemIdentifier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identifier', models.CharField(unique=True, max_length=255, verbose_name='identifier', blank=True)),
                ('date_add', models.DateTimeField(auto_now_add=True, verbose_name='date added')),
                ('date_first', models.DateTimeField(verbose_name='date of first attribution')),
                ('date_last', models.DateTimeField(verbose_name='date of last attribution')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='date modified')),
                ('notes', models.TextField(null=True, verbose_name='notes')),
                ('item', telemeta.models.fields.ForeignKey(related_name='identifiers', verbose_name='item', to='telemeta.MediaItem')),
                ('type', telemeta.models.fields.WeakForeignKey(default=None, blank=True, to='telemeta.IdentifierType', null=True, verbose_name='type')),
            ],
            options={
                'db_table': 'media_item_identifier',
                'verbose_name': 'item identifier',
                'verbose_name_plural': 'item identifiers',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.CreateModel(
            name='MediaItemKeyword',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item', telemeta.models.fields.ForeignKey(related_name='keyword_relations', verbose_name='item', to='telemeta.MediaItem')),
                ('keyword', telemeta.models.fields.ForeignKey(related_name='item_relations', verbose_name='keyword', to='telemeta.ContextKeyword')),
            ],
            options={
                'db_table': 'media_item_keywords',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.CreateModel(
            name='MediaItemMarker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('public_id', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='public_id', blank=True)),
                ('time', telemeta.models.fields.FloatField(default=0, verbose_name='time (s)', blank=True)),
                ('title', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='title', blank=True)),
                ('date', models.DateTimeField(auto_now=True, verbose_name='date')),
                ('description', telemeta.models.fields.TextField(default=b'', verbose_name='description', blank=True)),
                ('author', telemeta.models.fields.ForeignKey(related_name='markers', default=None, blank=True, to=settings.AUTH_USER_MODEL, null=True, verbose_name='author')),
                ('item', telemeta.models.fields.ForeignKey(related_name='markers', verbose_name='item', to='telemeta.MediaItem')),
            ],
            options={
                'ordering': ['time'],
                'db_table': 'media_markers',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.CreateModel(
            name='MediaItemPerformance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('instruments_num', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='number', blank=True)),
                ('musicians', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='interprets', blank=True)),
                ('alias', telemeta.models.fields.WeakForeignKey(related_name='performances', default=None, blank=True, to='telemeta.InstrumentAlias', null=True, verbose_name='vernacular name')),
                ('instrument', telemeta.models.fields.WeakForeignKey(related_name='performances', default=None, blank=True, to='telemeta.Instrument', null=True, verbose_name='composition')),
                ('media_item', telemeta.models.fields.ForeignKey(related_name='performances', verbose_name='item', to='telemeta.MediaItem')),
            ],
            options={
                'db_table': 'media_item_performances',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.CreateModel(
            name='MediaItemRelated',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='title', blank=True)),
                ('date', models.DateTimeField(auto_now=True, verbose_name='date')),
                ('description', telemeta.models.fields.TextField(default=b'', verbose_name='description', blank=True)),
                ('mime_type', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='mime_type', blank=True)),
                ('url', telemeta.models.fields.CharField(default=b'', max_length=500, verbose_name='url', blank=True)),
                ('credits', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='credits', blank=True)),
                ('file', telemeta.models.fields.FileField(db_column=b'filename', default=b'', upload_to=b'items/%Y/%m/%d', max_length=255, blank=True, verbose_name='file')),
                ('item', telemeta.models.fields.ForeignKey(related_name='related', verbose_name='item', to='telemeta.MediaItem')),
            ],
            options={
                'db_table': 'media_item_related',
                'verbose_name': 'item related media',
                'verbose_name_plural': 'item related media',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.CreateModel(
            name='MediaItemTranscoded',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mimetype', models.CharField(max_length=255, verbose_name='mime_type', blank=True)),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='date')),
                ('status', models.IntegerField(default=1, verbose_name='status', choices=[(0, 'broken'), (1, 'pending'), (2, 'processing'), (3, 'done'), (5, 'ready')])),
                ('file', models.FileField(upload_to=b'items/%Y/%m/%d', max_length=1024, verbose_name='file', blank=True)),
                ('item', models.ForeignKey(related_name='transcoded', verbose_name='item', to='telemeta.MediaItem')),
            ],
            options={
                'db_table': 'telemeta_media_transcoded',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.CreateModel(
            name='MediaItemTranscodingFlag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mime_type', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='mime_type', blank=True)),
                ('date', models.DateTimeField(auto_now=True, verbose_name='date')),
                ('value', telemeta.models.fields.BooleanField(default=False, verbose_name='transcoded')),
                ('item', telemeta.models.fields.ForeignKey(related_name='transcoding', verbose_name='item', to='telemeta.MediaItem')),
            ],
            options={
                'db_table': 'media_transcoding',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.CreateModel(
            name='MediaPart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='title', blank=True)),
                ('start', telemeta.models.fields.FloatField(default=0, verbose_name='start', blank=True)),
                ('end', telemeta.models.fields.FloatField(default=0, verbose_name='end', blank=True)),
                ('item', telemeta.models.fields.ForeignKey(related_name='parts', verbose_name='item', to='telemeta.MediaItem')),
            ],
            options={
                'db_table': 'media_parts',
                'verbose_name': 'item part',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.CreateModel(
            name='MediaType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', telemeta.models.fields.CharField(default=b'', unique=True, max_length=250, verbose_name='value', blank=True)),
                ('notes', telemeta.models.fields.TextField(default=b'', verbose_name='notes', blank=True)),
            ],
            options={
                'ordering': ['value'],
                'db_table': 'media_type',
                'verbose_name': 'media type',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.CreateModel(
            name='MetadataAuthor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', telemeta.models.fields.CharField(default=b'', unique=True, max_length=250, verbose_name='value', blank=True)),
                ('notes', telemeta.models.fields.TextField(default=b'', verbose_name='notes', blank=True)),
            ],
            options={
                'ordering': ['value'],
                'db_table': 'metadata_authors',
                'verbose_name': 'record author',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.CreateModel(
            name='MetadataWriter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', telemeta.models.fields.CharField(default=b'', unique=True, max_length=250, verbose_name='value', blank=True)),
                ('notes', telemeta.models.fields.TextField(default=b'', verbose_name='notes', blank=True)),
            ],
            options={
                'ordering': ['value'],
                'db_table': 'metadata_writers',
                'verbose_name': 'record writer',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.CreateModel(
            name='NumberOfChannels',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', telemeta.models.fields.CharField(default=b'', unique=True, max_length=250, verbose_name='value', blank=True)),
                ('notes', telemeta.models.fields.TextField(default=b'', verbose_name='notes', blank=True)),
            ],
            options={
                'ordering': ['value'],
                'db_table': 'original_channel_number',
                'verbose_name': 'number of channels',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', telemeta.models.fields.CharField(default=b'', unique=True, max_length=250, verbose_name='value', blank=True)),
                ('notes', telemeta.models.fields.TextField(default=b'', verbose_name='notes', blank=True)),
            ],
            options={
                'ordering': ['value'],
                'db_table': 'organization',
                'verbose_name': 'organization',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.CreateModel(
            name='OriginalFormat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', telemeta.models.fields.CharField(default=b'', unique=True, max_length=250, verbose_name='value', blank=True)),
                ('notes', telemeta.models.fields.TextField(default=b'', verbose_name='notes', blank=True)),
            ],
            options={
                'ordering': ['value'],
                'db_table': 'original_format',
                'verbose_name': 'original format',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.CreateModel(
            name='PhysicalFormat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', telemeta.models.fields.CharField(default=b'', unique=True, max_length=250, verbose_name='value', blank=True)),
                ('notes', telemeta.models.fields.TextField(default=b'', verbose_name='notes', blank=True)),
            ],
            options={
                'ordering': ['value'],
                'db_table': 'physical_formats',
                'verbose_name': 'archive format',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('public_id', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='public_id', blank=True)),
                ('title', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='title', blank=True)),
                ('description', telemeta.models.fields.TextField(default=b'', verbose_name='description', blank=True)),
                ('author', telemeta.models.fields.ForeignKey(related_name='playlists', db_column=b'author', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'playlists',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.CreateModel(
            name='PlaylistResource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('public_id', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='public_id', blank=True)),
                ('resource_type', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='resource_type', blank=True, choices=[(b'item', b'item'), (b'collection', b'collection'), (b'marker', b'marker'), (b'fonds', b'fonds'), (b'corpus', b'corpus')])),
                ('resource_id', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='resource_id', blank=True)),
                ('playlist', telemeta.models.fields.ForeignKey(related_name='resources', verbose_name='playlist', to='telemeta.Playlist')),
            ],
            options={
                'db_table': 'playlist_resources',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', telemeta.models.fields.CharField(default=b'', unique=True, max_length=250, verbose_name='value', blank=True)),
                ('notes', telemeta.models.fields.TextField(default=b'', verbose_name='notes', blank=True)),
            ],
            options={
                'ordering': ['value'],
                'db_table': 'publishers',
                'verbose_name': 'publisher',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.CreateModel(
            name='PublisherCollection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='value', blank=True)),
                ('publisher', telemeta.models.fields.ForeignKey(related_name='publisher_collections', verbose_name='publisher', to='telemeta.Publisher')),
            ],
            options={
                'ordering': ['value'],
                'db_table': 'publisher_collections',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.CreateModel(
            name='PublishingStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', telemeta.models.fields.CharField(default=b'', unique=True, max_length=250, verbose_name='value', blank=True)),
                ('notes', telemeta.models.fields.TextField(default=b'', verbose_name='notes', blank=True)),
            ],
            options={
                'ordering': ['value'],
                'db_table': 'publishing_status',
                'verbose_name': 'secondary edition',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.CreateModel(
            name='RecordingContext',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', telemeta.models.fields.CharField(default=b'', unique=True, max_length=250, verbose_name='value', blank=True)),
                ('notes', telemeta.models.fields.TextField(default=b'', verbose_name='notes', blank=True)),
            ],
            options={
                'ordering': ['value'],
                'db_table': 'recording_contexts',
                'verbose_name': 'recording context',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.CreateModel(
            name='Revision',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('element_type', telemeta.models.fields.CharField(default=b'', max_length=16, verbose_name='element type', blank=True, choices=[(b'collection', b'collection'), (b'item', b'item'), (b'part', b'part'), (b'marker', b'marker'), (b'media', b'media'), (b'fonds', b'fonds'), (b'corpus', b'corpus')])),
                ('element_id', telemeta.models.fields.IntegerField(default=0, verbose_name='element identifier', blank=True)),
                ('change_type', telemeta.models.fields.CharField(default=b'', max_length=16, verbose_name='modification type', blank=True, choices=[(b'import', b'import'), (b'create', b'create'), (b'update', b'update'), (b'delete', b'delete')])),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='time')),
                ('user', telemeta.models.fields.ForeignKey(related_name='revisions', db_column=b'username', verbose_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-time'],
                'db_table': 'revisions',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.CreateModel(
            name='Rights',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', telemeta.models.fields.CharField(default=b'', unique=True, max_length=250, verbose_name='value', blank=True)),
                ('notes', telemeta.models.fields.TextField(default=b'', verbose_name='notes', blank=True)),
            ],
            options={
                'ordering': ['value'],
                'db_table': 'rights',
                'verbose_name': 'rights',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='date')),
                ('description', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='Description', blank=True)),
                ('criteria', models.ManyToManyField(related_name='search', verbose_name='criteria', to='telemeta.Criteria', blank=True)),
                ('username', telemeta.models.fields.ForeignKey(related_name='searches', db_column=b'username', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date'],
                'db_table': 'searches',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', telemeta.models.fields.CharField(default=b'', unique=True, max_length=250, verbose_name='value', blank=True)),
                ('notes', telemeta.models.fields.TextField(default=b'', verbose_name='notes', blank=True)),
            ],
            options={
                'ordering': ['value'],
                'db_table': 'media_status',
                'verbose_name': 'collection status',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.CreateModel(
            name='TapeLength',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', telemeta.models.fields.CharField(default=b'', unique=True, max_length=250, verbose_name='value', blank=True)),
                ('notes', telemeta.models.fields.TextField(default=b'', verbose_name='notes', blank=True)),
            ],
            options={
                'ordering': ['value'],
                'db_table': 'tape_length',
                'verbose_name': 'tape length (cm)',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.CreateModel(
            name='TapeSpeed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', telemeta.models.fields.CharField(default=b'', unique=True, max_length=250, verbose_name='value', blank=True)),
                ('notes', telemeta.models.fields.TextField(default=b'', verbose_name='notes', blank=True)),
            ],
            options={
                'ordering': ['value'],
                'db_table': 'tape_speed',
                'verbose_name': 'tape speed (cm/s)',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.CreateModel(
            name='TapeVendor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', telemeta.models.fields.CharField(default=b'', unique=True, max_length=250, verbose_name='value', blank=True)),
                ('notes', telemeta.models.fields.TextField(default=b'', verbose_name='notes', blank=True)),
            ],
            options={
                'ordering': ['value'],
                'db_table': 'tape_vendor',
                'verbose_name': 'tape brand',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.CreateModel(
            name='TapeWheelDiameter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', telemeta.models.fields.CharField(default=b'', unique=True, max_length=250, verbose_name='value', blank=True)),
                ('notes', telemeta.models.fields.TextField(default=b'', verbose_name='notes', blank=True)),
            ],
            options={
                'ordering': ['value'],
                'db_table': 'tape_wheel_diameter',
                'verbose_name': 'tape wheel diameter (cm)',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.CreateModel(
            name='TapeWidth',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', telemeta.models.fields.CharField(default=b'', unique=True, max_length=250, verbose_name='value', blank=True)),
                ('notes', telemeta.models.fields.TextField(default=b'', verbose_name='notes', blank=True)),
            ],
            options={
                'ordering': ['value'],
                'db_table': 'tape_width',
                'verbose_name': 'tape width (inch)',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', telemeta.models.fields.CharField(default=b'', unique=True, max_length=250, verbose_name='value', blank=True)),
                ('notes', telemeta.models.fields.TextField(default=b'', verbose_name='notes', blank=True)),
            ],
            options={
                'ordering': ['value'],
                'db_table': 'topic',
                'verbose_name': 'topic',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('institution', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='Institution', blank=True)),
                ('department', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='Department', blank=True)),
                ('attachment', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='Attachment', blank=True)),
                ('function', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='Function', blank=True)),
                ('address', telemeta.models.fields.TextField(default=b'', verbose_name='Address', blank=True)),
                ('telephone', telemeta.models.fields.CharField(default=b'', max_length=250, verbose_name='Telephone', blank=True)),
                ('expiration_date', telemeta.models.fields.DateField(default=None, null=True, verbose_name='Expiration_date', blank=True)),
                ('user', telemeta.models.fields.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True)),
            ],
            options={
                'db_table': 'profiles',
                'permissions': (('can_view_users_and_profiles', 'Can view other users and any profile'),),
            },
        ),
        migrations.CreateModel(
            name='VernacularStyle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', telemeta.models.fields.CharField(default=b'', unique=True, max_length=250, verbose_name='value', blank=True)),
                ('notes', telemeta.models.fields.TextField(default=b'', verbose_name='notes', blank=True)),
            ],
            options={
                'ordering': ['value'],
                'db_table': 'vernacular_styles',
                'verbose_name': 'vernacular style',
            },
            bases=(models.Model, dirtyfields.dirtyfields.DirtyFieldsMixin),
        ),
        migrations.AddField(
            model_name='mediaitem',
            name='media_type',
            field=telemeta.models.fields.WeakForeignKey(related_name='items', default=None, blank=True, to='telemeta.MediaType', null=True, verbose_name='media type'),
        ),
        migrations.AddField(
            model_name='mediaitem',
            name='organization',
            field=telemeta.models.fields.WeakForeignKey(default=None, blank=True, to='telemeta.Organization', null=True, verbose_name='organization'),
        ),
        migrations.AddField(
            model_name='mediaitem',
            name='rights',
            field=telemeta.models.fields.WeakForeignKey(default=None, blank=True, to='telemeta.Rights', null=True, verbose_name='rights'),
        ),
        migrations.AddField(
            model_name='mediaitem',
            name='topic',
            field=telemeta.models.fields.WeakForeignKey(default=None, blank=True, to='telemeta.Topic', null=True, verbose_name='topic'),
        ),
        migrations.AddField(
            model_name='mediaitem',
            name='vernacular_style',
            field=telemeta.models.fields.WeakForeignKey(related_name='items', default=None, blank=True, to='telemeta.VernacularStyle', null=True, verbose_name='vernacular style'),
        ),
        migrations.AddField(
            model_name='mediacollection',
            name='media_type',
            field=telemeta.models.fields.WeakForeignKey(related_name='collections', default=None, blank=True, to='telemeta.MediaType', null=True, verbose_name='media type'),
        ),
        migrations.AddField(
            model_name='mediacollection',
            name='metadata_author',
            field=telemeta.models.fields.WeakForeignKey(related_name='collections', default=None, blank=True, to='telemeta.MetadataAuthor', null=True, verbose_name='record author'),
        ),
        migrations.AddField(
            model_name='mediacollection',
            name='metadata_writer',
            field=telemeta.models.fields.WeakForeignKey(related_name='collections', default=None, blank=True, to='telemeta.MetadataWriter', null=True, verbose_name='record writer'),
        ),
        migrations.AddField(
            model_name='mediacollection',
            name='original_format',
            field=telemeta.models.fields.WeakForeignKey(related_name='collections', default=None, blank=True, to='telemeta.OriginalFormat', null=True, verbose_name='original format'),
        ),
        migrations.AddField(
            model_name='mediacollection',
            name='physical_format',
            field=telemeta.models.fields.WeakForeignKey(related_name='collections', default=None, blank=True, to='telemeta.PhysicalFormat', null=True, verbose_name='archive format'),
        ),
        migrations.AddField(
            model_name='mediacollection',
            name='publisher',
            field=telemeta.models.fields.WeakForeignKey(related_name='collections', default=None, blank=True, to='telemeta.Publisher', null=True, verbose_name='publisher'),
        ),
        migrations.AddField(
            model_name='mediacollection',
            name='publisher_collection',
            field=telemeta.models.fields.WeakForeignKey(related_name='collections', default=None, blank=True, to='telemeta.PublisherCollection', null=True, verbose_name='publisher collection'),
        ),
        migrations.AddField(
            model_name='mediacollection',
            name='publishing_status',
            field=telemeta.models.fields.WeakForeignKey(related_name='collections', default=None, blank=True, to='telemeta.PublishingStatus', null=True, verbose_name='secondary edition'),
        ),
        migrations.AddField(
            model_name='mediacollection',
            name='recording_context',
            field=telemeta.models.fields.WeakForeignKey(related_name='collections', default=None, blank=True, to='telemeta.RecordingContext', null=True, verbose_name='recording context'),
        ),
        migrations.AddField(
            model_name='mediacollection',
            name='status',
            field=telemeta.models.fields.WeakForeignKey(related_name='collections', default=None, blank=True, to='telemeta.Status', null=True, verbose_name='collection status'),
        ),
        migrations.AddField(
            model_name='location',
            name='complete_type',
            field=telemeta.models.fields.ForeignKey(related_name='locations', verbose_name='complete type', to='telemeta.LocationType'),
        ),
        migrations.AddField(
            model_name='location',
            name='current_location',
            field=telemeta.models.fields.WeakForeignKey(related_name='past_names', default=None, blank=True, to='telemeta.Location', null=True, verbose_name='current location'),
        ),
        migrations.AddField(
            model_name='format',
            name='item',
            field=telemeta.models.fields.ForeignKey(related_name='format', on_delete=django.db.models.deletion.SET_NULL, default=None, blank=True, to='telemeta.MediaItem', null=True, verbose_name='item'),
        ),
        migrations.AddField(
            model_name='format',
            name='original_channels',
            field=telemeta.models.fields.WeakForeignKey(related_name='format', default=None, blank=True, to='telemeta.NumberOfChannels', null=True, verbose_name='number of channels'),
        ),
        migrations.AddField(
            model_name='format',
            name='original_location',
            field=telemeta.models.fields.ForeignKey(related_name='format', on_delete=django.db.models.deletion.SET_NULL, default=None, blank=True, to='telemeta.Location', null=True, verbose_name='original location'),
        ),
        migrations.AddField(
            model_name='format',
            name='physical_format',
            field=telemeta.models.fields.WeakForeignKey(related_name='format', default=None, blank=True, to='telemeta.PhysicalFormat', null=True, verbose_name='physical format'),
        ),
        migrations.AddField(
            model_name='format',
            name='tape_speed',
            field=telemeta.models.fields.WeakForeignKey(related_name='format', default=None, blank=True, to='telemeta.TapeSpeed', null=True, verbose_name='tape speed (cm/s)'),
        ),
        migrations.AddField(
            model_name='format',
            name='tape_vendor',
            field=telemeta.models.fields.WeakForeignKey(related_name='format', default=None, blank=True, to='telemeta.TapeVendor', null=True, verbose_name='tape vendor'),
        ),
        migrations.AddField(
            model_name='format',
            name='tape_wheel_diameter',
            field=telemeta.models.fields.WeakForeignKey(related_name='format', default=None, blank=True, to='telemeta.TapeWheelDiameter', null=True, verbose_name='tape wheel diameter (cm)'),
        ),
        migrations.AlterUniqueTogether(
            name='mediaitemkeyword',
            unique_together=set([('item', 'keyword')]),
        ),
        migrations.AlterUniqueTogether(
            name='mediaitemidentifier',
            unique_together=set([('identifier', 'item')]),
        ),
        migrations.AlterUniqueTogether(
            name='mediacollectionidentifier',
            unique_together=set([('identifier', 'collection')]),
        ),
        migrations.AlterUniqueTogether(
            name='locationrelation',
            unique_together=set([('location', 'ancestor_location')]),
        ),
        migrations.AlterUniqueTogether(
            name='locationalias',
            unique_together=set([('location', 'alias')]),
        ),
        migrations.AlterUniqueTogether(
            name='instrumentrelation',
            unique_together=set([('instrument', 'parent_instrument')]),
        ),
        migrations.AlterUniqueTogether(
            name='instrumentaliasrelation',
            unique_together=set([('alias', 'instrument')]),
        ),
        migrations.AlterUniqueTogether(
            name='ethnicgroupalias',
            unique_together=set([('ethnic_group', 'value')]),
        ),
    ]
