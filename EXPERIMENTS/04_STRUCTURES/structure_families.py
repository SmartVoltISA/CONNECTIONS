"""Common structure family catalogue for CONNECTIONS.

This is a controlled-experiment generator, not a claim that the structures
are equivalent. The first stage records topology; later stages can run the
same local dynamics on each family.

Requires: networkx
"""

import networkx as nx


def structures(n=8):
    grid = nx.grid_2d_graph(2, 4)
    grid = nx.convert_node_labels_to_integers(grid)

    star = nx.star_graph(n - 1)
    ring = nx.cycle_graph(n)
    path = nx.path_graph(n)
    clique = nx.complete_graph(n)

    # Two dense modules joined by one bridge.
    left = nx.complete_graph(n // 2)
    right = nx.complete_graph(n // 2)
    modular = nx.disjoint_union(left, right)
    modular.add_edge(0, n // 2)

    return {
        "path": path,
        "ring": ring,
        "star": star,
        "grid_2x4": grid,
        "clique": clique,
        "two_modules_bridge": modular,
    }


if __name__ == "__main__":
    for name, g in structures().items():
        print(name, {
            "nodes": g.number_of_nodes(),
            "edges": g.number_of_edges(),
            "degree_sequence": sorted(d for _, d in g.degree()),
            "triangles": sum(nx.triangles(g).values()) // 3,
            "connected": nx.is_connected(g),
            "diameter": nx.diameter(g) if nx.is_connected(g) else None,
        })
