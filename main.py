import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.widgets import Button
from graph_init import *


def main ():  

    # Створюємо поверхню для візуалізації із доданням карти на фон    
    bg = plt.imread('src/map.png')
    height, width = bg.shape[:2]
    fig, ax = plt.subplots(figsize=(width/100, height/100), dpi=80)
    ax.imshow(bg, extent=[0, width, height, 0], alpha=0.65)
    ax.set_title("Граф маршрутів Ленінського району м. Вінниця")
    plt.axis("off")

    # Візуалізуємо на створеній поверхні граф
    G, pos = graph_create()
    nx.draw(
        G,
        pos,
        with_labels = True,
        node_size = 400,
        edge_color = "orange",
        width = 2
    )

    # Додаємо ваги до ребер графу
    get_edges_weight(G, pos)
    edge_weights = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(
        G,
        pos,
        edge_labels = edge_weights,
        ax = ax,
        font_color = 'black'
    )
    
    # обрані вершини
    vertexes = [] 
    highlighted_nodes = {}

    # текстові поля для виводу інформації
    info = ax.text(10, height+50, "Оберіть мінімум 1 вершину(за замовченням обрана 'A')\n(2 для розрахунку маршруту).", fontsize=12, color="black",
                bbox=dict(facecolor='white', alpha=0.7), visible=True)
    graph_info = f"Загальна кількість вершин графу - {G.number_of_nodes()}\n"
    graph_info += f"Загальна кількість ребер графу - {G.number_of_edges()}\n"
    graph_info += f"Середня ступінь вершин графу - {sum(dict(G.degree()).values()) / G.number_of_nodes():.2f}"
    graph_info = ax.text(10, -50, graph_info, fontsize=12, color="black",
                bbox=dict(facecolor='white', alpha=0.7), visible=True)    
    warning = ax.text(width / 2 - 150, 30, "", fontsize=12, color="red",
                bbox=dict(facecolor='white', alpha=0.7), visible=True)
    message = ax.text(width / 2 - 140, 50, "", fontsize=12, color="green",
                bbox=dict(facecolor='white', alpha=0.7), visible=True)    
    
    
    def on_click(event):
        """
        Функція обрання вершин для реалізації алгоритмів
        """
        if event.xdata is None or event.ydata is None:
            return

        x, y = event.xdata, event.ydata

        message.set_text("")
        closest = None
        for node, (node_x, node_y) in pos.items():            
            dist = ((x - node_x)**2 + (y - node_y)**2)**0.5
            if dist < 20: 
                closest = node

                # Керування обранням вершин
                if closest not in vertexes:
                    # Не даємо обрати більше двох вершин
                    if len(vertexes) > 1:
                        warning.set_text("Не можна обрати більше двох вершин!")
                        warning.set_visible(True)
                        continue
                    vertexes.append(closest)                    
                    circle = Circle((node_x, node_y), radius=22, edgecolor='red', facecolor='none', linewidth=4)
                    highlighted_nodes[node] = circle
                    ax.add_patch(circle)
                    info.set_text(f"Обрані вершини: {", ".join(vertexes)}")
                else:
                    warning.set_visible(False)
                    vertexes.remove(closest)
                    highlighted_nodes[node].remove()
                    del highlighted_nodes[node]
                    info.set_text(f"Обрані вершини: {", ".join(vertexes)}")

        fig.canvas.draw()    

    cid = fig.canvas.mpl_connect('button_press_event', on_click)

    # Створення кнопки "DFS та BFS" ті її функціоналу
    button_ax = plt.axes([0.5, 0.1, 0.06, 0.04])
    button_1 = Button(button_ax, 'DFS та BFS')
    
    def dfs_bfs(event):

        if vertexes:
            source = vertexes[0]
        else:
            source = "A"

        # Обхід в глибину
        dfs_tree = nx.dfs_tree(G, source = source)

        # Обхід в ширину
        bfs_tree = nx.bfs_tree(G, source = source)                
                
        print()
        print(f"Результати обходу дерева у глибину з вершини {source}:")
        print(list(dfs_tree.edges()))
        print()
        print(f"Довжина (кількість ребер) для DFS: {len(list(dfs_tree.edges()))}")
        print("-----------------------")
        print(f"Результати обходу дерева у ширину з вершини {source}:")
        print(list(bfs_tree.edges()))
        print()
        print(f"Довжина (кількість ребер) для BFS: {len(list(dfs_tree.edges()))}")
        print("-----------------------")
        message.set_text(f"Результат обходу графа у глибину та ширину\nдля вершини {source} виведено у консоль!")
        plt.show()
        
    button_1.on_clicked(dfs_bfs)

    # Створення кнопки "Маршрут за Дейкстра" ті її функціоналу
    button_ax = plt.axes([0.6, 0.1, 0.12, 0.04])
    button_2 = Button(button_ax, 'Маршрут за Дейкстра')

    def dijkstra(event):
        '''
        Робота із алгоритмом Дейкстри
        '''
        if vertexes:
            source = vertexes[0]
        else:
            source = "A"                

        shortest_paths = nx.single_source_dijkstra_path(G, source = source)
        shortest_path_lengths = nx.single_source_dijkstra_path_length(G, source = source)
        
        print()
        print(f"Найкоротші шляхи з вершини {source}:")
        print(shortest_paths)
        print("-----------------------")
        print("та їх довжини:")
        print(shortest_path_lengths)
        print()

        # Розрахунок та візуалізація маршруту між двома вершинами
        if len(vertexes) == 2:                
                print(f"Маршрут від {vertexes[0]} до {vertexes[1]} проходить {" -> ".join(shortest_paths.get(vertexes[1]))} та становить {shortest_path_lengths.get(vertexes[1])} м.")
                print("-----------------------")

                nodes = list(highlighted_nodes.keys())
                for node in nodes:
                    highlighted_nodes[node].remove()
                    del highlighted_nodes[node]

                for node in shortest_paths.get(vertexes[1]):
                    node_x, node_y = pos[node]
                    circle = Circle((node_x, node_y), radius=22, edgecolor='green', facecolor='none', linewidth=4)
                    highlighted_nodes[node] = circle
                    ax.add_patch(circle)
                    plt.pause(1.0)

                message.set_text(f"Маршрут {" -> ".join(shortest_paths.get(vertexes[1]))}\nДовжина - {shortest_path_lengths.get(vertexes[1])} м.")

        plt.show()

    button_2.on_clicked(dijkstra)

    ## Створення кнопки "Очистити" ті її функціоналу
    button_ax = plt.axes([0.76, 0.1, 0.06, 0.04])
    button_3 = Button(button_ax, 'Очистити')

    def reset(event):
        '''
        Скидання раніше обраних значень
        '''
        vertexes.clear()
        nodes = list(highlighted_nodes.keys())
        for node in nodes:
            highlighted_nodes[node].remove()
            del highlighted_nodes[node]
        info.set_text("Оберіть мінімум 1 вершину (за замовченням обрана 'A')\n(2 для розрахунку маршруту).")
        warning.set_text("")
        message.set_text("")
        plt.show()

    button_3.on_clicked(reset)

    plt.show()


if __name__ == "__main__":
    main()