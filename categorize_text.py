# Task: write a function called categorize_text(text) that:
# - returns "code" if the word "def" or "import" is in the text
# - returns "note" if the word "todo" or "meeting" is in the text
# - returns "other" for everything else
# Test it with three different strings.
# This teaches you: string checking with 'in', if/elif/else

def categorize_text(text):
    text = text.lower()

    if "def" in text or "import" in text:
        return "code"
    elif "todo" in text or "meeting" in text:
        return "note"
    else:
        return "other"

print(categorize_text("def my_function(): pass"))   # code
print(categorize_text("TODO: finish assignment"))   # note
print(categorize_text("I went to the market"))      # other
