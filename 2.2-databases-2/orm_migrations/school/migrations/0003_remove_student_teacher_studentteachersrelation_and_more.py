# Generated by Django 4.2.3 on 2023-10-17 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_alter_student_group_alter_student_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='teacher',
        ),
        migrations.CreateModel(
            name='StudentTeachersRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.student')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.teacher')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='teachers',
            field=models.ManyToManyField(through='school.StudentTeachersRelation', to='school.teacher'),
        ),
    ]
