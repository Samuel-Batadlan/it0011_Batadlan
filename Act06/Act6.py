class Item:
    def __init__(self, item_id, name, description, price):
        # Validate inputs
        if not isinstance(item_id, int):
            raise TypeError("ID must be an integer")
        if not name or not name.strip():
            raise ValueError("Name cannot be empty")
        if not description or not isinstance(description, str):
            raise ValueError("Description must be a valid string")
        
        try:
            price = float(price)
            if price < 0:
                raise ValueError("Price cannot be negative")
        except (ValueError, TypeError):
            raise ValueError("Price must be a valid number")
            
        self.id = item_id
        self.name = name.strip()
        self.description = description.strip()
        self.price = price
    
    def display(self):
        print(f"│ {self.id:<5} │ {self.name:<20} │ {self.description:<30} │ ₱{self.price:<10.2f}│")


class ItemManager:
    def __init__(self):
        self.inventory = {}
    
    def add_item(self):
        try:
            print("\n" + "┌" + "─" * 48 + "┐")
            print("│" + " ADD NEW ITEM ".center(48) + "│")
            print("└" + "─" * 48 + "┘")
            
            item_id = int(input("Enter item ID: "))
            if item_id in self.inventory:
                print("\nError: ID already exists!")
                return
            
            name = input("Enter item name: ").strip()
            if not name:
                print("\nError: Name cannot be empty!")
                return
                
            description = input("Enter description: ").strip()
            
            try:
                price = float(input("Enter price: "))
                if price < 0:
                    print("\nError: Price can't be negative!")
                    return
            except ValueError:
                print("\nError: Invalid price format!")
                return
                
            self.inventory[item_id] = Item(item_id, name, description, price)
            print(f"\n{name} added successfully!")
            
        except ValueError:
            print("\nError: Invalid input! Please enter a number for ID.")
        except Exception as e:
            print(f"\nError: {str(e)}")
    
    def display_items(self):
        if not self.inventory:
            print("\nNo items in inventory!")
            return
            
        print("\n" + "┌" + "─" * 76 + "┐")
        print("│" + " INVENTORY ITEMS ".center(74) + "  │")
        print("├" + "─" * 7 + "┬" + "─" * 22 + "┬" + "─" * 32 + "┬" + "─" * 12 + "┤")
        print("│ ID    │ Name                 │ Description                    │ Price      │")
        print("├" + "─" * 7 + "┼" + "─" * 22 + "┼" + "─" * 32 + "┼" + "─" * 12 + "┤")
        
        for item in self.inventory.values():
            item.display()
            
        print("└" + "─" * 7 + "┴" + "─" * 22 + "┴" + "─" * 32 + "┴" + "─" * 12 + "┘")
    
    def update_item(self):
        try:
            print("\n" + "┌" + "─" * 48 + "┐")
            print("│" + " UPDATE ITEM ".center(48) + "│")
            print("└" + "─" * 48 + "┘")
            
            item_id = int(input("Enter item ID to update: "))
            if item_id not in self.inventory:
                print("\nError: Item not found!")
                return
                
            print("\nLeave blank to keep current value:")
            current = self.inventory[item_id]
            
            name = input(f"New name [{current.name}]: ") or current.name
            description = input(f"New description [{current.description}]: ") or current.description
            
            price_input = input(f"New price [₱{current.price}]: ")
            
            try:
                price = float(price_input) if price_input else current.price
                if price < 0:
                    print("\nError: Price can't be negative!")
                    return
            except ValueError:
                print("\nError: Invalid price format!")
                return
                
            self.inventory[item_id] = Item(item_id, name, description, price)
            print("\nItem updated successfully!")
            
        except ValueError:
            print("\nError: Invalid ID format! Please enter a number.")
        except Exception as e:
            print(f"\nError: {str(e)}")
    
    def delete_item(self):
        try:
            print("\n" + "┌" + "─" * 48 + "┐")
            print("│" + " DELETE ITEM ".center(48) + "│")
            print("└" + "─" * 48 + "┘")
            
            item_id = int(input("Enter item ID to remove: "))
            if item_id not in self.inventory:
                print("\nError: Item not found!")
                return
                
            item = self.inventory.pop(item_id)
            print(f"\n{item.name} removed from inventory!")
            
        except ValueError:
            print("\nError: Invalid ID! Please enter a number.")
        except Exception as e:
            print(f"\nError: {str(e)}")


def display_menu():
    print("\n" + "┌" + "─" * 40 + "┐")
    print("│" + " ITEM MANAGEMENT SYSTEM ".center(40) + "│")
    print("├" + "─" * 40 + "┤")
    print("│  [1] Add New Item                      │")
    print("│  [2] View All Items                    │")
    print("│  [3] Update Existing Item              │")
    print("│  [4] Delete Item                       │")
    print("│  [5] Exit System                       │")
    print("└" + "─" * 40 + "┘")


def main():
    item_manager = ItemManager()
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == "1":
            item_manager.add_item()
        elif choice == "2":
            item_manager.display_items()
        elif choice == "3":
            item_manager.update_item()
        elif choice == "4":
            item_manager.delete_item()
        elif choice == "5":
            print("\nThank you for using the Item Management System. Goodbye!")
            break
        else:
            print("\nInvalid choice! Please try again.")


if __name__ == "__main__":
    main()