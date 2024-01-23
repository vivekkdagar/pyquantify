def expand_pos_tag(pos_tag):
    pos_prefix = pos_tag[:2]

    pos_mapping = {
        'CC': 'Coordinating conjunction',
        'CD': 'Cardinal number',
        'DT': 'Determiner',
        'FW': 'Foreign word',
        'IN': 'Preposition or subordinating conjunction',
        'JJ': 'Adjective',
        'LS': 'List item marker',
        'MD': 'Modal',
        'NN': 'Noun',
        'PD': 'Predeterminer',
        'PR': 'Pronoun',
        'RB': 'Adverb',
        'RP': 'Particle',
        'SY': 'Symbol',
        'TO': 'to',
        'UH': 'Interjection',
        'VB': 'Verb',
        'WD': 'Wh-determiner',
        'WP': 'Wh-pronoun',
        'WR': 'Wh-adverb',
        'Unknown': 'Unknown POS Tag',
    }

    return pos_mapping.get(pos_prefix, pos_mapping['Unknown'])

