import json

print("Enter 'q' anytime to end the program.\n ")
while True:
    fav_num = input("What is your favorite number? ")
    if fav_num == 'q':
        break
    filename = 'favorite_number.json'
    try:
        fav_num = int(fav_num)
        with open(filename, 'w') as f_obj:
            json.dump(fav_num, f_obj)
        print("Thanks, we'll remember your favorite number is " + str(fav_num) 
            + ".")
        try_again = input("Would you like to enter another number?" 
            + "y/n for yes or no. ")
        if try_again == 'y':
            continue
        else:
            break
            
    except ValueError:
        print("Enter an actual digit.")
        continue

    
