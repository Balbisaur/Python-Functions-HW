while True:
    empty_list = input('would you like to add to your shopping list? yes or no: ')
    shopping_list = []
    if empty_list == 'yes':
        print('lets make that shopping list!')
    else:
        print('maybe another day')
        break
        
    for items in range(len(empty_list)):
        items = input()
        shopping_list.append(items)
        
    print('shopping_list', shopping_list)
    
    empty_list = input('which item would you like to remove? ')

    shopping_list.remove(items)
    print('shopping_list', shopping_list)
    break
#I was able to make the user add to the shopping list but only 3 items, not sure what I can do to raise the limit
#I was able to add the remove feature... but I am running into a problem. whenever I remove a certain item from the shopping list,
# it removes the last item instead of the one I chose.
