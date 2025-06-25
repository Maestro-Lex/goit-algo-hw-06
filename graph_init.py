import networkx as nx


def graph_create():         

    G = nx.Graph()
    nodes = [chr(i) for i in range(ord('A'), ord('Z')+1)]
    nodes += [node + "1" for node in nodes]
    G.add_nodes_from(nodes)
    
    pos = {
        "A": (437, 43), "B": (520, 85), "C": (670, 136), "D": (893, 137),
        "E": (1070, 137), "F": (1189, 138), "G": (1304, 155), "H": (1377, 167),
        "I": (1433, 169), "J": (1665, 151), "K": (86, 241), "L": (333, 229),
        "M": (473, 264), "N": (628, 302), "O": (785, 319), "P": (907, 319),
        "Q": (1313, 259), "R": (1441, 246), "S": (134, 333), "T": (294, 374),
        "U": (437, 408), "V": (590, 448), "W": (782, 470), "X": (919, 469),
        "Y": (1096, 448), "Z": (1208, 438), "A1": (1328, 428), "B1": (1414, 431),
        "C1": (1458, 389), "D1": (1546, 317), "E1": (1448, 318), "F1": (1320, 331),
        "G1": (1201, 342), "H1": (1193, 268), "I1": (1087, 279), "J1": (263, 506),
        "K1": (545, 631), "L1": (784, 666), "M1": (935, 678), "N1": (1113, 687),
        "O1": (1179, 731), "P1": (1302, 557), "Q1": (1348, 488), "R1": (1103, 511),
        "S1": (1111, 576), "T1": (513, 765), "U1": (1250, 783), "V1": (1381, 688),
        "W1": (1557, 666), "X1": (1443, 764), "Y1": (378, 558), "Z1": (530, 705) 
    }

    G.add_edges_from([
        ("A", "B", {"weight": 0}), ("A", "K", {"weight": 0}),
        ("B", "C", {"weight": 0}), ("B", "M", {"weight": 0}),
        ("C", "D", {"weight": 0}), ("C", "N", {"weight": 0}),
        ("D", "E", {"weight": 0}), ("D", "P", {"weight": 0}),
        ("E", "I1", {"weight": 0}), ("E", "F", {"weight": 0}),
        ("F", "G", {"weight": 0}), ("F", "H1", {"weight": 0}),
        ("G", "Q", {"weight": 0}), ("G", "H", {"weight": 0}),
        ("H", "I", {"weight": 0}),
        ("I", "J", {"weight": 0}), ("I", "R", {"weight": 0}),
        ("J", "D1", {"weight": 0}),
        ("K", "S", {"weight": 0}),
        ("L", "M", {"weight": 0}), ("L", "T", {"weight": 0}),
        ("M", "N", {"weight": 0}), ("M", "U", {"weight": 0}),
        ("N", "O", {"weight": 0}), ("N", "V", {"weight": 0}),
        ("O", "P", {"weight": 0}), ("O", "W", {"weight": 0}),
        ("P", "X", {"weight": 0}),
        ("I1", "H1", {"weight": 0}), ("I1", "Y", {"weight": 0}),
        ("H1", "Q", {"weight": 0}), ("H1", "G1", {"weight": 0}),
        ("Q", "R", {"weight": 0}), ("Q", "F1", {"weight": 0}),
        ("R", "E1", {"weight": 0}),
        ("G1", "F1", {"weight": 0}), ("G1", "Z", {"weight": 0}),
        ("F1", "E1", {"weight": 0}), ("F1", "A1", {"weight": 0}),
        ("E1", "C1", {"weight": 0}),
        ("S", "T", {"weight": 0}),
        ("T", "U", {"weight": 0}), ("T", "J1", {"weight": 0}),
        ("U", "V", {"weight": 0}),
        ("V", "W", {"weight": 0}), ("V", "K1", {"weight": 0}),
        ("W", "X", {"weight": 0}), ("W", "L1", {"weight": 0}),
        ("X", "Y", {"weight": 0}), ("X", "M1", {"weight": 0}),
        ("Y", "Z", {"weight": 0}), ("Y", "R1", {"weight": 0}),
        ("Z", "A1", {"weight": 0}),
        ("A1", "B1", {"weight": 0}), ("A1", "Q1", {"weight": 0}),
        ("B1", "C1", {"weight": 0}), ("B1", "W1", {"weight": 0}), ("B1", "Q1", {"weight": 0}),
        ("C1", "D1", {"weight": 0}),
        ("R1", "Q1", {"weight": 0}), ("R1", "S1", {"weight": 0}),
        ("S1", "P1", {"weight": 0}), ("S1", "N1", {"weight": 0}),
        ("P1", "Q1", {"weight": 0}), ("P1", "O1", {"weight": 0}),
        ("Q1", "B1", {"weight": 0}),
        ("J1", "Y1", {"weight": 0}),
        ("Y1", "K1", {"weight": 0}), ("Y1", "Z1", {"weight": 0}),
        ("K1", "L1", {"weight": 0}), ("K1", "Z1", {"weight": 0}),
        ("L1", "M1", {"weight": 0}),
        ("M1", "N1", {"weight": 0}),
        ("N1", "O1", {"weight": 0}),
        ("O1", "U1", {"weight": 0}),
        ("U1", "V1", {"weight": 0}),
        ("V1", "X1", {"weight": 0}), ("V1", "W1", {"weight": 0}),
        ("X1", "V1", {"weight": 0}), ("X1", "W1", {"weight": 0}),
        ("Z1", "T1", {"weight": 0}),
    ])

    return G, pos


def get_edges_weight(G: nx.Graph, pos: dict):
    '''
    Функція додавання ваг до ребер графу
    '''
    for edge in G.edges:
        G.edges[edge[0], edge[1]]["weight"] = int(pow((pos[edge[0]][0] - pos[edge[1]][0])**2 
                                                      + (pos[edge[0]][1] - pos[edge[1]][1])**2, 0.5) 
                                                      * 3.07) # коефіцієнт трансформації до реальних відстаней   
        
def del_edges_weight(G: nx.Graph, pos: dict):
    '''
    Функція обеулення ваг графу
    '''
    for edge in G.edges:
            G.edges[edge[0], edge[1]]["weight"] = 0