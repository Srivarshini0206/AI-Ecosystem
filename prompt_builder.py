"""
prompt_builder.py
Collects user input for building prompts
"""

def get_user_input():
    task = input("Describe the task: ").strip()

    while task == "":
        print("Task cannot be empty.")
        task = input("Describe the task: ").strip()

    style = input("Style (friendly/formal/poetic/instructive): ").strip()

    while style == "":
        print("Style cannot be empty.")
        style = input("Style (friendly/formal/poetic/instructive): ").strip()

    constraints = []
    print("Enter constraints (blank line to finish):")

    while True:
        c = input("- ").strip()
        if c == "":
            break
        constraints.append(c)

    examples = []
    print("Enter examples (blank line to finish):")

    while True:
        e = input(f"Example {len(examples)+1}: ").strip()
        if e == "":
            break
        examples.append(e)

    output_format = input("Desired output format: ").strip()

    while output_format == "":
        print("Output format cannot be empty.")
        output_format = input("Desired output format: ").strip()

    return {
        "task": task,
        "style": style,
        "constraints": constraints,
        "examples": examples,
        "output_format": output_format
    }