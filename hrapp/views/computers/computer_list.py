import sqlite3
from django.shortcuts import render
from hrapp.models import Computer
from ..connection import Connection


def computer_list(request):
    if request.method == 'GET':
        with sqlite3.connect("/Users/joeshep/workspace/python/bangazon-workforce-boilerplate/bangazonworkforcemgt/db.sqlite3") as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                c.id,
                c.make,
                c.purchase_date,
                c.decommission_date,
                e.first_name,
                e.last_name
            from hrapp_computer c
            LEFT JOIN hrapp_employeecomputer ec
            ON c.id == ec.computer_id
            LEFT JOIN hrapp_employee e
            on e.id == ec.employee_id
            where c.decommission_date is not null
            """)

            all_computers = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                computer = Computer()
                computer.id = row['id']
                computer.make = row['make']
                computer.purchase_date = row['purchase_date']
                if row['first_name'] is not None:
                    computer.current_employee = f"{row['first_name']} {row['last_name']}"

                all_computers.append(computer)

    template = 'computers/computers_list.html'
    context = {
        'computers': all_computers
    }

    return render(request, template, context)
