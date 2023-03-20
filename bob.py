def response(phrase):
    if phrase.strip().endswith('?') and phrase.isupper():
        return "Calm down, I know what I'm doing!"
    elif phrase.strip().endswith('?'):
        return "Sure."
    elif phrase.isupper():
        return "Whoa, chill out!"
    elif not phrase.strip():
        return "Fine. Be that way!"
    else:
        return "Whatever."