
def ds(roll_no, name):
    list = [roll_no, name]
    tuple = (roll_no, name)
    set = {roll_no, name}
    dict = {'roll_no': roll_no, 'name': name}
    
    print("main data structures")
    print("List:", list)
    print("Tuple:", tuple)
    print("Set:", set)
    print("Dictionary:", dict)
    
    
    new_rollno = input("Enter new roll number: ")
    new_name = input("Enter new name: ")
    
    # Changing values during runtime
    list[0] = new_rollno
    list[1] = new_name
    
    set.add(new_rollno)
    set.add(new_name)
    
    dict['roll_no'] = new_rollno
    dict['name'] = new_name
    
    print("\nUpdated data structures:")
    print("List:", list)
    print("Tuple:", tuple)
    print("Set:", set)
    print("Dictionary:", dict)


ds(45,"mohit")
