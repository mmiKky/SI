import heapq
import math
from datetime import datetime, timedelta, date

def find_shortest_path_dijkstra(graph, start_stop, end_stop_name, start_time):
    distances = {stop: float('inf') for stop in graph.get_vertices()}
    distances[start_stop] = 0
    paths = dict()
    
    # priority queue
    pq = [(0, start_stop)]
    
    while pq:
        # element with the smallest distance
        (dist, current_stop) = heapq.heappop(pq)
        
        # end_stop was found - no need to countinue searching
        if current_stop.name == end_stop_name:
            return make_list(paths, current_stop)
        
        current_time = (datetime.combine(date.today(), start_time) + timedelta(minutes=distances[current_stop])).time()
        for neighbor, (connection, waiting_time) in get_earliest_connections_with_waiting_time(
                                                    graph.get_edges(current_stop), current_time, current_stop).items():
            new_distance = distances[current_stop] + calculate_weights_based_on_time(waiting_time, 
                                                                                     connection.departure_time, 
                                                                                     connection.arrival_time)
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                paths[neighbor] = (current_stop, connection)
                heapq.heappush(pq, (new_distance, neighbor))
    
    # no path between nodes
    return None


def heuristic_function_distance(start_point, end_point):
    velocity_kmh = 50
    x1, y1 = float(start_point[0]), float(start_point[1])
    x2, y2 = float(end_point[0]), float(end_point[1])
    # euclidean distance in kilometers
    distance_km = math.sqrt((x2 - x1)**2 + (y2 - y1)**2) * 111.32
    # v = s/t => t = s/v; result coverted to minutes
    return distance_km / velocity_kmh * 60


def find_shortest_path_Astar_time(graph, start_stop, end_stop_name, start_time):
    distances = {stop: float('inf') for stop in graph.get_vertices()}
    distances[start_stop] = 0

    paths = dict()
    
    # priority queue
    pq = [(0, start_stop)]
    
    while pq:
        # element with the smallest distance
        (dist, current_stop) = heapq.heappop(pq)
        
        # end_stop was found - no need to countinue searching
        if current_stop.name == end_stop_name:
            return make_list(paths, current_stop)
        
        current_time = (datetime.combine(date.today(), start_time) + timedelta(minutes=distances[current_stop])).time()
        for neighbor, (connection, waiting_time) in get_earliest_connections_with_waiting_time(
                                                    graph.get_edges(current_stop), current_time, current_stop).items():
            new_distance = distances[current_stop] + calculate_weights_based_on_time(waiting_time, 
                                                                                     connection.departure_time, 
                                                                                     connection.arrival_time)
            if new_distance < distances[neighbor]:
                heuristic = heuristic_function_distance((current_stop.lon, current_stop.lat), (neighbor.lon, neighbor.lat))
                distances[neighbor] = new_distance
                paths[neighbor] = (current_stop, connection)
                heapq.heappush(pq, (new_distance + heuristic, neighbor))
    
    # no path between nodes
    return None


def find_shortest_path_Astar_change(graph, start_stop, end_stop_name, start_time):
    distances = {stop: float('inf') for stop in graph.get_vertices()}
    distances[start_stop] = 0

    paths = dict()
    
    # priority queue
    pq = [(0, start_stop)]
    
    while pq:
        # element with the smallest distance
        (dist, current_stop) = heapq.heappop(pq)
        
        # end_stop was found - no need to countinue searching
        if current_stop.name == end_stop_name:
            return make_list(paths, current_stop)
        
        current_time = (datetime.combine(date.today(), start_time) + timedelta(minutes=distances[current_stop])).time()
        for neighbor, (connection, waiting_time) in get_earliest_connections_with_waiting_time(
                                                    graph.get_edges(current_stop), current_time, current_stop).items():
            new_distance = distances[current_stop] + calculate_weights_based_on_time(waiting_time, 
                                                                                     connection.departure_time, 
                                                                                     connection.arrival_time)
            if new_distance < distances[neighbor]:
                heuristic = heuristic_function_distance((current_stop.lon, current_stop.lat), (neighbor.lon, neighbor.lat))
                distances[neighbor] = new_distance
                paths[neighbor] = (current_stop, connection)
                heapq.heappush(pq, (new_distance + heuristic, neighbor))
    
    # no path between nodes
    return None


