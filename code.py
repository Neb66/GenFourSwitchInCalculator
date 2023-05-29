type_chart = {
    'Normal': {
        'Rock': 0.5,
        'Ghost': 0,
    },
    'Fire': {
        'Fire': 0.5,
        'Water': 0.5,
        'Grass': 2,
        'Ice': 2,
        'Bug': 2,
        'Rock': 0.5,
        'Dragon': 0.5,
        'Steel': 2,
    },
    'Water': {
        'Fire': 2,
        'Water': 0.5,
        'Grass': 0.5,
        'Ground': 2,
        'Rock': 2,
        'Dragon': 0.5,
    },
    'Electric': {
        'Water': 2,
        'Electric': 0.5,
        'Grass': 0.5,
        'Ground': 0,
        'Flying': 2,
        'Dragon': 0.5,
    },
    'Grass': {
        'Fire': 0.5,
        'Water': 2,
        'Grass': 0.5,
        'Electric': 2,
        'Ice': 2,
        'Poison': 0.5,
        'Ground': 0.5,
        'Flying': 0.5,
        'Bug': 0.5,
        'Rock': 2,
        'Dragon': 0.5,
    },
    'Ice': {
        'Fire': 0.5,
        'Water': 0.5,
        'Grass': 2,
        'Ice': 0.5,
        'Ground': 2,
        'Flying': 2,
        'Dragon': 2,
        'Steel': 0.5,
    },
    'Fighting': {
        'Normal': 2,
        'Ice': 2,
        'Poison': 0.5,
        'Flying': 0.5,
        'Psychic': 0.5,
        'Bug': 0.5,
        'Rock': 2,
        'Ghost': 0,
        'Dark': 2,
        'Steel': 2,
        'Fairy': 0.5,
    },
    'Poison': {
        'Grass': 2,
        'Poison': 0.5,
        'Ground': 0.5,
        'Rock': 0.5,
        'Ghost': 0.5,
        'Steel': 0,
        'Fairy': 2,
    },
    'Ground': {
        'Fire': 2,
        'Electric': 2,
        'Grass': 2,
        'Poison': 2,
        'Flying': 0,
        'Bug': 0.5,
        'Rock': 2,
        'Steel': 2,
    },
    'Flying': {
        'Electric': 0.5,
        'Grass': 2,
        'Fighting': 2,
        'Bug': 2,
        'Rock': 0.5,
        'Steel': 0.5,
    },
    'Psychic': {
        'Fighting': 2,
        'Poison': 2,
        'Psychic': 0.5,
        'Dark': 0,
        'Steel': 0.5,
        'Fairy': 0.5,
    },
    'Bug': {
        'Fire': 0.5,
        'Grass': 2,
        'Fighting': 0.5,
        'Poison': 0.5,
        'Flying': 0.5,
        'Psychic': 2,
        'Ghost': 0.5,
        'Dark': 2,
        'Steel': 0.5,
        'Fairy': 0.5,
    },
    'Rock': {
        'Fire': 2,
        'Ice': 2,
        'Fighting': 0.5,
        'Ground': 0.5,
        'Flying': 2,
        'Bug': 2,
        'Steel': 0.5,
    },
    'Ghost': {
        'Normal': 0,
        'Psychic': 2,
        'Ghost': 2,
        'Dark': 0.5,
    },
    'Dragon': {
        'Dragon': 2,
        'Steel': 0.5,
        'Fairy': 0,
    },
    'Dark': {
        'Fighting': 0.5,
        'Psychic': 2,
        'Ghost': 2,
        'Dark': 0.5,
        'Fairy': 0.5,
    },
    'Steel': {
        'Fire': 0.5,
        'Water': 0.5,
        'Electric': 0.5,
        'Ice': 2,
        'Rock': 2,
        'Steel': 0.5,
        'Fairy': 2,
    },
    'Fairy': {
        'Fire': 0.5,
        'Fighting': 2,
        'Poison': 0.5,
        'Dragon': 2,
        'Dark': 2,
        'Steel': 0.5,
    },
}

def calculate_effectiveness(type1, type2):
    matchup_value = 1.0
    matchup_type1 = type_chart.get(type1, {})
    matchup_value *= matchup_type1.get(type2, 1.0)
    return matchup_value

def calculate_combined_effectiveness(user_types, ai_types):
    user_effectiveness = []
    ai_effectiveness = []
    
    for user_type in user_types:
        user_effectiveness.append(
            calculate_effectiveness(user_type, ai_types[0])
            * calculate_effectiveness(user_type, ai_types[1])
        )
    
    for ai_type in ai_types:
        ai_effectiveness.append(
            calculate_effectiveness(ai_type, user_types[0])
            * calculate_effectiveness(ai_type, user_types[1])
        )
    
    combined_effectiveness = user_effectiveness + ai_effectiveness
    return combined_effectiveness

results = []  # List to store the results

user_type1 = input("Enter your Pokemon's first type: ")
user_type2 = input("Enter your Pokemon's second type (leave blank if single type): ")

if user_type2 == "":
    user_type2 = user_type1
    
user_types = [user_type1, user_type2]

while True:
    user_name = input("Enter AI Pokemon name: ")
    ai_type1 = input("Enter AI trainer's Pokemon's first type: ")
    ai_type2 = input("Enter AI trainer's Pokemon's second type (leave blank if single type): ")

    # Duplicate the type if it's a single-type Pokémon
    if ai_type2 == "":
        ai_type2 = ai_type1

    ai_types = [ai_type1, ai_type2]

    combined_effectiveness = calculate_combined_effectiveness(user_types, ai_types)

    ai_effectiveness_1 = combined_effectiveness[2]
    ai_effectiveness_2 = combined_effectiveness[3]

    final_result = ai_effectiveness_1 + ai_effectiveness_2
    
    #This accounts for the overflow bug pointed out in Drxx's video, it is unclear what value is being assigned to
    #it but given that the value is somewhere between 1.5 and 2, this should account for the gap without any issues.
    if final_result == 8.0:
        final_result = 1.75

    results.append((user_name, final_result))  # Add the name and result to the list of results
    
    # Rank the results from highest to lowest
    results.sort(key=lambda x: x[1], reverse=True)
    
    # Print the ranked results
    print("Ranked Results:")
    for i, (name, result) in enumerate(results):
        print(f"Rank {i + 1}: {name} - Result: {result}x")

    choice = input("Do you want to continue (y/n)? ")
    if choice.lower() != 'y':
        break



