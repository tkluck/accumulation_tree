Test accumulations by inserting in-order (forcing rebalancing) and comparing
with the exact result for arithmetic series:

    >>> from accumulation_tree import AccumulationTree
    >>> t = AccumulationTree(lambda x: x)
    >>> N = 10000
    >>> for x in range(N):
    ...    t.insert(x,x)
    >>> all(t.get_accumulation(0, x) == x*(x-1)/2 for x in range(N))
    True

And also after removing half of them, leaving only the even ones:

    >>> for x in range(N >> 1):
    ...     t.remove(x*2+1)
    >>> all(t.get_accumulation(0, 2*x) == x*(x-1) for x in range(N >> 1))
    True

Let's also overwrite a value and see that this correctly propagates:

    >>> t.insert(0, 1)
    >>> all(t.get_accumulation(0, 2*x) == 1 + x*(x-1) for x in range(1, N >> 1))
    True

And the same, but through the dictionary interface:

    >>> t[0] = 2
    >>> all(t.get_accumulation(0, 2*x) == 2 + x*(x-1) for x in range(1, N >> 1))
    True