def find_shortest_path_Astar_change(graph, start_stop, end_stop_name, start_time):
    distances = {stop: float('inf') for stop in graph.get_vertices()}
    distances[start_stop] = 0
    elapsed_time = dict()
    elapsed_time[start_stop] = 0

    paths = dict()
    
    # priority queue
    pq = [(0, start_stop)]
    
    is_first = True
    while pq:
        # element with the smallest distance
        (dist, current_stop) = heapq.heappop(pq)
        
        # end_stop was found - no need to countinue searching
        if current_stop.name == end_stop_name:
            return make_list(paths, current_stop)
        
        current_time = (datetime.combine(date.today(), start_time) + timedelta(minutes=elapsed_time[current_stop])).time()
        for neighbor, (connection, waiting_time) in get_earliest_connections_with_waiting_time(
                                                    graph.get_edges(current_stop), current_time, current_stop).items():
            new_elapsed_time = elapsed_time[current_stop] + calculate_weights_based_on_time(waiting_time, 
                                                                                     connection.departure_time, 
                                                                                     connection.arrival_time)
            if not is_first: # first stop doesn't have connection to itself, so just skip it
                new_distance = distances[current_stop] + calculate_weights_based_on_changes(connection.line, 
                                                                                        paths[current_stop][1].line,
                                                                                        waiting_time)
            else:
                new_distance = distances[current_stop]
                is_first = False

            if new_distance < distances[neighbor]:
                heuristic = heuristic_function_distance((current_stop.lon, current_stop.lat), (neighbor.lon, neighbor.lat))
                elapsed_time[neighbor] = new_elapsed_time
                distances[neighbor] = new_distance
                paths[neighbor] = (current_stop, connection)
                heapq.heappush(pq, (new_distance + heuristic, neighbor))
    
    # no path between nodes
    return None


'''calculates how much time it takes to arrive at the next stop based on current time; result is in minutes'''
'''waiting_time is a difference between current time and departure time - it was calculate before'''
def calculate_weights_based_on_time(waiting_time, departure_time, arrival_time):
    return (waiting_time + calculate_time_difference(departure_time, arrival_time)).total_seconds() // 60


def calculate_weights_based_on_changes(line_nr1, line_nr2, waiting_time):
    if line_nr1 != line_nr2:
        return 10
    return 0


def get_the_same_line_connections():
    pass


def get_earliest_connections_with_waiting_time(connections, current_time, current_stop):
    eariliest_connections = dict()

    for connection in connections:
        time_diff = calculate_time_difference(current_time, connection.departure_time)
        if connection.end_stop not in eariliest_connections:
            eariliest_connections[connection.end_stop] = (connection, time_diff)
        elif time_diff < eariliest_connections[connection.end_stop][1]:
            eariliest_connections[connection.end_stop] = (connection, time_diff)

    return eariliest_connections


def calculate_time_difference(start_time, end_time):
    start_time = timedelta(hours=start_time.hour, minutes=start_time.minute)
    end_time = timedelta(hours=end_time.hour, minutes=end_time.minute)
    time_diff = end_time - start_time
    if time_diff < timedelta(0):
        time_diff += timedelta(hours=24)
    return time_diff


def make_list(paths, end_stop):
    if paths == None:
        return None
    
    path_list = []
    last_stop = end_stop

    while last_stop in paths:
        next_stop, connection = paths[last_stop]
        path_list.append(connection)
        last_stop = next_stop
    return path_list
