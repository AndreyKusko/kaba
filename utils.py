import re


def slugify(text):
    pattern = r'[^\w+\-]'
    return re.sub(pattern, '-', text.lower())
