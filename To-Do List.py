user_choice = 0

tasks = ["Learn to code", "Go shopping", "Watch Your favorite show",]

def show_tasks():
     
    for task in tasks:
        task_index = 0   
        print(task + str(task_index))
        task_index += 1
        print()



def add_task():
    task = input("Add reminder:" + "\n")
    tasks.append(task)
    print("Succesfully Added")


def delete_item():
    task_index = int(input("Which one do you wanna delete? : " + "\n"))
    if task_index < 0 or task_index > len(tasks) -1:
        print("This reminder doesn't exist")
        return
    
    tasks.pop(task_index)    
    print("Reminder removed")


def save_item():
    file = open("Reminder.txt", "w+")
    for task in tasks:
        file.write(task + "\n")
        file.close()



5

while user_choice != 5:
    if user_choice == 1:
        show_tasks()
        
    if user_choice ==2:
        add_task()
        

    if user_choice == 3:
        delete_item()

    if user_choice == 4:
        save_item()



    print("1.Show my reminders")
    print("2.Add reminder")
    print("3.Delete reminder")
    print("4.Save")
    print("5.Exit")
    print()

    user_choice = int(input("What do You want me to do ? : " + "\n"))        
       


        
    



    


