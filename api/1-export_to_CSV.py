#!/usr/bin/python3
"""Consumimos API para extraer información ficticia"""
import requests
from sys import argv
import csv


def main():
    """Consultamos el nombre y las tareas de un empleado."""
    if len(argv) > 1 and argv[1].isdigit():
        id = argv[1]

        url_id = f"https://jsonplaceholder.typicode.com/users/{id}"
        url_todos = f"https://jsonplaceholder.typicode.com/users/{id}/todos"

        try:
            response = requests.get(url_id)

            if response.status_code == 200:
                data = response.json()
                EMPLOYEE_NAME = data['name']

            response = requests.get(url_todos)

            if response.status_code == 200:
                todos = response.json()

                total_task = sum(1 for todo in todos if todo['completed'])

                NUMBER_OF_DONE_TASKS = total_task
                TOTAL_NUMBER_OF_TASKS = len(todos)
                text = f"Employee {EMPLOYEE_NAME} is done with "\
                    f"tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):"

                # Exportar datos a CSV
                file_name = f"datos_empleado_{id}.csv"
                with open(file_name, 'w', newline='') as file_csv:
                    writer_csv = csv.writer(file_csv)
                    writer_csv.writerow(['Task', 'Completed'])
                    for todo in todos:
                        writer_csv.writerow([todo['title'], todo['completed']])

                print(f"The data has been successfully exported in '{file_name}'.")
                print(text)
                for todo in todos:
                    if todo['completed']:
                        print(f'\t {todo["title"]}')

        except requests.exceptions.HTTPError as e:
            print(f"Error de solictud: {e}")


if __name__ == '__main__':
    main()
