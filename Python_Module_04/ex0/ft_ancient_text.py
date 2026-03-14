try:
    f = open("ancient_fragment.txt", "r")
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    print("Accessing Storage Vault: ancient_fragment.txt")
    print("Connection established...\n")
    print("RECOVERED DATA:")
    print(f.read())
    f.close()
    print("\nData recovery complete. Storage unit disconnected.")

except FileNotFoundError:
    print("ERROR: Storage vault not found. Run data generator first.")
