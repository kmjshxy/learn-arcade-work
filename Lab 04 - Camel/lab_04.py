import random


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

        elif choice.lower() == "a":
            if canisters_of_gas <= 0:
                print("you have no gas")
            elif canisters_of_gas > 0:
                gas_in_the_ship += 6
                canisters_of_gas -= 1
                enemy_travel = random.randrange(8, 12)
                nasa_traveled += enemy_travel
                print("Gas has been refiled!")

        elif choice.lower() == "b":
            fast_speed = random.randrange(8, 14)
            galaxys_traveled += fast_speed
            heat_fast = random.randrange(1, 3)
            engine_heat += heat_fast
            gas_in_the_ship -= .2
            enemy_travel = random.randrange(8, 12)
            nasa_traveled += enemy_travel
            print("You have traveled ", fast_speed, " galaxy's")
            planet_w_gas = random.randrange(1, 6)
            if planet_w_gas == 4:
                canisters_of_gas = 4
                gas_in_the_ship += 2
                print("you found a planet with the type of gas you need!"
                      "you have refilled all of your gas canisters and your ship!!")

        elif choice.lower() == "c":
            planet_w_gas = random.randrange(1, 6)
            if planet_w_gas == 4:
                canisters_of_gas = 4
                gas_in_the_ship += 2
                print("you found a planet with the type of gas you need!")
                print("you have refilled all of your gas canisters and your ship!!")
            light_speed = random.randrange(14, 17)
            galaxys_traveled += light_speed
            gas_in_the_ship -= 1
            heat_light = random.randrange(5, 8)
            engine_heat += heat_light
            enemy_travel = random.randrange(9, 12)
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
# engine heat
        if engine_heat >= 26:
            print("Your engine exploded!!")
            done = True
        elif engine_heat >= 18:
            print("The engines are getting hot!")
# NASA
        if galaxys_traveled <= nasa_traveled:
            print("You were captured!!")
            done = True
        elif galaxys_traveled - nasa_traveled <= 15:
            print("NASA is getting close!!")
# win
        if galaxys_traveled >= 250:
            print()
            print("You made it home!! ")
            done = True
# gas
        if gas_in_the_ship <= 0:
            print("you ran out of gas and your ship exploded!!")
            done = True
        elif gas_in_the_ship <= 1.5:
            print("you are getting low on gas.")


main()
