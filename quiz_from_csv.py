import tkinter as tk
import random
import webbrowser
import json
import csv
import os
import pandas as pd

FAMILIARITY_FILE = "familiarity.json"
TAXON_CSV = "bird_taxon_list.csv"
MY_LIST_CSV = "birds.csv"  # must contain 'bird_name' column
TAXONOMY_CSV = "ebird_taxonomy.csv"  # must contain 'English name' and 'species_code'


def create_taxon_list(my_list_csv, taxonomy_csv, output_csv):
    my_list = pd.read_csv(my_list_csv)
    my_list['bird_name_lower'] = my_list['bird_name'].str.strip().str.lower()

    taxonomy = pd.read_csv(taxonomy_csv)
    taxonomy['English name lower'] = taxonomy['English name'].str.strip().str.lower()

    merged = pd.merge(
        my_list,
        taxonomy,
        left_on='bird_name_lower',
        right_on='English name lower',
        how='left'
    )

    result = merged[['bird_name', 'species_code']].rename(columns={'species_code': 'taxon_code'})

    missing = result[result['taxon_code'].isna()]
    if not missing.empty:
        print("❌ Could not match the following bird names:")
        print(missing['bird_name'].to_string(index=False))

    result = result.dropna()
    result.to_csv(output_csv, index=False)
    print(f"✅ Created: {output_csv} with {len(result)} entries")


def load_bird_list(csv_path):
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return [{
            'name': row['bird_name'],
            'url': f"https://media.ebird.org/catalog?taxonCode={row['taxon_code']}&mediaType=photo&sort=rating_rank_desc"
        } for row in reader]


def save_familiarity(familiarity, path):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(familiarity, f, indent=2)


def load_familiarity(path):
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}


class BirdQuizApp:
    def __init__(self, master, bird_list):
        self.master = master
        self.master.title("🕊️ Bird ID Quiz")

        self.bird_list = bird_list
        self.familiarity_file = FAMILIARITY_FILE
        self.familiarity = load_familiarity(self.familiarity_file)
        self.group_var = tk.StringVar(value="unfamiliar")

        self.label = tk.Label(master, text="Guess the Bird!", font=("Arial", 16))
        self.label.pack(pady=10)

        dropdown = tk.OptionMenu(master, self.group_var, "unfamiliar", "somewhat familiar", "familiar", "all", command=self.update_group)
        dropdown.pack(pady=5)

        self.name_label = tk.Label(master, text="", font=("Arial", 14))
        self.name_label.pack(pady=5)

        self.buttons = tk.Frame(master)
        self.buttons.pack(pady=10)

        self.reveal_btn = tk.Button(self.buttons, text="Show Name", command=self.show_name)
        self.reveal_btn.grid(row=0, column=0, padx=5)

        self.somewhat_btn = tk.Button(self.buttons, text="Somewhat Familiar", command=self.mark_somewhat)
        self.somewhat_btn.grid(row=0, column=1, padx=5)

        self.familiar_btn = tk.Button(self.buttons, text="Familiar", command=self.mark_familiar)
        self.familiar_btn.grid(row=0, column=2, padx=5)

        self.unfamiliar_btn = tk.Button(self.buttons, text="Unfamiliar (Skip)", command=self.next_bird)
        self.unfamiliar_btn.grid(row=0, column=3, padx=5)

        self.status = tk.Label(master, text="", fg="gray")
        self.status.pack()

        self.current = None
        self.remaining = []
        self.update_group()

    def update_group(self, _event=None):
        selected_group = self.group_var.get()
        if selected_group == "all":
            self.remaining = self.bird_list.copy()
        else:
            self.remaining = [
                b for b in self.bird_list
                if self.familiarity.get(b['name'], 'unfamiliar') == selected_group
            ]
        self.next_bird()

    def next_bird(self):
        if not self.remaining:
            self.label.config(text="🎉 Done! No more birds in this group.")
            self.name_label.config(text="")
            return

        self.current = random.choice(self.remaining)
        self.remaining.remove(self.current)

        bird_name, bird_url = self.current['name'], self.current['url']
        webbrowser.open_new_tab(bird_url)

        self.label.config(text="Guess the Bird!")
        self.name_label.config(text="")
        self.status.config(text=f"{len(self.remaining)} left in '{self.group_var.get()}'")

    def show_name(self):
        if self.current:
            self.name_label.config(text=self.current['name'])

    def mark_somewhat(self):
        if self.current:
            self.familiarity[self.current['name']] = 'somewhat familiar'
            save_familiarity(self.familiarity, self.familiarity_file)
            self.next_bird()

    def mark_familiar(self):
        if self.current:
            self.familiarity[self.current['name']] = 'familiar'
            save_familiarity(self.familiarity, self.familiarity_file)
            self.next_bird()


if __name__ == "__main__":
    if not os.path.exists(TAXON_CSV):
        print("⚙️ Generating taxon list...")
        create_taxon_list(MY_LIST_CSV, TAXONOMY_CSV, TAXON_CSV)

    bird_list = load_bird_list(TAXON_CSV)
    root = tk.Tk()
    app = BirdQuizApp(root, bird_list)
    root.mainloop()
