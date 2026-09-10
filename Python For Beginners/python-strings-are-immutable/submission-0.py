def remove_fourth_character(word: str) -> str:
    before_second = word[:3] # "I"
    after_second = word[4:]  # "will never change."

    return before_second + after_second


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
