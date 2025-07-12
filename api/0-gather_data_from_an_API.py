#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    # Check that an employee ID is provided and is an integer
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    # Get user information
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("User not found.")
        sys.exit(1)

    employee_name = user_response.json().get("name")

    # Get todos
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Count tasks
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed") is True]
    num_done = len(done_tasks)

    # Print results
    print(f"Employee {employee_name} is done with tasks({num_done}/{total_tasks}):")
    for task in done_tasks:
        print("\t {}".format(task.get("title")))

