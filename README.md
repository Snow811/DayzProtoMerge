# DayzProtoMerge

**DayzProtoMerge** is a lightweight tool for merging multiple `mapgroupproto.xml` files into a single master file. It’s designed for DayZ modders who need to consolidate loot group definitions across maps or mods without duplicating existing entries.

---

## 🧩 What It Does

- Scans all `.xml` files in the `source_files/` folder.
- Compares each `<group name="...">` block against the master file.
- Adds any missing `<group>` blocks to `master/mapgroupproto.xml`.
- Skips groups that already exist in the master (based on `name` only).
- Creates required folders and a blank master file on first run.

---

## 📁 Folder Structure

After first run, the tool will create:

```
DayzProtoMerge.exe
master/
└── mapgroupproto.xml        ← merged output file
source_files/
└── *.xml                    ← input files to merge
```

---

## 🚀 How to Use

1. Place your source `mapgroupproto.xml` files inside the `source_files/` folder.
2. **Rename each file** to something unique (e.g. `chernarus.xml`, `livonia.xml`, `custom_base.xml`) so they don’t overwrite each other.
3. Run `DayzProtoMerge.exe`.
4. The tool will:
   - Create folders if missing.
   - Create a blank master file if missing.
   - Merge all unique `<group>` blocks into `master/mapgroupproto.xml`.

---

## ⚠️ Important Notes

- Only the `<group name="...">` attribute is used for comparison.
- If a group already exists in the master file, it will **not** be merged again.
- The tool does **not** validate or modify existing groups — it only appends new ones.

---

## 🛠 Building from Source

If you want to build the executable yourself:

```bash
pip install pyinstaller
pyinstaller --onefile --name DayzProtoMerge Main.py
```

---

## 💬 Feedback & Contributions

Feel free to fork, modify, or submit issues if you want to extend functionality (e.g. logging, GUI, filtering by group type). This tool is built for speed and clarity — no fluff, just results.
