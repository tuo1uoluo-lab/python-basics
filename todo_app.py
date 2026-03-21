tasks = []

def add_task(task):
    tasks.append(task)

def remove_task(task):
    tasks.remove(task)

def show_tasks():
    print(tasks)

add_task("买菜")
add_task("写作业")
show_tasks()
remove_task("买菜")
show_tasks()
