import time

class VirtualPet:

def __init__(self, name):

self.name = name

self.hunger = 5

self.happiness = 5

def feed(self):

self.hunger -= 1

self.happiness += 1

print(f"You fed {self.name}. Hunger: {self.hunger}, Happiness: {self.happiness}")

def play(self):

self.happiness += 2

print(f"You played with {self.name}. Happiness: {self.happiness}")

def check_status(self):

print(f"{self.name}'s status -> Hunger: {self.hunger}, Happiness: {self.happiness}")

def main():

pet_name = input("Name your virtual pet: ")

pet = VirtualPet(pet_name)

while True:

print("\n1. Feed your pet\n2. Play with your pet\n3. Check pet status\n4. Quit")

choice = input("Choose an option: ")

if choice == '1':

pet.feed()

elif choice == '2':

pet.play()

elif choice == '3':

pet.check_status()

elif choice == '4':

break

else:

print("Invalid choice.")

time.sleep(1)

if __name__ == "__main__":

main()
