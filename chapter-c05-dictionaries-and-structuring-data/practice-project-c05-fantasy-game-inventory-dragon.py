# Fantasy game inventory

def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print("Total number of items: " + str(item_total))#

def addToInventory(inventory, loot):
    for item in loot:
        # Item may or may not exist in inventory; use setdefault to add item without increasing count
        inventory.setdefault(str(item), 0)
        # Then increase count
        inventory[item] += 1

if __name__ == "__main__":
    stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    displayInventory(stuff)

    print("You slay the dragon! Collect your loot...")
    dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    addToInventory(stuff, dragonLoot)

    displayInventory(stuff)