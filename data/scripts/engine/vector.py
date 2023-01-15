from __future__ import annotations

from math import sqrt


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    # Returns the length of the vector
    def magnitude(self) -> float:
        return sqrt(self.x**2 + self.y**2)

    # Returns a normalized vector (vector with a length of 1)
    def normalized(self) -> Vector:
        nx = self.x / self.magnitude()
        ny = self.y / self.magnitude()
        return Vector(nx, ny)

    def set(self, new_x: float, new_y: float) -> None:
        self.x = new_x
        self.y = new_y

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
