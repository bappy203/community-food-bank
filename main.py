
class Family:
    def __init__(self, family_id, name, members):
        self.family_id = family_id
        self.name = name
        self.members = members

    def display(self):
        return f"{self.family_id} - {self.name} - {self.members} members"


class FoodBank:
    def __init__(self):
        self.families = {}       # Dictionary: family ID -> Family object
        self.family_ids = set()  # Set: unique family IDs
        self.distribution_history = []  # List: distribution records
        self.available_packs = 0
        self.total_distributed = 0

    def register_family(self, family_id, name, members):
        family_id = family_id.strip()
        name = name.strip()

        if not family_id or not name:
            print("Error: Family ID and name cannot be empty.")
            return

        if family_id in self.family_ids:
            print("Error: This family ID is already registered.")
            return

        if members <= 0:
            print("Error: Number of members must be greater than zero.")
            return

        family = Family(family_id, name, members)
        self.families[family_id] = family
        self.family_ids.add(family_id)

        print("Family registered successfully!")

    def add_food(self, quantity):
        if quantity <= 0:
            print("Error: Number of packs must be positive.")
            return

        self.available_packs += quantity
        print(f"Food added successfully. Current stock: {self.available_packs}")

    def distribute_food(self, family_id, quantity):
        family_id = family_id.strip()

        if family_id not in self.families:
            print("Error: Family not found.")
            return

        if quantity <= 0:
            print("Error: Number of packs must be positive.")
            return

        # Do not distribute partially if stock is insufficient.
        if quantity > self.available_packs:
            print(
                f"Not enough food! Available stock: "
                f"{self.available_packs}. No packs distributed."
            )
            return

        self.available_packs -= quantity
        self.total_distributed += quantity

        # Tuple: immutable distribution record
        record = (family_id, self.families[family_id].name, quantity)
        self.distribution_history.append(record)

        print(
            f"Success! {quantity} packs given to "
            f"{self.families[family_id].name}."
        )
        print(f"Remaining stock: {self.available_packs}")

    def show_report(self):
        print("\n===== FOOD BANK REPORT =====")
        print(f"Available Packs: {self.available_packs}")

        print("\nRegistered Families:")
        if not self.families:
            print("No families registered.")
        else:
            for family in self.families.values():
                print(family.display())

        print("\nDistribution History:")
        if not self.distribution_history:
            print("No distributions recorded.")
        else:
            for family_id, name, quantity in self.distribution_history:
                print(f"{family_id} ({name}) received {quantity} packs")

        print(f"\nTotal Distributed: {self.total_distributed}")


def read_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Error: Please enter a valid whole number.")


def main():
    food_bank = FoodBank()

    while True:
        print("\n===== COMMUNITY FOOD BANK =====")
        print("1. Register Family")
        print("2. Add Food Packs")
        print("3. Distribute Food Packs")
        print("4. Show Report")
        print("5. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            family_id = input("Family ID: ")
            name = input("Family Name: ")
            members = read_integer("Number of Members: ")
            food_bank.register_family(family_id, name, members)

        elif choice == "2":
            quantity = read_integer("Packs to add: ")
            food_bank.add_food(quantity)

        elif choice == "3":
            family_id = input("Family ID: ")
            quantity = read_integer("Packs requested: ")
            food_bank.distribute_food(family_id, quantity)

        elif choice == "4":
            food_bank.show_report()

        elif choice == "5":
            print("Thank you for using Community Food Bank. Goodbye!")
            break

        else:
            print("Invalid choice. Please select an option from 1 to 5.")


if __name__ == "__main__":
    main()
