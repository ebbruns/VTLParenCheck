# ParenCheck v 0.2
# Written by Evan Bruns
# Intended to help users find bugs in .vtl code without an IDE
# Currently works for parenthesis, square brackets, and curly brackets.
# Does not check for improper nesting (i.e. {(}) is ignored)
# Will falsely flag the opening and closing lines if a symbol is opened on one line and closes on a different line.


import fileinput


# Runs on each line to check for matching symbols
def matches(line):
    paren_count = 0
    curly_count = 0
    square_count = 0
    for char in line:
        if paren_count < 0 or curly_count < 0 or square_count < 0:
            return False
        if char == "(":
            paren_count += 1
        elif char == ")":
            paren_count -= 1
        elif char == "{":
            curly_count += 1
        elif char == "}":
            curly_count -= 1
        elif char == "[":
            square_count += 1
        elif char == "]":
            square_count -= 1

    return paren_count == 0 and curly_count == 0 and square_count == 0 and line[-2] != ";"


# The function that starts the ball rolling, tracks index, and presents output to the user.
# Prints out an array containing the line numbers where problems are detected
def main():
    print("Welcome to ParenCheck for VTL")
    print("Please copy in the text of your VTL file")
    print("When you are finished, type **done** and press enter")
    i = 1
    problem_lines = []
    for line in fileinput.input():
        if line.lower() == "**done**\n":
            fileinput.close()
            break
        else:
            if not matches(line):
                problem_lines.append(i)
            i += 1

    print("We have detected issues on the following lines:")
    print(problem_lines)

main()


