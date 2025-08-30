# Bird ID Quiz

This app helps you learn to identify birds using high-quality images from Macaulay Library while tracking your familiarity with each species. It's built for self-paced study and works on Windows, Linux, and macOS.

---

## Installation & Setup

### Windows Users

You have **two options** to run this application:

#### Option 1: Run the Executable (Recommended)

1. Go to the [Releases Page](https://github.com/dfgtblyx/Bird_ID_Quiz/releases).
2. Download the ZIP under **“Source code (zip)”** and extract it.
3. Then download the **larger** `quiz_from_csv.exe` separately from the same release page.
4. Replace the small (~1KB) `quiz_from_csv.exe` inside the extracted folder with the downloaded one.
5. Double-click `quiz_from_csv.exe` to launch the app.

> If Windows shows a “protected your PC” message, click **More info** → **Run anyway**.

#### Option 2: Run via Python

1. Make sure Python 3.10+ is installed.
2. Clone the repo or extract the ZIP.
3. In the folder, run:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python quiz_from_csv.py
```

---

### Linux & macOS Users

Use the Python version:

1. Ensure Python 3.10+ is installed.
2. Clone or extract the repository.
3. In terminal:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 quiz_from_csv.py
```

> You may need to install `tkinter`:
> On Ubuntu/Debian: `sudo apt install python3-tk`

---

## How to Use the App

1. **Edit the Bird List**  
   Open `birds.csv` and enter species names in the `bird_name` column. This is your personal study list. Make sure to keep the `bird_name` column name.

2. **Launch the App**  
   Use the .exe or Python script to open the quiz interface. If you're not set up yet, refer to [Installation & Setup](#installation--setup).

3. **Study Sessions**  
   The app opens a random bird’s Macaulay Library photo gallery in your browser.

4. **Guess & Mark**  
   Try to guess the bird before clicking **Show Name**. Then mark it as:
   - **Familiar**
   - **Somewhat Familiar**
   - **Unfamiliar (Skip)**

   Your familiarity is tracked in `familiarity.json` and saved between sessions.

5. **If You Update the List**  
   After editing `birds.csv`, be sure to **delete** the generated file `bird_taxon_list.csv` before running the app again. This ensures that the taxon codes are updated correctly.
---

## Study Modes
Use the dropdown menu at the top of the app to filter which birds are shown:

- **Unfamiliar** – not yet marked
- **Somewhat Familiar** – you know partially
- **Familiar** – you feel confident
- **All** – shows everything

---

## Key Files

| File Name              | Purpose                                           |
|------------------------|---------------------------------------------------|
| `birds.csv`            | Input file: list the birds you want to study     |
| `bird_taxon_list.csv`  | Auto-generated with eBird taxon codes            |
| `familiarity.json`     | Tracks your progress and familiarity              |
| `quiz_from_csv.exe`    | Standalone Windows executable                     |
| `quiz_from_csv.py`     | Source Python code                                |

> After updating `birds.csv`, delete `bird_taxon_list.csv` before running again to regenerate correct taxon codes.

---

## Notes

- This app **requires an internet connection** to display bird images.
- Images are opened using official Macaulay Library links. No media is downloaded or stored locally.
- For **personal and educational use only**.
- This project was developed with the help of ChatGPT for code generation, debugging, and documentation guidance.

---  

<span style="font-size: 2em; font-weight: bold;">Happy birding!</span>