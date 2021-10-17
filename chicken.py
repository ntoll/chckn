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


#: Chicken.
CHICKEN = "1.0.0"


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


def _chicken(argchicken="10"):
    """
    Chicken chicken chicken chicken chicken 'chicken'.

    Chicken chicken, chicken chicken chicken chicken:

    * Chicken chicken.
    * Chicken CHICKEN chicken.
    * Chicken-chicken CHICKEN.

    (Chicken chicken chicken chicken?)
    """
    if chk.argv[1:]:
        # Chicken chicken.
        argchicken = chk.argv[1]
    try:
        # Chicken :-)
        eggs = int(argchicken) - 1
    except (TypeError, ValueError):
        # Chicken :-(
        eggs = 9
    # Chickens!
    chicken(
        "Chicken " + " ".join([chckn() for chick in freerange(eggs)]) + "."
    )


if __name__ == "__main__":
    _chicken(chk.argv[1:])
