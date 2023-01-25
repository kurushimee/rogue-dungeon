from __future__ import annotations

from math import sqrt


class Vector:
    def __init__(self, x: float = 0.0, y: float = 0.0) -> None:
        self.x = x
        self.y = y

    # Returns the length of the vector
    def magnitude(self) -> float:
        return sqrt(self.x**2 + self.y**2)

    # Returns a normalized vector (vector with a length of 1)
    def normalized(self) -> Vector:
        magnitude = self.magnitude()
        if magnitude != 0.0:
            nx = self.x / magnitude
            ny = self.y / magnitude
            return Vector(nx, ny)
        return self

    # Normalizes the vector
    def normalize(self) -> None:
        self.set(self.normalized())

    # Sets new values for the vector
    def set(self, new: Vector) -> None:
        self.x = new.x
        self.y = new.y

    # Returns a distance between two vectors
    @staticmethod
    def distance(a: Vector, b: Vector) -> float:
        return (a - b).magnitude()

    def __sub__(self, other: Vector) -> Vector:
        x = self.x - other.x
        y = self.y - other.y
        return Vector(x, y)

    def __mul__(self, other: Vector) -> Vector:
        x = self.x * other.x
        y = self.y * other.y
        return Vector(x, y)

    def __div__(self, other: Vector) -> Vector:
        x = self.x / other.x
        y = self.y / other.y
        return Vector(x, y)

    def __add__(self, other: Vector) -> Vector:
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __eq__(self, other: Vector) -> bool:
        x = self.x == other.x
        y = self.y == other.y
        return x and y
