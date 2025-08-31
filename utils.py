import random
import string


def generate_short_code(length=6):
    """Generate a random short code of given length"""
    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for _ in range(length))


def is_valid_url(url):
    """Check if URL starts with http:// or https://"""
    return url.startswith("http://") or url.startswith("https://")
