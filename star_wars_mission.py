import random


characters = [
    "Jedi Knight",
    "Padawan",
    "Rebel Pilot",
    "Mandalorian",
    "Smuggler",
    "Clone Trooper",
    "Resistance Spy"
]

planets = [
    "Tatooine",
    "Hoth",
    "Endor",
    "Naboo",
    "Coruscant",
    "Dagobah",
    "Mustafar"
]

missions = [
    "rescue a captured droid",
    "recover stolen battle plans",
    "escape an Imperial base",
    "protect a hidden Jedi temple",
    "deliver a secret message",
    "destroy a Sith weapon",
    "find a lost lightsaber"
]

enemies = [
    "Darth Vader",
    "a Sith Inquisitor",
    "stormtroopers",
    "bounty hunters",
    "a crime lord",
    "battle droids",
    "the First Order"
]

allies = [
    "R2-D2",
    "Chewbacca",
    "Ahsoka Tano",
    "Obi-Wan Kenobi",
    "BB-8",
    "a group of Ewoks",
    "a mysterious rebel informant"
]

ships = [
    "Millennium Falcon",
    "X-wing",
    "TIE fighter",
    "Naboo starfighter",
    "Razor Crest",
    "Jedi starfighter",
    "Corellian freighter"
]

force_powers = [
    "Force push",
    "mind trick",
    "Force jump",
    "Force healing",
    "Force speed"
]
def generate_mission():
    character = random.choice(characters)
    planet = random.choice(planets)
    mission = random.choice(missions)
    enemy = random.choice(enemies)
    ally = random.choice(allies)
    ship = random.choice(ships)
    force_power = random.choice(force_powers)
    difficulty = random.randint(1, 10)
    success_chance = random.randint(1, 100)



    print("\n==============================")
    print("   STAR WARS MISSION BRIEFING")
    print("==============================")
    print("Character:", character)
    print("Planet:", planet)
    print("Mission:", mission)
    print("Enemy:", enemy)
    print("Ally:", ally)
    print("Ship:", ship)
    print("Difficulty:", difficulty)
    print("Force Power:", force_power)

    print("\nBriefing:")
    print(f"A {character} must travel to {planet} aboard the {ship}.")
    print(f"With help from {ally}, they must {mission} before {enemy} stops them.")

    if difficulty <= 3:
        print("This should be an easy mission.")
    elif difficulty <= 7:
        print("This mission will be dangerous.")
    else:
        print("This mission is extremely risky. I have a bad feeling about this.")

    print("May the Force be with you.")


print("Welcome to the Star Wars Mission Generator!")

while True:
    choice = input("\nGenerate a new mission? yes/no: ").lower()

    if choice == "yes":
        generate_mission()
    elif choice == "no":
        print("Goodbye, young Jedi.")
        break
    else:
        print("Please type yes or no.")
side = input("Choose your side: Jedi, Rebel, Sith, or Bounty Hunter: ").lower()

if side == "jedi":
    print("You have chosen the path of the Jedi.")
elif side == "sith":
    print("The dark side grows stronger...")
elif side == "rebel":
    print("The Rebellion needs your help.")
elif side == "bounty hunter":
    print("This mission is all about the credits.")
else:
    print("You are a mysterious traveler.")
