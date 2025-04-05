def remove_substring(main_string, sub_string):
    return main_string.replace(sub_string, "")

# Example usage
main_string = "abcdef"
sub_string = "cd"

final_string = remove_substring(main_string, sub_string)
print(final_string)  # Output: "abef"

