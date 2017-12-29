accumulation_tree
=================

A red/black tree which also stores partial aggregations at each node, making
getting aggregations of key range slices an O(log(N)) operation.
