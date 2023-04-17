import pandas as pd
import datetime as dt
import osmnx as ox
import networkx as nx

def Part1(df):
    start_time = dt.datetime.now()  # Record start time for runtime calculation


    # Convert start and end time columns to datetime objects
    df['started_at'] = pd.to_datetime(df['started_at'])
    df['ended_at'] = pd.to_datetime(df['ended_at'])

    # Calculate trip duration in minutes and filter out trips with duration 0 minutes
    df['trip_duration'] = (df['ended_at'] - df['started_at']).dt.total_seconds() / 60
    df = df[df['trip_duration'] > 0]

    # Calculate and print maximum and minimum trip durations
    max_duration = df['trip_duration'].max()
    min_duration = df['trip_duration'].min()
    print("Maximum duration of the trip (in minutes):", max_duration)
    print("Minimum duration of the trip (in minutes):", min_duration)

    # Calculate and print total number of trips corresponding to the minimum duration
    total_trips_min_duration = df[df['trip_duration'] == min_duration].shape[0]
    print("Total number of trips corresponding to the minimum duration:", total_trips_min_duration)

    # Calculate and print percentage of total circular trips
    total_circular_trips = df.loc[(df['start_lat'] == df['end_lat']) & (df['start_lng'] == df['end_lng'])].shape[0]
    percentage_circular_trips = (total_circular_trips / df.shape[0]) * 100
    print("Percentage of total circular trips:", percentage_circular_trips, "%")

    # Calculate and print total runtime for the function
    end_time = dt.datetime.now()
    total_runtime = (end_time - start_time).total_seconds()
    print("Total runtime for the function (in seconds):", total_runtime)

def Part2(df):
    start_time = dt.datetime.now()

    # Convert "started_at" column to datetime
    df['started_at'] = pd.to_datetime(df['started_at'])

    # Filter for trips starting between 6:00 AM and 6:00 PM
    df = df[(df['started_at'].dt.hour >= 6) & (df['started_at'].dt.hour < 18) | ((df['started_at'].dt.hour == 18) & (df['started_at'].dt.minute == 0) & (df['started_at'].dt.second == 0))]
    # Join the dataset to itself
    pairs = pd.merge(df, df, left_on=['end_lat', 'end_lng'], right_on=['start_lat', 'start_lng'])

    # Filter for feasible pairs
    feasible_pairs = pairs[pairs['ended_at_x'] <= pairs['started_at_y']]
    # Count the total number of feasible pairs
    num_feasible_pairs = len(feasible_pairs)

    print(f"Total number of feasible pairs of trips: {num_feasible_pairs}")
    # Filter feasible pair for trip id 4611
    feasible_pairs_4611 = feasible_pairs[(feasible_pairs['trip_id_x'] == 4611) | (feasible_pairs['trip_id_y'] == 4611)]

    # Create a new DataFrame from the results
    df_feasible_pairs_4611 = pd.DataFrame({
        'trip_id_x': feasible_pairs_4611['trip_id_x'],
        'trip_id_y': feasible_pairs_4611['trip_id_y'],
        'start_time_x': feasible_pairs_4611['started_at_x'],
        'end_time_x': feasible_pairs_4611['ended_at_x'],
        'start_time_y': feasible_pairs_4611['started_at_y'],
        'end_time_y': feasible_pairs_4611['ended_at_y'],
        'start_lat_x': feasible_pairs_4611['start_lat_x'],
        'start_lng_x': feasible_pairs_4611['start_lng_x'],
        'end_lat_x': feasible_pairs_4611['end_lat_x'],
        'end_lng_x': feasible_pairs_4611['end_lng_x'],
        'start_lat_y': feasible_pairs_4611['start_lat_y'],
        'start_lng_y': feasible_pairs_4611['start_lng_y'],
        'end_lat_y': feasible_pairs_4611['end_lat_y'],
        'end_lng_y': feasible_pairs_4611['end_lng_y'],

    })

    # Print the new DataFrame
    print(df_feasible_pairs_4611)
    # Calculate and print total runtime for the function
    end_time = dt.datetime.now()
    total_runtime = (end_time - start_time).total_seconds()
    print("Total runtime for the function (in seconds):", total_runtime)
    
def Part3(df):
    start_time = dt.datetime.now() 
    df = df.iloc[:100]

    # get the unique depots used
    depots = df[['start_lat', 'start_lng']].drop_duplicates().values.tolist()
    depots += df[['end_lat', 'end_lng']].drop_duplicates().values.tolist()
    unique_depots = list(set([tuple(x) for x in depots]))

    print(f'Number of unique depots: {len(unique_depots)}')

    G = ox.graph_from_point(unique_depots[0], network_type="all")

    nearest=[]
    for i in unique_depots:
        nearest_node = ox.distance.nearest_nodes(G,i[1],i[0])
        nearest.append(nearest_node)
        


    distance=[]

    for i in range(len(nearest)):
        for j in range(i+1,len(nearest)):
           try:
              length, path=nx.bidirectional_dijkstra(G, nearest[i], nearest[j], weight='length')
           except nx.NetworkXNoPath:
               length=-1
               path=[]
         
           distance.append([length,path])
          
    length=[i[0] for i in distance]
    min_distance=min(i for i in length if i>0)  
    index1=length.index(min_distance)  

    max_distance=max(length)
    index2=length.index(max_distance)  

    fig, ax = ox.plot_graph_route(G, distance[index1][1])
    fig, ax = ox.plot_graph_route(G, distance[index2][1])

    end_time = dt.datetime.now()
    total_runtime = (end_time - start_time).total_seconds()
    print("Total runtime for the function (in seconds):", total_runtime)
    
# Load dataset into a pandas DataFrame
df = pd.read_csv("C:/Users/nishk/Downloads/bike_data_new.csv")
print("\nAnswer1:\n")
Part1(df)
print("\nAnswer2:\n")
Part2(df)
print("\nAnswer3:\n")
Part3(df)
