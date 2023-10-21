import random
from datetime import datetime, timedelta
import os
import platform

def main():
    list1 = []
    for _ in range(5):
        list1.append(random.randint(40, 70))

    print(list1);

    curr_date = datetime.now().strftime("%A")

    print(curr_date)

    dir_name = "New Dir :D"

    new_path = os.path.join(os.getcwd(), dir_name)

    if not os.path.exists(new_path):
        os.mkdir(new_path)
    else:
        print("Already Exists BOZO")

    file_name = "File_Numba_1.txt"

    file_path = new_path + '/' + file_name

    with open(file_path, 'w+') as new_file:
        new_file.write("Hello Seaman!\n")
        new_file.write("Another Line >:3")

        new_file.seek(0)
        print(new_file.readline())
        print(new_file.readline())

        new_file.seek(0)

        new_file.write("I am ovverrrtinggg WOAW");



    print(platform.system());   
    print(os.name);
    print(platform.platform())

    print(os.listdir())

    print(datetime.date(datetime.now() - timedelta(days=10)))


if __name__ == '__main__':
    main();
