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


import customtkinter as ctk
from PIL import Image, ImageTk

ctk.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

# Create a tkinter window
window = ctk.CTk()
window.title("Gen 4 Switch-In Calculator")
window.geometry("600x400")

# Frame for user's Pokémon
user_frame = ctk.CTkFrame(window)
user_frame.pack(side="left", padx=10, pady=10)

# Label and dropdown for user's Pokémon type 1
user_type1_label = ctk.CTkLabel(user_frame, text="User Pokémon Type 1:")
user_type1_label.pack()

user_type1_combo = ctk.CTkComboBox(user_frame, values=list(type_chart.keys()))
user_type1_combo.pack()

# Label and dropdown for user's Pokémon type 2
user_type2_label = ctk.CTkLabel(user_frame, text="User Pokémon Type 2:")
user_type2_label.pack()

user_type2_combo = ctk.CTkComboBox(user_frame, values=list(type_chart.keys()) + [""])
user_type2_combo.pack()

# Frame for AI's Pokémon
ai_frame = ctk.CTkFrame(window)
ai_frame.pack(side="left", padx=10, pady=10)

# Entry for AI Pokémon name
ai_name_label = ctk.CTkLabel(ai_frame, text="AI Pokémon Name:")
ai_name_label.pack()

ai_name_entry = ctk.CTkEntry(ai_frame)
ai_name_entry.pack()

# Label and dropdown for AI's Pokémon type 1
ai_type1_label = ctk.CTkLabel(ai_frame, text="AI Pokémon Type 1:")
ai_type1_label.pack()

ai_type1_combo = ctk.CTkComboBox(ai_frame, values=list(type_chart.keys()))
ai_type1_combo.pack()

# Label and dropdown for AI's Pokémon type 2
ai_type2_label = ctk.CTkLabel(ai_frame, text="AI Pokémon Type 2:")
ai_type2_label.pack()

ai_type2_combo = ctk.CTkComboBox(ai_frame, values=list(type_chart.keys()) + [""])
ai_type2_combo.pack()

# Frame for displaying results
results_frame = ctk.CTkFrame(window)
results_frame.pack(pady=10)

# Label for displaying results
results_label = ctk.CTkLabel(results_frame, text="Results:")
results_label.pack()

# Listbox for displaying ranked results
results_listbox = ctk.CTkTextbox(results_frame, width=200, height=200)
results_listbox.pack()

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

results = []

def calculate_battle_effectiveness():
    user_type1 = user_type1_combo.get()
    user_type2 = user_type2_combo.get() or user_type1
    user_types = [user_type1, user_type2]

    ai_name = ai_name_entry.get()
    ai_type1 = ai_type1_combo.get()
    ai_type2 = ai_type2_combo.get() or ai_type1
    ai_types = [ai_type1, ai_type2]

    combined_effectiveness = calculate_combined_effectiveness(user_types, ai_types)

    ai_effectiveness_1 = combined_effectiveness[2]
    ai_effectiveness_2 = combined_effectiveness[3]

    final_result = ai_effectiveness_1 + ai_effectiveness_2

    # This accounts for the overflow bug pointed out in Drxx's video
    if final_result == 8.0:
        final_result = 1.75

    result = f"{ai_name} - Result: {final_result:.2f}x"
    results.append(result)
    ranked_results = sorted(results, key=lambda x: float(x.split(":")[1].split("x")[0].strip()), reverse=True)
    
    results_listbox.configure(state='normal')
    results_listbox.delete(0.0, ctk.END)
    
    for ranked_result in ranked_results:
        results_listbox.insert(ctk.END, ranked_result + "\n")
    results_listbox.configure(state='disabled')
    
def clear_results():
    results_listbox.configure(state='normal')
    results_listbox.delete("0.0", ctk.END)
    results_listbox.configure(state='disabled')
    
def rank_and_sort_results():
    results = results_listbox.get(0.0, ctk.END).splitlines()
    ranked_results = []
    for result in results:
        parts = result.split(":")
        if len(parts) == 2:
            value = parts[1].split("x")[0].strip()
            try:
                float_value = float(value)
                ranked_results.append((result, float_value))
            except ValueError:
                pass
    ranked_results = sorted(ranked_results, key=lambda x: x[1], reverse=True)
    results_listbox.delete(0.0, ctk.END)
    for result, _ in ranked_results:
        results_listbox.insert(ctk.END, result)

# Button for calculating battle effectiveness
calculate_button = ctk.CTkButton(window, text="Calculate", command=calculate_battle_effectiveness)
calculate_button.pack(pady=10)

# Button to clear results
clear_button = ctk.CTkButton(window, text="Clear Results", command=clear_results)
clear_button.pack(pady=10)

window.mainloop()





