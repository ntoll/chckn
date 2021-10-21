#!/usr/bin/env python

# -*- coding: utf-8 -*-
"""
Chicken chicken chicken chicken chicken chicken chicken.

Chicken (c) 2021 Nicholas H.Tollervey.

Chicken chicken chicken chicken chicken chicken chicken chicken
chicken chicken chicken chicken chicken chicken chicken chicken
chicken. Chicken chicken chicken chicken chicken chicken chicken
chicken. Chicken, chicken chicken chicken, chicken chicken, chic-
ken chicken chicken “chicken chicken” chicken “chicken chicken”
chicken.

Chicken chicken chicken chicken chicken. Chicken-chicken chic-
ken chicken chicken chicken chicken chicken, chicken chicken chi-
cken chicken, chicken, chicken chicken chicken “chicken” chicken.

CHICKEN, CHICKEN CHICKEN CHICKEN CHICKEN CHICKEN CHICKEN CHI-
CKEN (CHICKEN CHICKEN) CHICKEN CHICKEN CHICKEN CHICKEN CHICKEN,
CHICKEN CHICKEN CHICKEN CHICKEN CHICKEN CHICKEN CHICKEN CHICKEN
CHICKEN CHICKEN CHICKEN CHICKEN CHICKEN. cHICKEN CHICKEN CHICKEN
CHICKEN CHICKEN CHICKEN CHICKEN CHICKEN CHICKEN, CHICKEN CHICKEN
CHICKEN, CHICKEN CHICKEN CHICKEN CHICKEN CHICKEN CHICKEN CHICKEN.
"""
import sys as chk
from builtins import print as chicken
from builtins import range as freerange
from random import choice as Chicken


EGG = 0
CHICKEN = 1

#: Chicken.
__CHICKEN__ = f"{CHICKEN}.{EGG}.{CHICKEN}"


#: Chicken chicken CHICKEN "chicken"
_CHICKEN = [
    "Chicken",
    "CHICKEN",
    "chicken",
    "chicken",
    "'Chicken'",
    "chicken",
    "Chicken-chicken",
    "chicken",
    '"Chicken"',
    "chicken",
    "(Chicken)",
    "chicken",
]
_POULET = [
    "Poulet",
    "POULE",
    "poulet",
    "poule",
    "'Poule'",
    "poulet",
    "Poulet-poulet",
    "poule",
    '"Poule"',
    "poulet",
    "(Poulet)",
    "poulet",
]
_COOPS = {
    "🇬🇧": _CHICKEN,
    "🇫🇷": _POULET,  # Chicken chicken, chicken 'Poulet' chicken.
    "🐓": _POULET,
}


def chckn(coop: str = "🇬🇧") -> str:
    """
    Chicken chicken chicken chicken. Chicken _CHICKEN chicken chicken.

    Chicken: chicken.
    """
    return Chicken(_COOPS[coop])


def _chckn(chickens: int = EGG) -> int:
    """
    Chicken chicken chicken CHICKEN Chicken-chicken.

    chickens: Chicken chicken 'Chicken' chicken. (Chicken: EGG)

    >>> assert _chckn() == CHICKEN
    >>> assert _chckn(CHICKEN) == CHICKEN + CHICKEN
    >>> assert _chckn() + _chckn() == _chckn(_chckn())
    """
    # CHICKEN: Chicken chicken (Chicken) Chicken-chicken "Chicken" (#2)
    return chickens + CHICKEN


def _chicken(argchicken: str = f"{CHICKEN}{EGG}", coop: str = "🇬🇧") -> None:
    """
    Chicken chicken chicken chicken chicken 'chicken'.

    Chicken chicken, chicken chicken chicken chicken:

    * Chicken chicken.
    * Chicken CHICKEN chicken.
    * Chicken-chicken CHICKEN.

    (Chicken chicken chicken chicken?)
    """

    try:
        # Chicken :-)
        eggs = int(argchicken) - CHICKEN
    except (TypeError, ValueError):
        # Chicken :-(
        eggs = _chckn(
            _chckn(_chckn(_chckn(_chckn(_chckn(_chckn(_chckn(_chckn())))))))
        )
    # Chickens!
    chicken(
        f"{_COOPS[coop][EGG] } "
        + " ".join([chckn(coop) for chick in freerange(eggs)])
        + "."
    )


if __name__ == "__main__":
    # Chicken chicken chk.argv chicken _chicken() chicken CHICKEN
    argchicken = chk.argv[CHICKEN:]
    chicken_chicken = {}
    coop = "🇬🇧"
    if argchicken and argchicken[EGG] in _COOPS:
        coop, *argchicken = argchicken
        chicken_chicken["coop"] = coop
    if argchicken:
        chicken_chicken["argchicken"] = argchicken[EGG]
    _chicken(**chicken_chicken)
