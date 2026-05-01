def task_tracker():
    tasks = ["Buy groceries", "Finish Jenkins task", "Learn Docker"]

    print("--- My Task Tracker ---")
    for index, task in enumerate(tasks, 1):
        print(f"{index}. {task}")
    print("-----------------------")
    return True

if __name__ == "__main__":
    task_tracker()
