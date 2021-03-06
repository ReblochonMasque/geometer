import numpy as np
from geometer import *


def test_is_collinear():
    p1 = Point(1, 0)
    p2 = Point(2, 0)
    p3 = Point(3, 0)
    l = Line(p1, p2)
    assert l.contains(p3)
    assert is_collinear(p1, p2, p3)


def test_dist():
    p = Point(0, 0)
    q = Point(1, 0)

    assert np.isclose(dist(p, q), 1)

    p1 = Point(1j, 0, 0, 2j)
    p2 = Point(0, 2j, 0, 0)

    assert np.isclose(dist(p1, p2), 3)

    p1 = Point(1, 0, 0)
    p2 = Point([1, 0, 0, 0])

    assert dist(p1, p2) == dist(p2, p1) == np.inf

    p1 = Point(0, 0, 0)
    p2 = Point(1, 0, 0)

    assert np.isclose(dist(p1, p2), 1)

    e = Plane(1, 0, 0, 0)
    assert np.isclose(dist(e, p2), 1)

    l = Line(p2, Point(1, 1, 0))
    assert np.isclose(dist(l, e), 1)
    assert np.isclose(dist(l, p1), 1)


def test_angle():
    a = Point(0, 0)
    b = Point(1, 1)
    c = Point(1, 0)

    assert np.isclose(angle(a, b, c), np.pi/4)

    e1 = Plane(1, 0, 0, 0)
    e2 = Plane(0, 0, 1, 0)

    assert np.isclose(abs(angle(e1, e2)), np.pi/2)

    p1 = Point(0, 0, 0)
    p2 = Point(0, 1, 0)
    p3 = Point(1, 0, 0)
    l = Line(p1, p2)
    m = Line(p1, p3)

    assert np.isclose(abs(angle(l, m)), np.pi/2)
    assert np.isclose(abs(angle(p1, p2, p3)), np.pi / 2)


def test_angle_bisectors():
    a = Point(0, 0)
    b = Point(1, 1)
    c = Point(1, 0)
    l = Line(a, b)
    m = Line(a, c)
    q, r = angle_bisectors(l, m)
    assert is_perpendicular(q, r)
    assert np.isclose(angle(l, q), angle(q, m))

    p1 = Point(0, 0, 0)
    p2 = Point(0, 1, 0)
    p3 = Point(1, 0, 0)
    l = Line(p1, p2)
    m = Line(p1, p3)
    q, r = angle_bisectors(l, m)
    assert is_perpendicular(q, r)
    assert np.isclose(angle(l, q), angle(q, m))


def test_is_cocircular():
    p = Point(0,1)
    t = rotation(np.pi/3)

    assert is_cocircular(p, t*p, t*t*p, t*t*t*p)


def test_is_coplanar():
    p1 = Point(1, 1, 0)
    p2 = Point(2, 1, 0)
    p3 = Point(3, 4, 0)
    p4 = Point(0, 2, 0)

    assert is_coplanar(p1, p2, p3, p4)


def test_is_perpendicular():
    l = Line(0, 1, 0)
    m = Line(1, 0, 0)
    assert is_perpendicular(l, m)

    p1 = Point(0, 0, 0)
    p2 = Point(0, 1, 0)
    p3 = Point(1, 0, 0)
    l = Line(p1, p2)
    m = Line(p1, p3)
    assert is_perpendicular(l, m)


def test_pappos():
    a1 = Point(0, 1)
    b1 = Point(1, 2)
    c1 = Point(2, 3)

    a2 = Point(0, 0)
    b2 = Point(1, 0)
    c2 = Point(2, 0)

    p = a1.join(b2).meet(b1.join(a2))
    q = b1.join(c2).meet(c1.join(b2))
    r = c1.join(a2).meet(a1.join(c2))

    assert is_collinear(p, q, r)


def test_cp1():
    p = Point(1+0j)
    q = Point(0+1j)
    m = Transformation([[np.e**(np.pi/2*1j), 0], [0, 1]])
    assert m*p == q
    c = crossratio(p, q, m*q, m*m*q)
    assert np.isclose(np.real(c), c)


def test_harmonic_set():
    a = Point(0, 0)
    b = Point(1, 1)
    c = Point(3, 3)
    d = harmonic_set(a, b, c)
    assert np.isclose(crossratio(a, b, c, d), -1)

    a = Point(0, 0, 0)
    b = Point(1, 1, 0)
    c = Point(3, 3, 0)
    d = harmonic_set(a, b, c)
    assert np.isclose(crossratio(a, b, c, d), -1)
