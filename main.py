import uuid

# first to do in python
# 1. make a while to show the to do list or finish the program
# 2. show the user list and ask him to select one item
# 3. show the item and ask  if  his  check this item
# 4. show the list resume as finished tasks unfinished task and the task avarage


def generate_uuid():
    new_uuid = uuid.uuid4()
    return str(new_uuid)


user_task_list = []


def create_new_item():

    task_name = input("type your task: ")
    task = {
        "name": task_name,
        "id": generate_uuid(),
        "isFinished": False
    }
    user_task_list.append(task)
    print("itemCreated")


def delete_task(task_index=0,):
    item_deleted = user_task_list.pop(task_index)
    print(f"you deleted the task {item_deleted["name"]}")

    if len(user_task_list) < 1:
        print("you task list in empty, please create one")
        create_new_item()
    
    
def update_task_name(task_index=0):
    task = user_task_list[task_index]

    new_task_name = input("What is the new task name: ")
    user_task_list[task_index]["name"] = new_task_name
    print(f"the name {task["name"]} was marked as changed to {new_task_name}")
    
    
def mark_task_as_finished(task_index=0):
    task = user_task_list[task_index]
    user_task_list[task_index]["isFinished"] = True
    print(f"the {task["name"]} was marked as finished")


def mark_task_as_unfinished(task_index=0):
    task = user_task_list[task_index]
    user_task_list[task_index]["isFinished"] = False
    print(f"the {task["name"]} was marked as unfinished")
    

def show_list_item(show_task_status=True):
    for task in user_task_list:
        task_item_position = user_task_list.index(task) + 1

        if show_task_status:
            task_is_finished = task["isFinished"]
            task_status = ""

            if task_is_finished:
                task_status = "that task is done"
            else:
                task_status = "you still has to complete that task"

            print(f"{task_item_position}°: {task["name"]} \n {task_status}")
        else:
            print(f"{task_item_position}°: {task["name"]} ")


def edit_list_item():
    if len(user_task_list) < 1:
        print("you task list in empty, please create one")
        create_new_item()

    while True:
        show_list_item(False)
        print("type 999 to  finish")
        task_to_edit = int(input("which some task: "))

        if task_to_edit == 999:
            break
        task_position = task_to_edit - 1
        task = user_task_list[task_position]

        print("Edit options")
        print("Choose an option:")
        print("+-----------------+---------------------+")
        print("|        type 1        |      change the task name       |")
        print("|        type 2        |      mark as finished      |")
        print("|        type 3        |      mark as unfinished     |")
        print("|        type 4        |      delete task    |")
        print("|        type 5        |      back to main painel    |")
        print("+-----------------+---------------------+")

        task_action = int(input("make a choice: "))

        if task_action == 1:
            update_task_name(task_position)
        elif task_action == 2:
            mark_task_as_finished(task_position)
        elif task_action == 3:
            mark_task_as_unfinished(task_position)
        elif task_action == 4:
            delete_task(task_position)
        elif task_action == 5:
            break
        else:
            input("you have to choose one")
        input("type enter to continue... ")


def finish_program():
    exit()


def task_status():
    if len(user_task_list) < 1:
        print("you task list in empty, please create one")
        create_new_item()

    total_tasks = len(user_task_list)
    finished_tasks = sum(task["isFinished"] for task in user_task_list)
    percentage_finished = (finished_tasks / total_tasks) * 100 if total_tasks > 0 else 0

    print(f"Total tasks: {total_tasks}")
    print(f"Finished tasks: {finished_tasks}")
    print(f"Percentage of finished tasks: {percentage_finished:.2f}%")

    input()


while True:
    print("__Hello this is you daily task")
    print("Choose an option:")
    print("+-----------------+---------------------+")
    print("|        type 1        |      See your list       |")
    print("|        type 2        |      Create a new item       |")
    print("|        type 3        |      Edit a task     |")
    print("|        type 4        |      Task  status   |")
    print("|        type 5        |      Finish the program     |")
    print("+-----------------+---------------------+")
    user_choice = int(input("make a choice:  "))

    if user_choice == 1:
        show_list_item()
    elif user_choice == 2:
        create_new_item()
    elif user_choice == 3:
        edit_list_item()
    elif user_choice == 4:
        task_status()
    elif user_choice == 5:
        finish_program()
    else:
        input("you have to choose one")
