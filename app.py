import time

def task_tracker():
    tasks = ["Learn Java", "Finish Jenkins task", "Use Docker"]
    
    print("--- My Task Tracker ---")
    for index, task in enumerate(tasks, 1):
        print(f"{index}. {task}")
    print("-----------------------")
    
    print("deployment successful, the container is now up")

    while True:
        time.sleep(60)
    return True

if __name__ == "__main__":
    task_tracker()
