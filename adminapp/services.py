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
