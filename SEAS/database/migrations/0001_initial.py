# Generated by Django 3.2.7 on 2021-12-01 10:16

import database.models
from django.db import migrations, models
import django.db.models.deletion
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassroomT',
            fields=[
                ('cRoom_ID', database.models.FixedCharField(db_column='cRoom_ID', max_length=10, primary_key=True, serialize=False)),
                ('nRoomCapacity', models.IntegerField(blank=True, db_column='nRoomCapacity', null=True)),
            ],
            options={
                'db_table': 'Classroom_T',
            },
        ),
        migrations.CreateModel(
            name='FacultyT',
            fields=[
                ('cFaculty_ID', database.models.FixedCharField(db_column='cFaculty_ID', max_length=4, primary_key=True, serialize=False)),
                ('cFacultyName', models.CharField(blank=True, db_column='cFacultyName', max_length=50, null=True)),
            ],
            options={
                'db_table': 'Faculty_T',
            },
        ),
        migrations.CreateModel(
            name='SchoolT',
            fields=[
                ('cSchool_ID', database.models.FixedCharField(db_column='cSchool_ID', max_length=5, primary_key=True, serialize=False)),
                ('cSchoolName', models.CharField(blank=True, db_column='cSchoolName', max_length=50, null=True)),
            ],
            options={
                'db_table': 'School_T',
            },
        ),
        migrations.CreateModel(
            name='DepartmentT',
            fields=[
                ('cDepartment_ID', database.models.FixedCharField(db_column='cDepartment_ID', max_length=5, primary_key=True, serialize=False)),
                ('cDepartmentName', models.CharField(blank=True, db_column='cDepartmentName', max_length=50, null=True)),
                ('cSchool_ID', models.ForeignKey(blank=True, db_column='cSchool_ID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='database.schoolt')),
            ],
            options={
                'db_table': 'Department_T',
            },
        ),
        migrations.CreateModel(
            name='CourseT',
            fields=[
                ('cCourse_ID', database.models.FixedCharField(db_column='cCourse_ID', max_length=7, primary_key=True, serialize=False)),
                ('cCourseName', models.CharField(blank=True, db_column='cCourseName', max_length=50, null=True)),
                ('nCreditHours', models.IntegerField(blank=True, db_column='nCreditHours', null=True)),
                ('cDepartment_ID', models.ForeignKey(blank=True, db_column='cDepartment_ID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='database.departmentt')),
            ],
            options={
                'db_table': 'Course_T',
            },
        ),
        migrations.CreateModel(
            name='CoofferedcourseT',
            fields=[
                ('cCoffCode_ID', database.models.FixedCharField(db_column='cCoffCode_ID', max_length=7, primary_key=True, serialize=False)),
                ('cCourse_ID', models.ForeignKey(blank=True, db_column='cCourse_ID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='database.courset')),
            ],
            options={
                'db_table': 'CoOfferedCourse_T',
            },
        ),
        migrations.CreateModel(
            name='SectionT',
            fields=[
                ('section_id', models.BigAutoField(db_column='section_ID', primary_key=True, serialize=False)),
                ('eSession', django_mysql.models.EnumField(choices=[('Autumn', 'Autumn'), ('Summer', 'Summer'), ('Spring', 'Spring')], db_column='eSession')),
                ('eDays', django_mysql.models.EnumField(blank=True, choices=[('ST', 'ST'), ('MW', 'MW'), ('S', 'S'), ('M', 'M'), ('T', 'T'), ('W', 'W'), ('R', 'R'), ('F', 'F'), ('A', 'A'), ('AR', 'AR'), ('TR', 'TR'), ('MWA', 'MWA'), ('STR', 'STR'), ('AMW', 'AMW'), ('SMW', 'SMW')], db_column='eDays', null=True)),
                ('dYear', database.models.YearField(db_column='dYear')),
                ('nSectionNumber', models.IntegerField(blank=True, db_column='nSectionNumber', null=True)),
                ('nSectionCapacity', models.IntegerField(blank=True, db_column='nSectionCapacity', null=True)),
                ('nEnrolled', models.IntegerField(blank=True, db_column='nEnrolled', null=True)),
                ('bIsBlocked', models.BooleanField(blank=True, db_column='bIsBlocked', null=True)),
                ('tStartTime', database.models.TimeField(blank=True, db_column='tStartTime', max_length=4, null=True)),
                ('tEndTime', database.models.TimeField(blank=True, db_column='tEndTime', max_length=4, null=True)),
                ('cCoffCode_ID', models.ForeignKey(blank=True, db_column='cCoffCode_ID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='database.coofferedcourset')),
                ('cFaculty_ID', models.ForeignKey(blank=True, db_column='cFaculty_ID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='database.facultyt')),
                ('cRoom_ID', models.ForeignKey(blank=True, db_column='cRoom_ID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='database.classroomt')),
            ],
            options={
                'db_table': 'Section_T',
                'unique_together': {('cCoffCode_ID', 'eSession', 'dYear', 'nSectionNumber')},
            },
        ),
    ]
