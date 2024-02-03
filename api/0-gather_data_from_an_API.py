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
    get_employee_todo_progress(employee_id)