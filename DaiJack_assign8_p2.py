pokemon_names = ['charmander', 'squirtle', 'bulbasaur', 'gyrados']
pokemon_amounts = [3, 2, 5, 1]
pokemon_fees = [100, 50, 25, 1000]
pokemon_types = [['fire'], ['water'], ['grass'], ['water', 'flying']]
while True:
    accepted_type = ['bug', 'dark', 'dragon', 'electric', 'fairy', 'fighting', 'fire', 'flying', 'ghost', 'grass', 'ground', 'ice', 'normal', 'poison', 'psychic', 'rock', 'steel', 'water']
    print("Welcome to the Pokemon Center!")
    user = input("(a)dd, (r)emove, r(e)port, (s)earch by name, search by (t)ype, (l)ist or (q)uit: ")
    if user.upper() == "S":
        search = input("Name of Pokemon to search for: ")
        if search.lower() in pokemon_names:
            for i in range(len(pokemon_names)):
                if search == pokemon_names[i]:
                    amount = pokemon_amounts[i]
                    fee = pokemon_fees[i]
                    print(f"We have {amount} {search.capitalize()} at the Pokemon Center")
                    print(f"It will cost ${fee} to adopt this Pokemon")
                    print(f"{search.capitalize()} have the following types: {' '.join(pokemon_types[i][:]).title()}")
                    
                    
        else:
            print(f"We do not have any {search.capitalize()} at the Pokemon Center")
    elif user.upper() == "Q":
        print("See you next time!")
        break
    elif user.upper() == "L":
        print("Name                    Amount Available        Adoption Fee Type(s)")
        for i in range(len(pokemon_names)):
            element = ' '.join(pokemon_types[i][:]).title()
            fee = pokemon_fees[i]
            pokemon = pokemon_names[i]
            print("{:<20} {:>19} {:>19} {:>1}".format(pokemon.capitalize(), pokemon_amounts[i], "{:,.2f}".format(fee), element))
    elif user.upper() == "T":
        energy = input("Enter Pokemon type: ")
        print("Name                    Amount Available        Adoption Fee Type(s)")
        for i in range(len(pokemon_types)):
            if energy in pokemon_types[i]:
                element = ' '.join(pokemon_types[i][:]).title()
                pokemon = pokemon_names[i]
                fee = pokemon_fees[i]
                print("{:<20} {:>19} {:>19} {:>1}".format(pokemon.capitalize(), pokemon_amounts[i], "{:,.2f}".format(fee), element))

    elif user.upper() == "A":
        new_pokemon = input("Enter name of new pokemon: ")
        if new_pokemon.lower() not in pokemon_names:
            while True:
                try:  
                    new_amount = int(input("How many of these Pokemon are you adding? "))
                    pokemon_amounts.append(new_amount)
                    break
                except ValueError:
                    print("Invalid, please try again")
            while True:
                try:  
                    new_fee = float(input("What is the adoption fee for this Pokemon? "))
                    pokemon_fees.append(new_fee)
                    break
                except ValueError:
                    print("Invalid, please try again")
            print("Next you will be prompted to enter the 'types' for this Pokemon.  Pokemon can have multiple types. Type 'help' to view all possible Pokemon types, and type 'end' to stop entering types. You must enter at least one valid 'type'")
            pokemon_types.append([])
            while True:
                new_type = input("What type of Pokemon is this? ")
                if new_type == "help":
                    print("* bug\n* dark\n* dragon\n* electric\n* fairy\n* fighting\n* fire\n* flying\n* ghost\n* grass\n* ground\n* ice\n* normal\n* poison\n* psychic\n* rock\n* steel\n* water")
                elif new_type.lower() == "end" :
                    print("Pokemon added")
                    pokemon_names.append(new_pokemon)
                    break
                elif new_type.lower() not in accepted_type:
                    print("Invalid, please try again")

                else:
                    print("Type", new_type.lower(), "added")
                    pokemon_types[len(pokemon_types) - 1].append(new_type.lower())
                
        else:
            print("Duplicate name, add operation cancelled")
            
    elif user.upper() == "R":
        remove = input("Enter name of Pokemon to remove: ")
        if remove.lower() in pokemon_names:
            for d in range(len(pokemon_names)):
                if remove.lower() == pokemon_names[d-1]:
                    pokemon_names.remove(remove)
                    del pokemon_types[d-1]
                    del pokemon_fees[d-1]
                    del pokemon_amounts[d-1]
                    print("Pokemon removed")
        else:
            print("Pokemon not found, cannot remove")
    elif user.upper() == "E":
        high = pokemon_fees.index(max(pokemon_fees))
        low = pokemon_fees.index(min(pokemon_fees))
        print(f"Highest priced Pokemon: {pokemon_names[high]} @ ${max(pokemon_fees):,.2f} per Pokemon")
        print(f"Lowest priced Pokemon: {pokemon_names[low]} @ ${min(pokemon_fees):,.2f} per Pokemon")
        total = 0
        for i in pokemon_amounts:
            total += i * pokemon_fees[pokemon_amounts.index(i)]
        print(f"Total cost to adopt all Pokemon in the Center: ${total: ,.2f}")

        
        
        
    else:
        print("Unknown command, please try again")



