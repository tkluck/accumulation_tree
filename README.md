`accumulation_tree`
===================

A red/black tree which also stores partial aggregations at each node, making
getting aggregations of key range slices an O(log(N)) operation.

Synopsis
--------
```python
>>> from accumulation_tree import AccumulationTree
>>> t = AccumulationTree(lambda x: x)
>>> N = 10000
>>> for x in range(N):
...    t.insert(x,x)
>>> t.get_accumulation(0, 2)
1
>>> t.get_accumulation(0, 5)
10
>>> all(t.get_accumulation(0, x) == x*(x-1)/2 for x in range(N))
True
```
