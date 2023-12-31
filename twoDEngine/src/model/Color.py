from dataclasses import dataclass


class Color:
    def __init__(self, R, G, B):
        if R > 255 or G > 255 or B > 255:
            raise ValueError("R / G / B values must be 0 - 255")
        self.R = int(R)
        self.G = int(G)
        self.B = int(B)

    def __eq__(self, other):
        if isinstance(other, Color):
            return self.R == other.R and self.G == other.G and self.B == other.B
