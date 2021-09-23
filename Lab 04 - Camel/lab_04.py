import random

#do the oasisi thing
def main():
    print("Welcome to Space Escape!")
    print("You are a alien and are trying to return home.")
    print("You have illegally borrowed a small space ship from NASA.")
    print("NASA is chasing you! Get across multiple galaxy's to get home!")

    galaxys_traveled = 0
    gas_in_the_ship = 6
    engine_heat = 0
    nasa_traveled = -20
    canisters_of_gas = 4
    done = False
    while not done:
        print()
        print(" A: refill your ship.")
        print("B: high speed.")
        print("C: light speed.")
        print("D: stop to cool the engine.")
        print("E: status check.")
        print("Q: Quit.")
        choice = input("whats you choice? ")
        print()
        if choice.lower() == "q":
            done = True
# fix this -->
        elif choice.lower() == "a":
            if canisters_of_gas <= 0:
                print("you have no gas")
            elif canisters_of_gas < 0:
                gas_in_the_ship += 1
                canisters_of_gas -= 1
                enemy_travel = random.randrange(8, 12)
                nasa_traveled += enemy_travel
                print("Gas has been refiled!")
        elif choice.lower() == "b":
            fast_speed = random.randrange(2, 10)
            galaxys_traveled += fast_speed
            heat_fast = random.randrange(1, 3)
            engine_heat += heat_fast
            gas_in_the_ship -= .2
            enemy_travel = random.randrange(8, 12)
            nasa_traveled += enemy_travel
            print("You have traveled ", fast_speed, " galaxy")
        elif choice.lower() == "c":
            light_speed = random.randrange(20, 26)
            galaxys_traveled += light_speed
            gas_in_the_ship -= 1
            heat_light = random.randrange(5, 8)
            engine_heat += heat_light
            enemy_travel = random.randrange(8, 12)
            nasa_traveled += enemy_travel
            print("You have traveled ", light_speed, " galaxy's")
        elif choice.lower() == "d":
            engine_heat -= 15
            enemy_travel = random.randrange(8, 12)
            nasa_traveled += enemy_travel
            print("you have stopped for a bit to cool your engines")
        elif choice.lower() == "e":
            print("galaxy's traveled: ", galaxys_traveled)
            print("you have", canisters_of_gas, "canisters of gas left")
            print("NASA is", galaxys_traveled - nasa_traveled, "galaxy's behind you")

        if engine_heat >= 15:
            print("The engines are getting hot!")
        if engine_heat >= 26:
            print("Your engine exploded!!")
            done = True
        if galaxys_traveled <= nasa_traveled:
            print("You were captured!!")
            done = True
        if galaxys_traveled >= 250:
            print("You made it home!! ")
            done = True
        if galaxys_traveled - nasa_traveled <= 15:
            print("NASA is getting close!!")
        if gas_in_the_ship <= 0:
            print("you ran out of gas and your ship exploded!!")
            done = True
        if gas_in_the_ship <= 2:
            print("you are getting low on gas.")










main()
