import pickle
import os

class DigitalPet:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.hunger = 50
        self.happiness = 50
        self.age = 0

    def feed(self):
        self.hunger = max(self.hunger - 15, 0)
        self.happiness = min(self.happiness + 5, 100)
        print(f"{self.name} has been fed!")

    def play(self):
        self.happiness = min(self.happiness + 15, 100)
        self.hunger = min(self.hunger + 10, 100)
        self.health = max(self.health - 5, 0)
        print(f"{self.name} is playing and having fun!")

    def sleep(self):
        self.health = min(self.health + 10, 100)
        self.hunger = min(self.hunger + 5, 100)
        self.age += 1
        print(f"{self.name} slept and is now {self.age} days old.")

    def bathe(self):
        self.happiness = min(self.happiness + 5, 100)
        print(f"{self.name} is now clean and fresh!")

    def check_mood(self):
        if self.happiness >= 70:
            return "Happy 😀"
        elif 40 <= self.happiness < 70:
            return "Okay 🙂"
        elif 20 <= self.happiness < 40:
            return "Sad 😢"
        else:
            return "Angry 😡"

    def is_alive(self):
        return self.health > 0 and self.hunger < 100

    def check_status(self):
        print(f"\n--- {self.name}'s Status ---")
        print(f"Health: {self.health}")
        print(f"Hunger: {self.hunger}")
        print(f"Happiness: {self.happiness}")
        print(f"Age: {self.age}")
        print(f"Mood: {self.check_mood()}")
        print("---------------------------")

# Save pets to file
def save_pets(pets, filename="pets_data.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(pets, f)

# Load pets from file
def load_pets(filename="pets_data.pkl"):
    if os.path.exists(filename):
        with open(filename, "rb") as f:
            return pickle.load(f)
    return {}

def main():
    pets = load_pets()
    print("🐾 Welcome back to Digital Pet World! 🐾")

    if not pets:
        num_pets = int(input("How many pets do you want to adopt? "))
        for i in range(num_pets):
            name = input(f"Enter the name of pet #{i+1}: ")
            pets[name] = DigitalPet(name)

    while True:
        print("\nAvailable Pets:", ", ".join(pets.keys()))
        pet_name = input("Which pet do you want to interact with? (Type 'save' to save, 'exit' to quit) ").strip()
        
        if pet_name.lower() == 'exit':
            print("Goodbye! Remember to save next time! 👋")
            break
        elif pet_name.lower() == 'save':
            save_pets(pets)
            print("✅ Pets saved successfully!")
            continue

        pet = pets.get(pet_name)
        if not pet:
            print("Pet not found. Try again!")
            continue

        if not pet.is_alive():
            print(f"😢 {pet.name} has passed away. You can't interact with it anymore.")
            continue

        print("\nWhat would you like to do?")
        print("1. Feed 🥕")
        print("2. Play 🎾")
        print("3. Sleep 💤")
        print("4. Bathe 🛁")
        print("5. Check Status 📋")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            pet.feed()
        elif choice == '2':
            pet.play()
        elif choice == '3':
            pet.sleep()
        elif choice == '4':
            pet.bathe()
        elif choice == '5':
            pet.check_status()
        else:
            print("Invalid choice. Try again!")

        if not pet.is_alive():
            print(f"⚠️ Oh no! {pet.name} didn't survive...")

if __name__ == "__main__":
    main()
