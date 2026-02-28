print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
print("Initializing new storage unit: new_discovery.txt")
print("Storage unit created successfully...\n")
print("Inscribing preservation data...")

f = open("new_discovery.txt", "w")

f.write("{[}ENTRY 001{]} New quantum algorithm discovered\n")
f.write("{[}ENTRY 002{]} Efficiency increased by 347%\n")
f.write("{[}ENTRY 003{]} Archived by Data Archivist trainee\n")
f.close()

f = open("new_discovery.txt", "r")

print(f.read())
f.close()

print("Data inscription complete. Storage unit sealed.")
print("Archive 'new_discovery.txt' ready for long-term preservation.")
