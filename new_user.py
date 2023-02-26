import time

def new_username():
    username = input("Hello, what's your name? ")

    username_file = open(f'/home/matthew/python/formula1game/username.txt', 'a')
    username_file.write(f"{username}")
    username_file.close()

    print(f"Hello, {username}. We will remember you in the future.")
    time.sleep(3)
    username_file.close()   