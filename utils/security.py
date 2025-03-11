# jarvis/utils/security.py
# Security functions
import hashlib

def hash_string(text):
    return hashlib.sha256(text.encode()).hexdigest()
