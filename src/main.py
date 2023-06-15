import json
from termcolor import colored

json_path = f"{__file__}\\..\\data.json"
# Load The JSON Data From A File
with open(json_path) as file:
    json_data = json.load(file)

print(colored("\n~.~ Hello, Welcome To This Program ~.~ \n", "green", attrs=["dark"]))

while True:
    # Ask The User For The Path Of Value He/She Wanted
    path = input("Enter The Path Of Value You Want (or \"done\" to finish): ")
    
    if path == "done":
        break
    
    data = json_data
    # Traverse The JSON Data Based On The Path
    for key in path.split():
        if key.isdigit():
            key = int(key)
        data = data[key]

    # Display The Retrieved Value
    print(colored("\n==> %s \n" %data, 'cyan'))

print(colored("\nThank You For Choosing Us :)\n>>> Developed By Maryam Fakhraei & Amirhossein Naseri <<<","magenta", attrs=["dark"]))