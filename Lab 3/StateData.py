# Author:		Logan Hammond; lhammond12@student.umuc.edu
# Source File:  States.py
# Description:  Program that allows a user to display, sort and update as 
#               needed a List of U.S States containing the State Capital and 
#               State Bird.
# IDE:			AWS Cloud9

import json

class StateData:
    state_data = []
    
    def __init__(self):
        self.loadData()
        pass
    
    def loadData(self):
        with open("data.json") as json_file:
            try:
                data = json.load(json_file)
                for d in data["states"]:
                    state = [d["name"], d["capital"], d["flower"], d["bird"]]
                    self.state_data.append(state)
            except(ValueError, KeyError, TypeError):
                print("JSON format error.")
        pass
            
    # End of class
    pass

def main():
    states = StateData()
    
    # Display menu. 
    while True:
        print("\n\tSelect from the following menu...")
        print("\t\t1. Display all U.S. states in alphabetical order along " \
        "with capital and flower.")
        print("\t\t2. Search for a specific state and display the " \
        "appropriate capital and bird.")
        print("\t\t3. Update a bird for a specific state.")
        print("\t\t4. Exit the application.")
        
        # Get input from user and display it. 
        try:
            choice_int = int(input())
            print("\n\t\tYou selected {}".format(choice_int))
        except ValueError: 
            print("\n\t\tInvalid input. Please try again.")
            continue
        
        
        # Sentinel check. 
        if choice_int == 4: 
            print("Thanks for using this application!")
            break
            
        # "Switch" logic. 
        if choice_int == 1:
            print("Format: #: NAME, CAPITAL, FLOWER, BIRD")
            i = 1
            for state in states.state_data:
                print("{}: {}, {}, {}, {}".format(i, state[0], state[1], 
                state[2], state[3]))
                i += 1
        elif choice_int == 2:
            try: 
                print("\n\t\tEnter state number (select 1 from previous menu)")
                state_index = int(input()) - 1
                print("\n\t\tFORMAT: CAPITAL, BIRD\n " \
                "\t\t{}, {}".format(states.state_data[state_index][1], 
                states.state_data[state_index][3]))
            except (IndexError, ValueError):
                print("\n\t\tInvalid input. Please try again.") 

        elif choice_int == 3:
            print("\n\t\tEnter state number (select 1 from previous menu)")
            try: 
                state_index = int(input()) - 1
                if state_index < 1 or state_index > 50: 
                    print("\b\t\tInvalid input. Please try again.")
                    continue
                print("\n\t\tWhat is the new state bird?")
                new_bird = input()
                states.state_data[state_index][3] = str(new_bird)
            except (IndexError, ValueError):
                print("\n\t\tInvalid input. Please try again.") 
        else:
            print("Invalid input. Please try again.")
    pass

if __name__ == "__main__":
    main()
    pass