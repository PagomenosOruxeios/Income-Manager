import requests
from menu_options import option1, option2, option3

cash = 0

options = [
    {
        "display": "Remaining balance",
        "function": option1
    },
    {
        "display": "Recent transactions",
        "function": option2
    },
    {
        "display": "Log a transaction",
        "function": option3
    },
]

option_string = ""

for i, option_data in enumerate(options):
    string = f"{option_string}{i+1}. {option_data["display"]}"
    if i == 0:
        option_string = string if len(options) == 1 else f"{string}\n"
    elif i == (len(options)-1):
        option_string = string
    else:
        option_string = f"{string}\n"

def main():
    while True:
        print(option_string)
        option_index = int(input())
        option_data = options[option_index-1]
        if option_data == None:
            print(f"Couldn't find option {option_index or 0}, please try again!")
            print(option_string)
        else:
            option_data["function"]()

if __name__ == "__main__":
    main()