# Star Wars Mission Generator

## One-Day Python Coding Challenge

Today you will build a **Star Wars Mission Generator** using Python.

Your program will randomly create a Star Wars-style mission briefing with a character, planet, mission, enemy, ally, ship, and difficulty level.

This project is meant to be fun, creative, and a good review of Python basics.

---

## Project Goal

By the end of class, your program should generate a mission that feels like it could start a Star Wars movie, game, or comic.

Example output:

```text
==============================
   STAR WARS MISSION BRIEFING
==============================
Character: Jedi Knight
Planet: Tatooine
Mission: rescue a captured droid
Enemy: Darth Vader
Ally: Chewbacca
Ship: Millennium Falcon
Difficulty: 8

Briefing:
A Jedi Knight must travel to Tatooine aboard the Millennium Falcon.
With help from Chewbacca, they must rescue a captured droid before Darth Vader stops them.
This mission is extremely risky. I have a bad feeling about this.
May the Force be with you.
```

---

## What You Will Practice

This project reviews several important Python skills:

- Lists
- `random.choice()`
- `random.randint()`
- Variables
- Strings
- f-strings
- Functions
- `while` loops
- `if`, `elif`, and `else`
- Clean output formatting
- Creativity in coding

---

# Step 1: Create Your Python File

Create a new Python file named:

```text
star_wars_mission.py
```

At the top of your file, import the `random` module:

```python
import random
```

The `random` module lets Python randomly choose items from a list.

---

# Step 2: Create Your Lists

A list stores multiple values in one variable.

For this project, we will create lists of possible Star Wars mission details.

Add this starter code:

```python
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
```

---

# Step 3: Use `random.choice()`

The `random.choice()` function randomly picks one item from a list.

Example:

```python
character = random.choice(characters)
```

This chooses one random character from the `characters` list.

Add this code below your lists:

```python
character = random.choice(characters)
planet = random.choice(planets)
mission = random.choice(missions)
enemy = random.choice(enemies)
ally = random.choice(allies)
ship = random.choice(ships)
```

---

# Step 4: Print the Mission Details

Now display the randomly chosen mission details.

Add this code:

```python
print("STAR WARS MISSION BRIEFING")
print()
print("Your character:", character)
print("Your planet:", planet)
print("Your mission:", mission)
print("Your enemy:", enemy)
print("Your ally:", ally)
print("Your ship:", ship)
```

Run your program.

You should see a random mission briefing.

Run it again.

The results should change.

---

# Step 5: Add a Story Briefing with f-Strings

An f-string lets you insert variables into a sentence.

Example:

```python
print(f"A {character} must travel to {planet}.")
```

Add this to your program:

```python
print()
print("Mission Briefing:")
print(f"A {character} must travel to {planet} aboard the {ship}.")
print(f"With help from {ally}, they must {mission} before {enemy} stops them.")
print("May the Force be with you.")
```

Now your mission should read more like a story.

---

# Step 6: Add Mission Difficulty

Use `random.randint()` to generate a random difficulty number.

Add this code near your other random choices:

```python
difficulty = random.randint(1, 10)
```

Then display it:

```python
print("Difficulty:", difficulty)
```

Now add a difficulty message:

```python
if difficulty <= 3:
    print("This should be an easy mission.")
elif difficulty <= 7:
    print("This mission will be dangerous.")
else:
    print("This mission is extremely risky. I have a bad feeling about this.")
```

---

# Step 7: Improve the Output

Make your output easier to read by adding separators and spacing.

Example:

```python
print("\n==============================")
print("   STAR WARS MISSION BRIEFING")
print("==============================")
```

The `\n` creates a blank line before the heading.

Clean output makes your program feel more polished.

---

# Step 8: Put the Mission Generator in a Function

A function lets us organize code and reuse it.

Create a function called `generate_mission()`.

Example:

```python
def generate_mission():
    character = random.choice(characters)
    planet = random.choice(planets)
    mission = random.choice(missions)
    enemy = random.choice(enemies)
    ally = random.choice(allies)
    ship = random.choice(ships)
    difficulty = random.randint(1, 10)

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
```

To run the function, call it like this:

```python
generate_mission()
```

---

# Step 9: Add a Replay Loop

A replay loop lets the user generate more than one mission.

Add this code after your function:

```python
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
```

Now the user can keep generating missions until they choose to stop.

---

# Complete Starter Version

You may use this as your full starter code:

```python
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


def generate_mission():
    character = random.choice(characters)
    planet = random.choice(planets)
    mission = random.choice(missions)
    enemy = random.choice(enemies)
    ally = random.choice(allies)
    ship = random.choice(ships)
    difficulty = random.randint(1, 10)

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
```

---

# Required Tasks

Your program must include:

- [ ] A file named `star_wars_mission.py`
- [ ] `import random`
- [ ] At least 6 lists
- [ ] At least 6 uses of `random.choice()`
- [ ] At least 1 use of `random.randint()`
- [ ] At least 2 f-strings
- [ ] A function named `generate_mission()`
- [ ] A loop that lets the user generate more missions
- [ ] An `if`, `elif`, and `else` statement
- [ ] Clean and readable output
- [ ] At least 3 custom items added to the starter lists

---

# Customization Requirements

Add at least 3 new items to at least 3 different lists.

For example, you could add new:

- Characters
- Planets
- Ships
- Enemies
- Allies
- Missions

You should also add one new custom list.

Possible custom list ideas:

- Lightsaber colors
- Droids
- Force powers
- Weapons
- Mission rewards
- Danger events
- Secret locations
- Star Wars creatures

Example:

```python
force_powers = [
    "Force push",
    "mind trick",
    "Force jump",
    "Force healing",
    "Force speed"
]
```

