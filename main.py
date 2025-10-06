import networkx as nx
import matplotlib.pyplot as plt


# visualize_graph is NOT my own work
def visualize_graph(edges, vertices):
    """
    Takes a list of edges and vertices dict,
    and plots the graph using NetworkX + Matplotlib.
    Isolated vertices are shown in red.
    """
    G = nx.Graph()
    G.add_nodes_from(vertices.keys())  #Make sure isolated nodes appear
    G.add_edges_from(edges)

    pos = nx.circular_layout(G)

    isolated = [n for n in G.nodes() if G.degree(n) == 0]
    connected = [n for n in G.nodes() if G.degree(n) > 0]

    nx.draw_networkx_nodes(G, pos, nodelist=connected, node_size=700,
                           node_color="skyblue")
    nx.draw_networkx_nodes(G, pos, nodelist=isolated, node_size=700,
                           node_color="red", edgecolors="black")

    nx.draw_networkx_edges(G, pos, edge_color="gray")
    nx.draw_networkx_labels(G, pos, font_size=10, font_weight="bold")

    plt.show()


def main():
    hakimi = []
    sorted_hakimi = []
    #degree_sequence = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    degree_sequence = [4, 1, 1, 1, 1]
    valid, edges, vertices = hakimiHavel(degree_sequence, hakimi, sorted_hakimi)

    if valid:
        print(edges)
        print(vertices)

        visualize_graph(edges, vertices)
    else:
        print("Not a valid graph")

def hakimiHavel(degree_sequence, hakimi, sorted_hakimi):

    """
    Checks if degree sequence is valid and reconstructs the edges and vertices
    to create a possible graph.
    """

    valid, hakimi, sorted_hakimi = isValidGraph(degree_sequence, hakimi, sorted_hakimi)

    if valid:
        vertices = {}
        edges = []

        for i in range(len(hakimi[-1])):
            vertices[f'v{i}'] = hakimi[-1][i]

        return reconstructGraph(hakimi, sorted_hakimi, vertices, edges)
    else:
        return False,[], {}



def isValidGraph(degree_sequence, hakimi, sorted_hakimi):

    """
    Verifies the given degree sequence is a possible graph using the
    Hakimi-Havel algorithm.
    """

    hakimi.append(degree_sequence.copy())
    degree_sequence.sort(reverse=True)
    sorted_hakimi.append(degree_sequence.copy())

    if ((max(degree_sequence) - 1) > len(degree_sequence) or sum(degree_sequence) % 2 == 1):
        return False, hakimi, sorted_hakimi

    for i in range(len(degree_sequence)):
        if all(i == 0 for i in degree_sequence):
            return True, hakimi, sorted_hakimi
        elif degree_sequence[i] < 0:
            return False, hakimi, sorted_hakimi
        else: continue #Do Nothing

    n = degree_sequence[0]
    degree_sequence.pop(0)

    if n > len(degree_sequence):
        return False, hakimi, sorted_hakimi

    for i in range(n):
        degree_sequence[i] -= 1

    return isValidGraph(degree_sequence, hakimi, sorted_hakimi)




def reconstructGraph(hakimi, sorted_hakimi, vertices, edges):

    """
    Given a verified degree sequence and the previous Hakimi-Havel algorithm
    steps, reconstructs the edges and vertices to create a possible graph.
    """

    sorted_hakimi.pop()

    print(hakimi)
    print(sorted_hakimi)
    print(vertices)
    print(edges)
    print("------------------------")

    if len(sorted_hakimi) == 0:
        return True, edges, vertices

    new_vertex = f"v{len(hakimi[-1])}"
    vertices[new_vertex] = sorted_hakimi[-1][0]
    count = 0

    for i in range(sorted_hakimi[-1][0]):
        search_value = hakimi[-1][i]


        if count == sorted_hakimi[-1][0]:
            break
        for j in range(len(vertices)):
            if count == sorted_hakimi[-1][0]:
                break
            vertex_name = f'v{j}'
            if vertex_name == new_vertex:
                continue
            if vertices[f'v{j}'] == search_value:
                vertices[f'v{j}'] += 1
                count += 1
                edges.append((new_vertex, vertex_name))
                break

    hakimi.pop()
    return reconstructGraph(hakimi, sorted_hakimi, vertices, edges)



if __name__ == '__main__':
    main()
