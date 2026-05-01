import time

def task_tracker():
    tasks = ["Learn Java", "finish Jenkins task", "Use Docker"]
    print("My task tracker app")
    for index, task in enumerate(tasks, 1):
        print(f"{index}. {task}")
    print("-----------------------")
    return tasks

if __name__ == "__main__":
    task_tracker()
    
    print("deployment success, container up")
    while True:
        time.sleep(60)
