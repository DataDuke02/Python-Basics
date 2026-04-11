# Task: create a dictionary called FRUIT_COLORS where:
# apple = red, banana = yellow, grape = purple
# Then write a function get_color(fruit_name) that returns the color
# if found, or "unknown" if not in the dictionary.
# This teaches you: dictionaries, .get(), functions with defaults

FRUIT_COLORS = {"apple":"red",
                "banana":"yellow",
                "grape":"purple"}
def get_color(fruit_name):
    return FRUIT_COLORS.get(fruit_name.lower(),"UNKNOWN")

print(get_color("apple"))
print(get_color("banana"))
print(get_color("grape"))
