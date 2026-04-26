from collections import deque


def palindrom_check(text: str):
    clean_text = text.lower().replace(" ", "")
    d = deque()

    for char in clean_text:
        d.append(char)
    
    while len(d) > 1:
        if d.pop() != d.popleft():
            return False

    return True

    
print(palindrom_check("А роза упала на лапу Азора"))
print(palindrom_check("Абабагаламага"))