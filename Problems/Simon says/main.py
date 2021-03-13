def what_to_do(instructions):
    return f"I {instructions.replace('Simon says', '').strip()}" \
        if instructions.startswith('Simon says') or instructions.endswith('Simon says') \
        else "I won't do it!"
