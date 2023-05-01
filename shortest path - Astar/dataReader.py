import pandas as pd
from graph import Graph, Vertex, Edge
from datetime import datetime

pd.set_option('display.max_rows', None)
def read_data():
    return pd.read_csv('connection_graph.csv', dtype=str)

def create_graph():
    graph = Graph()
    data = read_data()
    for index, row in data.iterrows():
        start_stop = Vertex(name=row['start_stop'], lat=row['start_stop_lat'], lon=row['start_stop_lon'])
        end_stop = Vertex(name=row['end_stop'], lat=row['end_stop_lat'], lon=row['end_stop_lon'])

        departure_time = datetime.strptime(row['departure_time'], '%H:%M:%S').time()
        arrival_time = datetime.strptime(row['arrival_time'], '%H:%M:%S').time()
        
        connection = Edge(departure_time=departure_time, arrival_time=arrival_time, company=row['company'], 
                          line=row['line'], end_stop=end_stop)
        
        graph.add_edge(start_stop, connection)
        graph.add_vertex(end_stop)
        if index % 10000 == 0:
            print(f'reading data from file, row nr: {index}')
    return graph
