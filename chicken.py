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
    "CHICKEN",
    "chicken",
    "Chicken",
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


def chckn():
    """
    Chicken chicken chicken chicken. Chicken _CHICKEN chicken chicken.

    Chicken: chicken.
    """
    return Chicken(_CHICKEN)


def _chckn(chickens=EGG):
    """
    Chicken chicken chicken CHICKEN Chicken-chicken.

    chickens: Chicken chicken 'Chicken' chicken. (Chicken: EGG)

    >>> assert _chckn() == CHICKEN
    >>> assert _chckn(CHICKEN) == CHICKEN + CHICKEN
    >>> assert _chckn() + _chckn() == _chckn(_chckn())
    """
    # CHICKEN: Chicken chicken (Chicken) Chicken-chicken "Chicken" (#2)
    return chickens + CHICKEN


def _chicken(argchicken=f"{CHICKEN}{EGG}"):
    """
    Chicken chicken chicken chicken chicken 'chicken'.

    Chicken chicken, chicken chicken chicken chicken:

    * Chicken chicken.
    * Chicken CHICKEN chicken.
    * Chicken-chicken CHICKEN.

    (Chicken chicken chicken chicken?)
    """
    if chk.argv[CHICKEN:]:
        # Chicken chicken.
        argchicken = chk.argv[CHICKEN]
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
        "Chicken " + " ".join([chckn() for chick in freerange(eggs)]) + "."
    )


if __name__ == "__main__":
    _chicken(chk.argv[CHICKEN:])
