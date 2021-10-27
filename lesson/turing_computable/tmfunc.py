class Cnst:
    def __init__(self, c):
        self.c = c

    def __call__(self, *x):
        return self.c


class Branching:
    def __init__(self, f0, f1, g, c):
        self.f0 = f0
        self.f1 = f1
        self.g = g
        self.c = c

    def __call__(self, *x):
        # h(x) = f0(x) if g(x) = c else f1(x)
        if self.g(*x) == self.c:
            return self.f0(*x)
        else:
            return self.f1(*x)


class Recursion:
    def __init__(self, g, f):
        self.g = g
        self.f = f

    def __call__(self, x, *y):
        # h(0, y) = g(y)
        ret = self.g(*y)

        # h(x+1, y) = h(f(x, y), x, y)
        for i in range(1, x+1):
            ret = self.f(ret, i-1, *y)

        return ret


def identity(x):
    return x


def add(x, y):
    return x + y


def sub(x, y):
    return max(x - y, 0)


def suc(x):
    return x + 1


def mul(x, y):
    func = Recursion(
        Cnst(0),
        lambda hi, i, y: add(hi, y)
    )
    return func(x, y)


def fact(x):
    func = Recursion(
        Cnst(1),
        lambda hi, i, y: mul(hi, suc(i))
    )
    return func(x, x)


def rem(x, y):
    func = Branching(
        Cnst(0),
        Recursion(
            Cnst(0),
            lambda hi, i, y: Branching(
                Cnst(0),
                lambda hi, y: suc(hi),
                lambda hi, y: sub(y-1, hi),
                0
            )(hi, y)
        ),
        lambda i, y: y,
        0)
    return func(x, y)


def quo(x, y):
    func = Branching(
        Cnst(0),
        lambda x, y: Recursion(
            Cnst(0),
            lambda hi, i, x, y: Branching(
                lambda hi, i, y: hi,
                lambda hi, i, y: suc(hi),
                lambda hi, i, y: sub(i, hi*y),
                0,
            )(hi, x, y)
        )(x, x, y),
        lambda x, y: y,
        0,
    )
    return func(x, y)


def prime(x):
    func = Branching(
        Cnst(0),
        Branching(
            Cnst(0),
            lambda x: Recursion(
                Cnst(1),
                Branching(
                    Cnst(0),
                    Branching(
                        Cnst(1),
                        Branching(
                            Cnst(1),
                            Branching(
                                Cnst(0),
                                Cnst(1),
                                lambda x1, x2, y: rem(y, x2),
                                0
                            ),
                            lambda x1, x2, y: x2,
                            1
                        ),
                        lambda x1, x2, y: x2,
                        0
                    ),
                    lambda x1, x2, y: x1,
                    0
                )
            )(x-1, x),
            identity,
            0
        ),
        identity,
        1
    )

    return func(x)
