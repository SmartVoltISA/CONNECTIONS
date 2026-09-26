"""Exploratory triangle-structure sweep.

Purpose:
Compare networks containing different amounts/arrangements of triangles
under the same synchronous binary local-rule family.

This experiment is deliberately exploratory: degree and other graph
properties are not automatically matched. Controlled comparisons must
record all graph descriptors before interpretation.

Requires: networkx, numpy
"""

import networkx as nx
import numpy as np


def rule_step(state, g, rule):
    out = 0
    for i in g:
        s = (state >> i) & 1
        k = sum((state >> j) & 1 for j in g.neighbors(i))
        idx = s * (max(dict(g.degree()).values()) + 1) + k
        out |= ((rule >> idx) & 1) << i
    return out


def analyse(g, rule, steps=100):
    n = len(g)
    records = []
    for start in range(1 << n):
        seen = {}
        state = start
        for t in range(steps):
            if state in seen:
                records.append((seen[state], t - seen[state]))
                break
            seen[state] = t
            state = rule_step(state, g, rule)
    return records


def families():
    return {
        "triangle": nx.complete_graph(3),
        "two_triangles": nx.disjoint_union(nx.complete_graph(3), nx.complete_graph(3)),
        "triangle_with_tail": nx.path_graph(3),
        "clique4": nx.complete_graph(4),
        "cycle6": nx.cycle_graph(6),
    }


if __name__ == "__main__":
    # Use a modest rule sweep first; expand only after graph controls are fixed.
    for name, g in families().items():
        triangles = sum(nx.triangles(g).values()) // 3
        print(name, {
            "nodes": len(g),
            "edges": g.number_of_edges(),
            "triangles": triangles,
            "degree_sequence": sorted(d for _, d in g.degree()),
        })
