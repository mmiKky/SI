import time
from datetime import datetime

import dataReader
from graph import Vertex
import shortestPathAlgorithms as shortest_path_algos


def print_path(path_list, first_stop):
    if path_list == None:
        print('Route impossible')
        return
    longer_spaces_nr = 50
    shorter_spaces_nr = 20
    print(f'{first_stop.name:<{longer_spaces_nr}} ({first_stop.lat},{first_stop.lon})', end='')
    while path_list != []:
        connection = path_list.pop()
        next_stop = connection.end_stop
        print(f'{connection.line:^{shorter_spaces_nr}} {connection.departure_time}-{connection.arrival_time}')
        print(f'{next_stop.name:<{longer_spaces_nr}} ({next_stop.lat},{next_stop.lon})', end='')
    print()


if __name__ == '__main__':
    graph = dataReader.create_graph()
    start_stop = Vertex(name='Hala Stulecia', lat='51.10708825', lon='17.07346452')
    start_time = datetime.strptime('13:43:00', '%H:%M:%S').time()
    end_stop = 'most Grunwaldzki'

    exec_start_time = time.time()
    shortest_path = shortest_path_algos.find_shortest_path_dijkstra(graph, start_stop, end_stop, start_time)
    print('dijkstra, execution time: ', time.time() - exec_start_time)
    print_path(shortest_path, start_stop)
    print()
    exec_start_time = time.time()
    shortest_path = shortest_path_algos.find_shortest_path_Astar_time(graph, start_stop, end_stop, start_time)
    print('A*, execution time: ', time.time() - exec_start_time)
    print_path(shortest_path, start_stop)
    print()
    exec_start_time = time.time()
    shortest_path = shortest_path_algos.find_shortest_path_Astar_change(graph, start_stop, end_stop, start_time)
    print('A*_changes, execution time: ', time.time() - exec_start_time)
    print_path(shortest_path, start_stop)
    print()

    end_stop = 'Ogród Botaniczny'
    exec_start_time = time.time()
    shortest_path = shortest_path_algos.find_shortest_path_dijkstra(graph, start_stop, end_stop, start_time)
    print('dijkstra, execution time: ', time.time() - exec_start_time)
    print_path(shortest_path, start_stop)
    print()
    exec_start_time = time.time()
    shortest_path = shortest_path_algos.find_shortest_path_Astar_time(graph, start_stop, end_stop, start_time)
    print('A*, execution time: ', time.time() - exec_start_time)
    print_path(shortest_path, start_stop)
    print()
    exec_start_time = time.time()
    shortest_path = shortest_path_algos.find_shortest_path_Astar_change(graph, start_stop, end_stop, start_time)
    print('A*_changes, execution time: ', time.time() - exec_start_time)
    print_path(shortest_path, start_stop)
    print()


    end_stop = 'Trawowa'
    exec_start_time = time.time()
    shortest_path = shortest_path_algos.find_shortest_path_dijkstra(graph, start_stop, end_stop, start_time)
    print('dijkstra, execution time: ', time.time() - exec_start_time)
    print_path(shortest_path, start_stop)
    print()
    exec_start_time = time.time()
    shortest_path = shortest_path_algos.find_shortest_path_Astar_time(graph, start_stop, end_stop, start_time)
    print('A*, execution time: ', time.time() - exec_start_time)
    print_path(shortest_path, start_stop)
    print()
    exec_start_time = time.time()
    shortest_path = shortest_path_algos.find_shortest_path_Astar_change(graph, start_stop, end_stop, start_time)
    print('A*_changes, execution time: ', time.time() - exec_start_time)
    print_path(shortest_path, start_stop)
    print()
