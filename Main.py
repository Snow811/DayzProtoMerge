import os
import sys
import xml.etree.ElementTree as ET

# 🧭 Get base directory (works for .py and .exe)
def get_base_dir():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)  # Running as .exe
    else:
        return os.path.dirname(os.path.abspath(__file__))  # Running as script

base_dir = get_base_dir()
source_dir = os.path.join(base_dir, "source_files")
master_file = os.path.join(base_dir, "master", "mapgroupproto.xml")

# 📁 Ensure required folders and master file exist
def ensure_directories():
    os.makedirs(source_dir, exist_ok=True)
    os.makedirs(os.path.dirname(master_file), exist_ok=True)

    if not os.path.exists(master_file):
        root = ET.Element("groups")
        tree = ET.ElementTree(root)
        tree.write(master_file, encoding="utf-8", xml_declaration=True)
        print("📁 Created blank master file at:", master_file)

# 🔍 Extract all group names from a tree
def get_group_names(tree):
    return {group.attrib.get("name") for group in tree.findall(".//group")}

# 🔄 Merge missing groups into master
def merge_groups(master_path, source_folder):
    master_tree = ET.parse(master_path)
    master_root = master_tree.getroot()
    master_names = get_group_names(master_tree)

    added_count = 0

    for filename in os.listdir(source_folder):
        if filename.endswith(".xml"):
            file_path = os.path.join(source_folder, filename)
            try:
                tree = ET.parse(file_path)
                root = tree.getroot()

                for group in root.findall(".//group"):
                    name = group.attrib.get("name")
                    if name and name not in master_names:
                        master_root.append(group)
                        master_names.add(name)
                        added_count += 1
            except ET.ParseError:
                print(f"⚠️ Skipped invalid XML file: {filename}")

    master_tree.write(master_path, encoding="utf-8", xml_declaration=True)
    print(f"✅ Merge complete. {added_count} new <group> blocks added.")

# 🚀 Main entry point
if __name__ == "__main__":
    ensure_directories()
    merge_groups(master_file, source_dir)
