def expand_pos_tag(pos_tag):
    pos_tag_mapping = {
        "ADJ": "adjective",
        "ADP": "adposition",
        "ADV": "adverb",
        "AUX": "auxiliary verb",
        "CONJ": "conjunction",
        "CCONJ": "coordinating conjunction",
        "DET": "determiner",
        "INTJ": "interjection",
        "NOUN": "noun",
        "NUM": "numeral",
        "PART": "particle",
        "PRON": "pronoun",
        "PROPN": "proper noun",
        "PUNCT": "punctuation",
        "SCONJ": "subordinating conjunction",
        "SYM": "symbol",
        "VERB": "verb",
        "X": "other",
        "SPACE": "space"
    }

    return pos_tag_mapping.get(pos_tag, "unknown")
