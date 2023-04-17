import multiprocessing
import pandas as pd
from geopy.distance import distance

# Define a function to calculate the distance between two locations using geopy's distance method
def calculate_distance(loc1, loc2):
    return distance(loc1, loc2).km

# Define a function to calculate the total distance traveled by a user
def calculate_user_distance(user_data):
    # Get the unique trajectories for the user
    unique_trajectories = user_data['trajectory_id'].unique()
    
    # Calculate the total distance for each trajectory
    trajectory_distances = []
    for trajectory_id in unique_trajectories:
        # Get the location data for the current trajectory
        trajectory_data = user_data[user_data['trajectory_id'] == trajectory_id]
        locations = [(row['latitude'], row['longitude'], row['altitude']) for index, row in trajectory_data.iterrows()]
        
        # Calculate the distance for the current trajectory using parallel processing
        pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
        distances = sum(pool.starmap(calculate_distance, zip(locations[:-1], locations[1:])))
        pool.close()
        pool.join()
        
        trajectory_distances.append(distances)
    
    # Calculate the total distance for the user by summing the distances for each trajectory
    total_distance = sum(trajectory_distances)
    
    return total_distance

# Load the dataset
df = pd.read_csv("C:/Users/nishk/Downloads/combined_trajectories.csv")

# Calculate the total distance traveled by each user
total_distances = []
for user_id in df['individual_id'].unique():
    user_data = df[df['individual_id'] == user_id]
    total_distance = calculate_user_distance(user_data)
    total_distances.append(total_distance)

# Print the distance of each user
for i, distance in enumerate(total_distances):
    print("The total distance traveled by individual " + str(i+1) + " is: " + str(distance) + " km")
