#creating a to do list
#adding a task
#removing a task
#interface
#display current task
def interface():
    while True:
        print("1. view task \n2. add task \n3. Complete task \n4. EXIT")
        n = int((input("Enter a number: ")))
        if n == 1:
            view_task()
        elif n == 2:
            add_tasK()
        elif n == 3:
            complete()
        elif n == 4:
            exit()
            

    
to_do = []


def add_tasK():
    tasK = input("Input a task: ")
    to_do.append(tasK)
    print(f"task, {tasK} was added to the list")
    for i in range(len(to_do)): 
        print(i, ":", to_do[i])
    interface()

def view_task() -> object:
    if to_do == []:
        print("you have completed all the task")
    else:
        print(to_do)
    for lmn in to_do:
        print(to_do(lmn), lmn)
    interface()

def complete():
    if not to_do:
        print("youve already completed all the task")
        return
    for idx, task in enumerate(to_do):
        print(f"{idx}: {task}")    #this checks if n is an empty string

    completiong = input(f"which task did you complete? {to_do}: ")
    #this checks if to_do is empty

    #compared n to a value in to_do list and delete it
    if completiong in to_do:
        to_do.remove(completiong)
        print(f"your new list of to do is: {to_do}")
    else:
        print("There is no task associated with this")
        
    

        
    
    
        
        
        
    
    
    #printing the values inside the list appointed to the index
    #for i in range(len(to_do)):
       # print(i, ":", to_do[i])
        
    #checks if n is a number
    
    # if n not in to_do:#makes sure n is not a negative number
    #     print("invalid task number")
    # else:
    #     del to_do[n]
            
        
interface()
add_tasK()
view_task()
complete()