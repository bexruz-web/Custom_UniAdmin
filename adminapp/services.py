from django.db import connection
from contextlib import closing


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row)) for row in cursor.fetchall()
    ]


def dictfetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))


def get_facuties():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * FROM adminapp_faculty""")
        faculties = cursor.dictfetchall(cursor)
        return faculties


def get_kafedra():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * FROM adminapp_kafedra""")
        kafedra = dictfetchall(cursor)
        return kafedra


def get_subjects():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * FROM adminapp_subjects""")
        subjects = dictfetchall(cursor)
        return subjects


def get_teachers():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * FROM adminapp_teachers""")
        teachers = dictfetchall(cursor)
        return teachers


def get_groups():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * FROM adminapp_groups""")
        groups = dictfetchall(cursor)
        return groups


def get_students():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * FROM adminapp_students""")
        students = dictfetchall(cursor)
        return students


