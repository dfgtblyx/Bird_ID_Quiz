# Bird ID Quiz App

This app helps you learn to identify birds using high-quality images from Macaulay Library, while tracking your familiarity with each species.

---

## Setup Instructions

1. **Edit the Bird List**

   Open `birds.csv` and replace the entries in the `bird_name` column with the species you want to study. Make sure to keep the `bird_name` column name.

2. **Run the App**

   Double-click `quiz_from_csv.exe` to launch the program.

3. **If You Update the List**

   After editing `birds.csv`, be sure to **delete** the generated file `bird_taxon_list.csv` before running the app again. This ensures that the taxon codes are updated correctly.

---

## How to Use the App

- The app will open a random bird photo gallery in your web browser.
- Try to guess the bird’s name before revealing it.
- Click **Show Name** to check your answer.
- Then mark the bird as:
  - Familiar
  - Somewhat Familiar
  - Unfamiliar (Skip)

Your familiarity is saved automatically in `familiarity.json` and persists across sessions.

---

##  Study Groups

You can choose a study mode using the dropdown at the top of the app window:

- **Unfamiliar** – birds not yet marked
- **Somewhat Familiar** – birds you know partially
- **Familiar** – birds you feel confident about
- **All** – includes every bird regardless of familiarity

---

## Files

| File Name              | Purpose                                           |
|------------------------|---------------------------------------------------|
| `birds.csv`            | Input file: List the birds you want to study     |
| `bird_taxon_list.csv`  | Auto-generated file with eBird taxon codes       |
| `familiarity.json`     | Auto-saved progress tracking your familiarity     |
| `quiz_from_csv.exe`    | Executable to launch the app                     |

---

##  Notes

- The app only opens links to eBird’s official media pages using taxon codes, so you **need to be online** to view bird images.
- This tool is intended for **personal and educational use only**. Please respect the terms of use of Macaulay Library and eBird.

---

Happy birding! 🐦
