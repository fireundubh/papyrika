# Papyrika

Papyrika fixes ScriptName declarations in Papyrus scripts to match file names.

## Why

When you change the file name of a Papyrus script, you also need to change the ScriptName declaration usually at the top of the script; otherwise, the Papyrus compiler will print an error and not compile the script.

If you need to fix one file, the problem is simple. If you need to fix a hundred files, you need an automated solution.

Just sprinkle some Papyrika.

## Requirements

Python 3 (tested with Python 3.7.2)

## Usage

Papyrika is super simple.

```
-i, --input       Source folder
--recursive       Recursively process scripts in source folder
```

### Example

```
python3 E:/repos/papyrika -i "E:\projects\fallout4\Auto Loot\scripts\source\User\AutoLoot\Fragments\Terminals"
```
