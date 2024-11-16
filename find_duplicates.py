import os
import hashlib
import xml.etree.ElementTree as ET
from xml.dom import minidom

def hash_file(file_path):
    """Compute MD5 hash of a file."""
    hasher = hashlib.md5()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()

def find_duplicates(folder1, folder2):
    """Find duplicate files in the second folder compared to the first folder."""
    folder1_hashes = {}
    duplicates = []

    # Hash files in the first folder
    for root, _, files in os.walk(folder1):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = hash_file(file_path)
            folder1_hashes[file_hash] = file_path

    # Compare files in the second folder against the first folder
    for root, _, files in os.walk(folder2):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = hash_file(file_path)
            if file_hash in folder1_hashes:
                duplicates.append((file_path, folder1_hashes[file_hash], file_hash))

    return duplicates

def write_to_pretty_xml(duplicates, output_file):
    """Write duplicate file pairs to a pretty-printed XML file."""
    root = ET.Element("Duplicates")

    for file2, file1, file_hash in sorted(duplicates, key=lambda x: os.path.basename(x[0])):
        duplicate = ET.SubElement(root, "DuplicatePair")
        ET.SubElement(duplicate, "File1", attrib={"Size": str(os.path.getsize(file1))}).text = file1
        ET.SubElement(duplicate, "File2", attrib={"Size": str(os.path.getsize(file2))}).text = file2
        ET.SubElement(duplicate, "Hash").text = file_hash

    # Pretty print XML
    xml_str = ET.tostring(root, encoding="utf-8")
    pretty_xml = minidom.parseString(xml_str).toprettyxml(indent="    ")

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(pretty_xml)

if __name__ == "__main__":
    # Prompt user for folder names
    folder1 = input("Enter the name of the first folder: ").strip()
    folder2 = input("Enter the name of the second folder: ").strip()

    # Get the absolute paths of the folders
    base_path = os.path.dirname(os.path.abspath(__file__))
    folder1_path = os.path.join(base_path, folder1)
    folder2_path = os.path.join(base_path, folder2)

    # Ensure both folders exist
    if not os.path.exists(folder1_path):
        print(f"Folder '{folder1}' does not exist.")
    elif not os.path.exists(folder2_path):
        print(f"Folder '{folder2}' does not exist.")
    else:
        # Find duplicate files
        duplicates = find_duplicates(folder1_path, folder2_path)

        # Output results
        if duplicates:
            output_file = os.path.join(base_path, "duplicates.xml")
            write_to_pretty_xml(duplicates, output_file)
            print(f"Duplicate files found. Results saved to '{output_file}'.")
        else:
            print("No duplicate files found.")
