from difflib import get_close_matches

COMMON_NAMES = [
    "Ramesh Kumar",
    "Ram Kumar",
    "Suresh Kumar",
    "Mahesh Singh"
]

def recommend_name(spoken_name):
    return get_close_matches(spoken_name, COMMON_NAMES, n=3, cutoff=0.6)