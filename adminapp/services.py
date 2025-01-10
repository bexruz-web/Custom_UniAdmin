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


def get_data_from_table(table_name):
    # connection.cursor() yordamida bazaga  ulanamiz va cursor obyektini ochamiz
    with closing(connection.cursor()) as cursor:
        # Berilgan jadval nomi (table_name) asosida SQL so'rovini bajaradi
        cursor.execute(f"SELECT * FROM {table_name}")
        # Jadvaldagilarni lug'at shaklida qaytaradi
        return dictfetchall(cursor)


# adminapp_kafedra jadvaliga adminapp_faculty dan faculty nomlarini olish uchun LEFT JOIN ishlatildi
def get_kafedra_with_faculty():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""
            SELECT adminapp_kafedra.*, adminapp_faculty.name AS faculty_name
            FROM adminapp_kafedra
            LEFT JOIN adminapp_faculty ON adminapp_kafedra.faculty_id = adminapp_faculty.id
        """)
        return dictfetchall(cursor)


# adminapp_teachers jadvaliga adminapp_subjects dan subjects nomlarini olish uchun LEFT JOIN ishlatildi
def get_teachers_with_subjects():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""
            SELECT adminapp_teachers.*, adminapp_subjects.name AS subject_name
            FROM adminapp_teachers
            LEFT JOIN adminapp_subjects ON adminapp_teachers.subjects_id = adminapp_subjects.id
        """)
        return dictfetchall(cursor)


"""
    Bu function adminapp_groups jadvalidan guruhlar va ularga tegishli ma'lumotlarni olish uchun.
    
    LEFT JOIN lar orqali quyidagi bog'liq jadvallardan ma'lumot olinadi:
    adminapp_faculty - guruhning fakulteti
    adminapp_kafedra - guruhning kafedrasi
    adminapp_teachers - guruhning mentori
    adminapp_groups_subjects - ManyToManyField() orqali guruh va predmetlarni bog'lovchi jadval
    adminapp_subjects - guruhga tegishli predmetlar
    
    GROUP_CONCAT yordamida guruhning barcha predmetlari bitta qatorga yig'iladi.
"""

def get_groups_with_details():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""
            SELECT 
                adminapp_groups.*,
                adminapp_faculty.name AS faculty_name, 
                adminapp_kafedra.name AS kafedra_name, 
                adminapp_teachers.first_name AS mentor_name,
                GROUP_CONCAT(adminapp_subjects.name) as subjects
            FROM 
                adminapp_groups
            LEFT JOIN
                adminapp_faculty ON adminapp_groups.faculty_id = adminapp_faculty.id
            LEFT JOIN
                adminapp_kafedra ON adminapp_groups.kafedra_id = adminapp_kafedra.id
            LEFT JOIN
                adminapp_teachers ON adminapp_groups.mentor_id = adminapp_teachers.id    
            LEFT JOIN
                adminapp_groups_subjects ON adminapp_groups.id = adminapp_groups_subjects.groups_id
            LEFT JOIN
                adminapp_subjects ON adminapp_groups_subjects.subjects_id = adminapp_subjects.id
            GROUP BY
                adminapp_groups.id
        """)
        return dictfetchall(cursor)


"""
    Bu func adminapp_students jadvaliga adminapp_groups jadvalidan name ni olib kelish uchun LEFT JOIN ishlatildi
"""

def get_students_with_groups():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""
            SELECT adminapp_students.*, adminapp_groups.name AS group_name
            FROM adminapp_students
            LEFT JOIN adminapp_groups ON adminapp_students.group_id = adminapp_groups.id
        """)
        return dictfetchall(cursor)

