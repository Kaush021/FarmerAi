# app/name_match/recommend.py
from difflib import get_close_matches

COMMON_NAMES = ["Ramesh Kumar", "Ramesh Kumaar", "Ram Kumar", "Ramesh Kumer"]

def recommend_name(spoken_name):
    return get_close_matches(spoken_name, COMMON_NAMES, n=3, cutoff=0.6)
