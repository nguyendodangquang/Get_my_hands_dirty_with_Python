inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'dagger','gold coin' ]

def addToInventory(inventory, addedItems):
    for i in range(len(addedItems)):
        if addedItems[i] in inventory:
            inventory[addedItems[i]] += 1
        else:
            inventory.setdefault(addedItems[i], 1)
    return inventory

def displayInventory(inventory):
    print('Inventor have: ')
    itemtotal = 0
    for k, v in inventory.items():
        print(k + ': ' + str(v))
        itemtotal = itemtotal + v
    print('Total items: ' + str(itemtotal))

inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
