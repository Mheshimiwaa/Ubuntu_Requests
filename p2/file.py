filename = input("Enter the filename to read: ")

try:
    
    with open(filename, "r") as f:
        content = f.read()

    # Modify content (uppercase)
    modified = content.upper()

    # Create new filename
    new_filename = "modified_" + filename

    # Write modified content into new file
    with open(new_filename, "w") as f:
        f.write(modified)

    print(f"✅ File processed successfully! Saved as '{new_filename}'")

except FileNotFoundError:
    print("❌ Error: File not found.")
except PermissionError:
    print("❌ Error: You don’t have permission to read this file.")
except Exception as e:
    print(f"❌ Unexpected error: {e}")
