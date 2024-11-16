## What's This About?

Hey there! This little project was born out of my love for modding. I was working on a mod pack for **Dragon Age: Origins** (amazing game, right?) and needed to compare two folders for duplicate files. I couldn’t find a program that worked exactly how I wanted (or maybe I’m just bad at finding stuff), so I thought, why not make my own? And here we are—a simple Python script that gets the job done.  

---

## What Does It Do?

This script compares files between two folders to find duplicates. It works by hashing file contents (using MD5) and generates a neat XML report listing all duplicates. Here’s what it can do for you:

- Detect exact duplicate files **only across the two folders** (ignoring duplicates within the same folder).
- Provide a detailed XML report showing:
  - The file paths of the duplicates.
  - The file sizes.
  - Their MD5 hash values (for the geeks among us).
- Save you time and effort when managing large folders, whether for mods, backups, or any other project.

---

## How to Use It?

1. **Run the Script**
Simply run the Python script (by first inserting the script into the same folder where the compared are located):
   ```
   python duplicate_finder.py
   ```
2. **Enter Folder Names**   
When prompted, enter the names of the two folders you want to compare. These should be relative to where the script is located, like this:
    ```
    Enter the name of the first folder: Mods_Folder1
    Enter the name of the second folder: Mods_Folder2
    ```
3. **Check generated XML file**   
If duplicates are found, the script creates an XML file called duplicates.xml in the same folder as the script. Open it in your favorite editor to see the results.
