# string concatination (how to put strings together)
# suppose we want to create a string that says "subscribe to _____"

# basics of string concatination 

# youtuber = "kylie ying" # some string varibale


# # few ways to do this 

# print("subscribe to "+ youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

adj = input("adjective: ")

verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("famous person:")

madlib = f"computer programmming is so {adj}! i makes me so exited all the time because\
I love to {verb1}. Stay hidrated and {verb2} like you are {famous_person}!"

print(madlib)