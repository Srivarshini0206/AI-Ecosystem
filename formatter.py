"""
formatter.py
Formats prompt into structured output
"""

def format_prompt(data):

    prompt = "TASK:\n"
    prompt += f"You are an AI assistant. {data['task']}\n\n"

    prompt += f"STYLE: {data['style'].capitalize()}\n\n"

    prompt += "CONSTRAINTS:\n"

    if len(data["constraints"]) == 0:
        prompt += "- None\n"
    else:
        for c in data["constraints"]:
            prompt += f"- {c}\n"

    prompt += "\nEXAMPLES:\n"

    if len(data["examples"]) == 0:
        prompt += "None\n"
    else:
        for i in range(len(data["examples"])):
            prompt += f"{i+1}. {data['examples'][i]}\n"

    prompt += f"\nOUTPUT FORMAT: {data['output_format'].upper()}\n"

    return prompt