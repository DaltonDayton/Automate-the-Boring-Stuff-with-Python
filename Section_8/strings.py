import pyperclip

print("Enter a name.")
name = input()

pyperclip.copy(name)

place = "Main Street"
time = "6 pm"
food = "turnips"

print(
    "Hello %s, you are invited to a party at %s at %s. Please bring %s."
    % (name, place, time, food)
)

