import sqlite3
from django.shortcuts import render
from hrapp.models import Department
from ..connection import Connection


def department_list(request):
    if request.method == 'GET':
        with sqlite3.connect("/Users/joeshep/workspace/python/bangazon-workforce-boilerplate/bangazonworkforcemgt/db.sqlite3") as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            # and e.is_supervisor == 1
            db_cursor.execute("""
            select
                d.id,
                d.name,
                d.budget,
                e.first_name,
                e.last_name,
                e.is_supervisor,
                count(e.id) employee_count
            from hrapp_department d
            left join hrapp_employee e
            on e.department_id == d.id
            group by d.id
            """)

            all_departments = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                department = Department()
                department.id = row['id']
                department.name = row['name']
                department.budget = row['budget']
                department.size = row['employee_count']
                if row['is_supervisor']:
                    department.supervisor = f"{row['first_name']} {row['last_name']}"

                all_departments.append(department)

    template = 'departments/departments_list.html'
    context = {
        'departments': all_departments
    }

    return render(request, template, context)
