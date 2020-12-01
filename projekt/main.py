"""Calculate triangle."""
import math


def lengthofside(jednaX, dveX, jednaY, dveY):
    """Calculate length of a side."""
    sa = jednaX - dveX
    sb = jednaY - dveY
    vysledek = math.sqrt(sa * sa + sb * sb)
    return vysledek
