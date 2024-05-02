def greet():
    print("Hello from first module!")
    print("first module will become: {}".format(__name__))
if __name__ == "__main__":
    greet()