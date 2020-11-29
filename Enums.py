""" Modul obshaujici definice vyctovych typu."""


def enum(**enums):
    """ Funkce umoznujici vytvoreni vyctoveho typu.

    Args:
        - enums - Volitelny parametr obsahujici pozadovany vycet.

    Returns:
        Nove vytvoreny vyctovy typ.
    """

    return type('Enum', (), enums)


""" Vyctovy typ definujici stavy automatu."""
States = enum(MENU=1, ACTION=2, PROCCESS=3)

""" Vyctovy typ definujici jednotlive akce aplikace."""
Actions = enum(ENCODE=1, DECODE=2, END=3, UNKNOWN=4)
