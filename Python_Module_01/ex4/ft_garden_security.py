#!/usr/bin/env python3

class SecurePlant:
    """A plant class with secure, private attributes for height and age."""

    def __init__(self, name: str, height: int, age: int):
        """
        Initialize a SecurePlant instance.

        Args:
            name (str): Name of the plant.
            height (int): Initial height in cm.
            age (int): Initial age in days.
        """
        self.name = name
        self.__height = height
        self.__age = age

    def set_height(self, new_height: int):
        """
        Safely update the plant's height if positive.

        Args:
            new_height (int): New height in cm.

        Prints a warning if the new height is invalid.
        """
        if new_height > 0:
            self.__height = new_height
        else:
            print(
                "\nInvalid operation attempted: "
                f"height {new_height}cm [REJECTED]"
                )
            print("Security: Negative height rejected")

    def set_age(self, new_age: int):
        """
        Safely update the plant's age if positive.

        Args:
            new_age (int): New age in days.

        Prints a warning if the new age is invalid.
        """
        if new_age > 0:
            self.__age = new_age
        else:
            print(
                "\nInvalid operation attempted: "
                f"age {new_age} days [REJECTED]"
            )
            print("Security: Negative age rejected")

    def get_height(self):
        """
        Retrieve the plant's current height.

        Returns:
            int: Current height in cm.
        """
        return self.__height

    def get_age(self):
        """
        Retrieve the plant's current age.

        Returns:
            int: Current age in days.
        """
        return self.__age

    def get_info(self):
        """Print the current information of the plant."""
        print(
            f"\nCurrent plant: {self.name} "
            f"({self.__height}cm, {self.__age} days)"
        )


if __name__ == "__main__":
    """Demo for the SecurePlant class showing secure attribute updates."""
    rose = SecurePlant("Rose", 15, 20)
    rose.set_height(25)
    rose.set_age(30)

    print("=== Garden Security System ===")
    print(f"Plant created: {rose.name}")
    print(f"Height updated: {rose.get_height()}cm [OK]")
    print(f"Age updated: {rose.get_age()} days [OK]")
    rose.set_height(-5)
    rose.get_info()
