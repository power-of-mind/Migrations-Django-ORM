from django.db import migrations


def forwards(apps, schema_editor):
    Student = apps.get_model('school', 'Student')
    Teacher = apps.get_model('school', 'Teacher')

    for student in Student.objects.all():
        if student.teacher_id:
            student.teachers.add(student.teacher_id)


def backwards(apps, schema_editor):
    Student = apps.get_model('school', 'Student')

    for student in Student.objects.all():
        teacher = student.teachers.first()
        if teacher:
            student.teacher_id = teacher.id
            student.save()


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_student_teacher'),
    ]

    operations = [
        migrations.RunPython(forwards, backwards),
    ]