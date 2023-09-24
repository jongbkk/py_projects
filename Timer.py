import time


def timer(seconds):
    print("Timer set for", seconds, "seconds.")
    time.sleep(seconds)
    print("Timer has finished!")


def f_timer():
    print("Timer Program")
    while True:
        try:
            seconds = int(input("Enter the number of seconds for the timer: "))
            if seconds <= 0:
                print("please enter a positive number of seconds.")
            else:
                timer(seconds)
                break
        except ValueError:
            print("invalid input. Please enter a valid number of seconds.")


f_timer()