Then randomly choose one:

```python
force_power = random.choice(force_powers)
```

Then display it:

```python
print("Force Power:", force_power)
```

---

# Bonus Challenge 1: Choose Your Side

Let the user choose their side before generating a mission.

Example:

```python
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
```

---

# Bonus Challenge 2: Add a Success Chance

Generate a random success chance from 1 to 100.

```python
success_chance = random.randint(1, 100)

print("Success Chance:", success_chance, "%")

if success_chance >= 75:
    print("The Force is strong with this mission.")
elif success_chance >= 40:
    print("This mission is risky, but possible.")
else:
    print("The odds are not good.")
```

---

# Bonus Challenge 3: Create a Mission Code Name

Create a random mission code name.

Example lists:

```python
code_words_1 = ["Shadow", "Red", "Jedi", "Echo", "Rebel", "Nova"]
code_words_2 = ["Falcon", "Saber", "Moon", "Strike", "Temple", "Droid"]
```

Randomly combine them:

```python
code_name = random.choice(code_words_1) + " " + random.choice(code_words_2)
print("Mission Code Name:", code_name)
```

Example output:

```text
Mission Code Name: Shadow Falcon
```

---

# Bonus Challenge 4: Add ASCII Art

Add a simple text design at the beginning of your program.

Example:

```text
      /\
     /  \
    /____\
      ||
      ||
```

Or create your own Star Wars-style banner using text.

---

# Bonus Challenge 5: Add Multiple Mission Types

Let the mission type change the story.

Example:

```python
mission_type = random.choice(["rescue", "battle", "spy", "escape"])

if mission_type == "rescue":
    print("This is a rescue mission. Move quickly and protect the target.")
elif mission_type == "battle":
    print("This is a combat mission. Prepare for heavy resistance.")
elif mission_type == "spy":
    print("This is a stealth mission. Do not get caught.")
else:
    print("This is an escape mission. Get out before it is too late.")
```

---

# Example Final Output

```text
Welcome to the Star Wars Mission Generator!

Generate a new mission? yes/no: yes

==============================
   STAR WARS MISSION BRIEFING
==============================
Character: Mandalorian
Planet: Mustafar
Mission: recover stolen battle plans
Enemy: bounty hunters
Ally: BB-8
Ship: Razor Crest
Difficulty: 6

Briefing:
A Mandalorian must travel to Mustafar aboard the Razor Crest.
With help from BB-8, they must recover stolen battle plans before bounty hunters stop them.
This mission will be dangerous.
May the Force be with you.

Generate a new mission? yes/no: no
Goodbye, young Jedi.
```

---

# Common Mistakes to Watch For

## Mistake 1: Forgetting to Import Random

Incorrect:

```python
character = random.choice(characters)
```

If you forgot this at the top:

```python
import random
```

Python will not know what `random` means.

---

## Mistake 2: Forgetting Parentheses When Calling a Function

Incorrect:

```python
generate_mission
```

Correct:

```python
generate_mission()
```

Functions need parentheses to run.

---

## Mistake 3: Misspelling a Variable Name

Incorrect:

```python
charcter = random.choice(characters)
print(character)
```

Correct:

```python
character = random.choice(characters)
print(character)
```

Variable names must match exactly.

---

## Mistake 4: Forgetting Commas in a List

Incorrect:

```python
ships = [
    "Millennium Falcon"
    "X-wing"
    "Razor Crest"
]
```

Correct:

```python
ships = [
    "Millennium Falcon",
    "X-wing",
    "Razor Crest"
]
```

List items need commas between them.

---

## Mistake 5: Incorrect Indentation

Incorrect:

```python
def generate_mission():
character = random.choice(characters)
print(character)
```

Correct:

```python
def generate_mission():
    character = random.choice(characters)
    print(character)
```

Python uses indentation to know what belongs inside a function.

---

# Reflection Questions

Answer these questions in a comment at the bottom of your Python file.

```python
# Reflection Questions:
# 1. What does random.choice() do?
# 2. What does random.randint() do?
# 3. Why are lists useful in this project?
# 4. Why did we put the mission generator inside a function?
# 5. What custom list or feature did you add?
# 6. What was your favorite mission your program created?
```

---

# 50-Point Rubric

| Category | Points |
|---|---:|
| Uses at least 6 lists | 8 |
| Uses `random.choice()` correctly | 8 |
| Uses `random.randint()` for difficulty or success chance | 5 |
| Uses at least 2 f-strings | 6 |
| Uses a function named `generate_mission()` | 8 |
| Uses a loop to generate multiple missions | 5 |
| Output is clean and easy to read | 5 |
| Adds custom content to the starter lists | 5 |
| **Total** | **50** |

---

# Bonus Points

You may earn up to 10 bonus points.

| Bonus Feature | Points |
|---|---:|
| Choose your side | +3 |
| Success chance system | +3 |
| Mission code name | +3 |
| ASCII art or custom banner | +2 |
| Multiple mission types | +4 |
| Extra creativity | +3 |

Maximum bonus: 10 points.

---

# Final Submission Checklist

Before submitting, make sure:

- [ ] Your file is named `star_wars_mission.py`
- [ ] Your program runs without errors
- [ ] Your program generates a random mission
- [ ] Your program uses lists
- [ ] Your program uses `random.choice()`
- [ ] Your program uses a function
- [ ] Your program uses a loop
- [ ] Your program has clean output
- [ ] You added custom content
- [ ] You answered the reflection questions

---

# Final Goal

Your final program should generate creative Star Wars-style mission briefings.

Every time the user generates a mission, the result should be different.

Be creative, have fun, and may the Force be with you.
