import random

#list of endangered species
species = ['African Elephant'  ,'African Wild Dog'  ,'Albacore Tuna'     ,'Amazon Dolphin'    ,'Amur Leopard'      ,'Arctic Fox'        ,'Arctic Wolf'       ,'Asian Elephant'    ,'Beluga'            ,'Bigeye Tuna'       ,'Black Rhino'       ,'Black Spider Monkey','Black-footed Ferret','Blue Whale'        ,'Bluefin Tuna'      ,'Bonobo'            ,'Bornean Orangutan' ,'Pygmy Elephant'    ,'Bowhead Whale'     ,'Brown Bear'        ,'Chimpanzee'        ,'Bottlenose Dolphin','Continental Tiger' ,'Cross River Gorilla','Dolphins'          ,'Porpoises'         ,'Dugong'            ,'Eastern Gorilla'   ,'Elephant'          ,'Fin Whale'         ,'Forest Elephant'   ,'Galápagos Penguin' ,'Ganges Dolphin'    ,'Giant Panda'       ,'Giant Tortoise'    ,'Gorilla'           ,'Gray Whale'        ,'Great White Shark' ,'One-Horned Rhino'  ,'Greater Sage-Grouse','Green Turtle'      ,'Hawksbill Turtle'  ,'Hectors Dolphin'   ,'Hippopotamus'      ,'Humphead Wrasse'   ,'Indian Elephant'   ,'Indus River Dolphin','Irrawaddy Dolphin' ,'Jaguar'            ,'Javan Rhino'       ,'Leatherback Turtle','Loggerhead Turtle' ,'Macaw'             ,'Marine Iguana'     ,'Monarch Butterfly' ,'Mountain Gorilla'  ,'Mountain Plover'   ,'Narwhal'           ,' Right Whale'      ,'Olive Ridley Turtle','Orangutan'         ,'Pacific Salmon'    ,'Pangolin'          ,'Penguin'           ,'Plains Bison'      ,'Poison Dart Frog'  ,'Polar Bear'        ,'Pronghorn'         ,'Red Panda'         ,'Rhino'             ,'Saola'             ,'Savanna Elephant'  ,'Sea Lions'         ,'Sea Turtle']

def generate_grid():
        grid = {"B": [],"I": [],"N": [],"G": [],"O": [],}
        for letter in grid:
            grid[letter] = random.sample((species),5)
            if letter == 'N':
                grid[letter][2] = 'X'
        return grid


def print_card(grid):
    for letter in grid:
        print(letter, end="\t\t")
        for number in grid[letter]:
            print(number, end="\t\t")
        print("\n")
    print("\n")

def draw(grid, species):
#pop function used to draw random from species list
    specie_drawn = species.pop()
    for letter in grid:
        i = 0
        for specie in grid[letter]:
            if specie == specie_drawn:
                grid[letter][i] = "X"
            i += 1
    return specie_drawn

def check_win(grid):
    win = False
    if grid["B"][0] == "X" and grid["I"][1] == "X" and grid["N"][2] == "X" and grid["G"][3] == "X" and grid["O"][4] == "X":
        win = True
    elif grid["O"][0] == "X" and grid["G"][1] == "X" and grid["N"][2] == "X" and grid["I"][3] == "X" and grid["B"][4] == "X":
        win = True
    elif grid["B"][0] == "X" and grid["O"][4] == "X" and grid["B"][4] == "X" and grid["O"][0] == "X":
        win = True
    for letter in grid:
        if(len(set(grid[letter]))==1):
            win = True
    for i in range(5):
        cnt = 0
        for letter in grid:
            if grid[letter][i] == "X":
                cnt += 1
        print(cnt)
        if cnt == 5:
            win = True
            break
    return win

#----------------------------------------------------------------------------------------------------------

def main():

    print("Let's play BINGO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    grid = generate_grid()

    print("\nHere is your card:\n")
    print_card(grid)

    print("\nKeep pressing ENTER to continue or type quit to exit.\n")
    user_input = input()
    win = check_win(grid)
    draws_till_win = 0

    while win == False and user_input != "quit":
        species_drawn = draw(grid, species)
        draws_till_win += 1

        print(f"\nspecie drawn: {species_drawn}.")
        print(f"Total drawn species: {draws_till_win}.\n")
        print_card(grid)
        win = check_win(grid)
        user_input = input()

    if win == True:
        print(f"\nBingo JA!!!!!!!!! Total drawn species to win: {draws_till_win}.")
    else:
        print("Bummer, Thanks for playing!")

main()