import random
from typing import List


def monty_hall_game(switch_doors: bool) -> bool:
    # the car is behind one of the doors
    doors = ['car'] + ['goat'] * 2
    random.shuffle(doors)

    # the player picks a door
    initial_choice = random.choice([0, 1, 2]) #  range(3) would be better

    # the host opens a door with a goat
    doors_revealed = [i for i in range(3) if i != initial_choice and doors[i] == 'goat']
    door_reveald = random.choice(doors_revealed)
    
    # the player switches doors
    if switch_doors:
        final_choice = [i for i in range(3) if i != initial_choice and i != door_reveald][0]
    else:
        # the player sticks with their initial choice
        final_choice = initial_choice

    # the player wins if they picked the car
    return doors[final_choice] == 'car'


def monty_hall_sim(num_games: int = 10000) -> None:

    # simulate the game n times and return the fraction of wins

    num_wins_without_switching =  sum(monty_hall_game(switch_doors=False) for _ in range(num_games))
    num_wins_switching = sum(monty_hall_game(switch_doors=True) for _ in range(num_games))

    return num_wins_switching , num_wins_without_switching

if __name__ == '__main__':
    num_games = 10000
    num_wins_switching , num_wins_without_switching = monty_hall_sim(num_games=num_games)
    print(f"Monty Hall simulation ({num_games} games):")
    print(f"Win rate without switching: {num_wins_without_switching/num_games:.2%}")
    print(f"Win rate with switching: {num_wins_switching/num_games:.2%}")