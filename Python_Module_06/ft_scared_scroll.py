import alchemy
import alchemy.elements

print("\n=== Sacred Scroll Mastery ===\n")

print("Testing direct module access:", alchemy.elements.create_fire())
print("alchemy.elements.create_fire():", alchemy.elements.create_fire())
print("alchemy.elements.create_water():", alchemy.elements.create_water())
print("alchemy.elements.create_earth():", alchemy.elements.create_earth())
print("alchemy.elements.create_air():", alchemy.elements.create_air())

print("\nTesting package-level access (controlled by __init__.py):")

print("alchemy.create_fire():", alchemy.create_fire())
print("alchemy.create_water():", alchemy.create_water())

try:
    print("alchemy.create_earth(): ", alchemy.create_earth())
except AttributeError as e:
    print("alchemy.create_earth(): AttributeError - not exposed")

try:
    print("alchemy.create_air(): ", alchemy.create_air())
except AttributeError as e:
    print("alchemy.create_air(): AttributeError - not exposed")

print("\nPackage metadata:")
print("Version:", alchemy.__version__)
print("Author:", alchemy.__author__)