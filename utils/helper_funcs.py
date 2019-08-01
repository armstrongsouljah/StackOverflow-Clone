import string
import random
from django.utils.text import slugify

def create_code(size, chars=string.digits+string.ascii_lowercase):
    return "".join(random.choice(chars) for _ in range(size))

def create_unique_slug(field_name):
    if field_name:
        return f"{slugify(field_name)}-{create_code(size=5)}"
    