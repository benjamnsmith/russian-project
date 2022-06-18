cases_m = ["Nominative", "Accusative (animate)", "Accusative (inanimate)", "Genitive", "Prepositional", "Dative", "Instrumental"]

cases_f = ["Nominative", "Accusative", "Genitive", "Prepositional", "Dative", "Instrumental"]


# CASE ENDINGS - ADJECTIVES
adj_endings_m = {
    "nom" : "ый",
    "acc_a": "ый",
    "acc_i": "ого",
    "gen": "ого",
    "prep": "ом",
    "dat": "ому",
    "ins": "ым"
}

adj_endings_f = {
    "Nominative" : "ая",
    "Accusative": "ую",
    "everything": "ой"
}

adj_endings_n = {}

# CASE ENDINGS - NOUNS
noun_endings_m = {}

noun_endings_f = {}

noun_endings_n = {}


# HELPER FUNCTIONS
def sanity_check(word):
    sane = False
    if word.endswith("ый"):
        sane = not sane
        gen = 'm'
    elif word.endswith("ий"):
        sane = not sane
        gen = 'm'
    elif word.endswith("ой"):
        sane = not sane
        gen = 'm'
    elif word.endswith("ая"):
        sane = not sane
        gen = 'f'
    elif word.endswith("ое"):
        sane = not sane
        gen = 'n'
    elif word.endswith("ые"):
        sane = not sane
        gen = 'pl'
    elif word.endswith("ие"):
        sane = not sane
        gen = 'pl'
    return sane, gen

def spelling_rule(forms):
    not_allowed = {
        'жы':'жи',
        'шы':'ши',
        'щы':'щи',
        'чы':'чи',
        'кы': 'ки',
        'гы': 'ги',
        'хы': 'хи',
        'жо': 'же',
        'шо':'ше',
        'що':'ще',
        'чо':'че'
    }
    fixed = []
    for entry in forms:
        for offender in not_allowed:
            if offender in entry:
                entry = entry.replace(offender, not_allowed[offender])
        fixed.append(entry)
    return fixed

def pretty_print(vals):
    global cases_m
    global cases_f

    if len(vals) == len(cases_m):
        print("==============================")
        for i in range(len(vals)): 
            print(cases_m[i].center(23), end='')
            print(" | ", end='')
            print(vals[i])
            

    elif len(vals) == len(cases_f):
        print("==============================")
        for i in range(len(vals)): 
            print(cases_f[i].center(15), end='')
            print(" | ", end='')
            print(vals[i])
            

    else:
        print("uneven lists")
        return



# DRIVER CODE
def decline_adj(word):
    global adj_endings_m
    global adj_endings_f
    global cases_m
    global cases_f
    cont, gen = sanity_check(word)
    if not cont:
        print("Please enter a word in nominative case")
        return
    
    forms = []
    stem = word[:-2]
    if gen == 'm':
        print("This is a masculine adjective")
        for entry in adj_endings_m:
            decl = stem + adj_endings_m[entry]
            forms.append(decl)
    if gen == 'f':
        print("This is a feminine adjective")
        for entry in cases_f:
            if entry in adj_endings_f:
                decl = stem + adj_endings_f[entry]
            else:
                decl = stem + adj_endings_f['everything']
            forms.append(decl)
    forms = spelling_rule(forms)
    pretty_print(forms)

decline_adj("хороший")
print()
decline_adj('хорошая')
print()
decline_adj('большой')
print()