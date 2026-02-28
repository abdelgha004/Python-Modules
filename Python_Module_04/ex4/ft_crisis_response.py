print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")


def access_archive(file_name):
    """
    Access an archive file safely and handle
    missing, restricted, or corrupted scenarios.
    """
    print(f"CRISIS ALERT: Attempting access to '{file_name}'...")

    try:
        with open(file_name, "r") as f:
            content = f.read()
            print(f"SUCCESS: Archive recovered - \"{content}\"")
            print("STATUS: Normal operations resumed")

    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")

    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")

    except Exception:
        print("RESPONSE: Archive corrupted")
        print("STATUS: Crisis contained\n")


access_archive("lost_archive.txt")
access_archive("classified_vault.txt")
access_archive("standard_archive.txt")

print("All crisis scenarios handled successfully. Archives secure.")
