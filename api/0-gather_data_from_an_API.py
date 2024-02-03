#!/usr/bin/python3
import requests
import sys

def get_employee_todo_progress(employee_id):
    # URL de la API REST
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'

    # Realizar la solicitud a la API
    response = requests.get(url)

    # Verificar si la solicitud fue exitosa
    if response.status_code != 200:
        print(f"Error al obtener los datos del empleado {employee_id}.")
        return

    # Obtener los datos de las tareas del empleado
    todos = response.json()

    # Filtrar las tareas completadas
    completed_tasks = [task for task in todos if task['completed']]
    total_tasks = len(todos)
    completed_tasks_count = len(completed_tasks)

    # Obtener el nombre del empleado
    employee_name = todos[0]['name']

    # Mostrar la información formateada
    print(f"Employee {employee_name} is done with tasks ({completed_tasks_count}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)#!/usr/bin/python3
"""Consumimos API para extraer información ficticia"""
import requests
from sys import argv


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

                print(text)
                for todo in todos:
                    if todo['completed']:
                        print(f'\t {todo["title"]}')

        except requests.exceptions.HTTPError as e:
            print(f"Error de solictud: {e}")


if __name__ == '__main__':
    main()