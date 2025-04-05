queue = []
def menu():
    while True:
        print("\nMenu:")
        print("1. Enqueue (Add an element to the queue)")
        print("2. Dequeue (Remove an element from the queue)")
        print("3. Display the queue")
        print("4. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            element = input("Enter an element to enqueue: ")
            queue.append(element)
            print(f"{element} has been added to the queue.")
        elif choice == 2:
            if queue:
                removed = queue.pop(0)
                print(f"{removed} has been removed from the queue.")
            else:
                print("The queue is empty. Nothing to dequeue.")
        elif choice == 3:
            print("Current queue:", queue if queue else "The queue is empty.")
        elif choice == 4:
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")
menu()