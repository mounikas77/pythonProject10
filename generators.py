def mygen():
    yield 1
    yield 2
    yield 3
g=mygen()
print(type(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
