# format method

print("\n== Format Method ==")
print("1. Indentation")
print("2. Justified to the right")
print("3. Justified to the left")
print("4. Justified to the center")
print("E. Exit")
print("The sentence: \"Pass me the {noun}\" she says")
choice = input("choice: ")

while choice != 'E' and choice != 'e':
    if choice == '1':
        print("\n- Indentation")
        noun = input("input a noun: ")
        print("[ \"Pass me the ({:10})\" she says ]".format(noun))
    elif choice == '2':
        print("\n- Justified to the right")
        noun = input("input a noun: ")
        print("[ \"Pass me the ({:>10})\" she says ]".format(noun))
    elif choice == '3':
        print("\n- Justified to the left")
        noun = input("input a noun: ")
        print("[ \"Pass me the ({:<10})\" she says ]".format(noun))
    elif choice == '4':
        print("\n- Justified to the center")
        noun = input("input a noun: ")
        print("[ \"Pass me the ({:^10})\" she says ]".format(noun))
    else:
        print("\n[ Invalid input ]")

    print("\n== Format Method ==")
    print("1. Indentation")
    print("2. Justified to the right")
    print("3. Justified to the left")
    print("4. Justified to the center")
    print("E. Exit")
    print("The sentence: \"Pass me the {noun}\" she says")
    choice = input("choice: ")

if choice == 'e' or choice == 'E':
    print("\n== Exit Program ==")





