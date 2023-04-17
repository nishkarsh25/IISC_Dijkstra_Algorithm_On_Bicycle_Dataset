# IISC_Dijkstra_Algorithm_On_Bicycle_Dataset
### Function Analysis Report

The function `Part1` is a Python function that takes a DataFrame `df` as input and performs various operations to analyze a dataset containing information about bicycle trips in a bicycle-sharing system. Let's go through the code step by step to understand what it does:

1. Record Start Time: The function records the start time using the `dt.datetime.now()` function, which will be used to calculate the runtime of the function.

2. Convert Columns to Datetime: The "started_at" and "ended_at" columns of the DataFrame are converted to datetime objects using the `pd.to_datetime()` function.

3. Calculate Trip Duration: The "trip_duration" column is calculated by subtracting the "started_at" column from the "ended_at" column, converting the result to seconds, and then dividing by 60 to get the duration in minutes.

4. Filter Zero Duration Trips: Trips with a duration of 0 minutes are filtered out from the DataFrame using boolean indexing.

5. Calculate Maximum and Minimum Trip Durations: The maximum and minimum trip durations are calculated using the `max()` and `min()` functions on the "trip_duration" column, respectively.

6. Count Trips with Minimum Duration: The total number of trips corresponding to the minimum duration is calculated by filtering the DataFrame using boolean indexing and then getting the shape (number of rows) of the resulting DataFrame.

7. Count Circular Trips: The total number of circular trips is calculated by filtering the DataFrame using boolean indexing to find trips where the starting latitude and longitude match the ending latitude and longitude, and then getting the shape (number of rows) of the resulting DataFrame.

8. Calculate Percentage of Circular Trips: The percentage of total circular trips is calculated by dividing the total number of circular trips by the total number of trips in the DataFrame and multiplying by 100.

9. Calculate Runtime: The runtime of the function is calculated by subtracting the start time recorded at the beginning of the function from the current time, and the result is printed along with the other calculated values.

Note: The function assumes that the input DataFrame "df" has columns named "started_at", "ended_at", "start_lat", "start_lng", and "end_lat", and "end_lng" with the corresponding data types. If the column names or data types are different in the actual dataset, the function may not work correctly and may need to be modified accordingly.

<img width="700" alt="image" src="https://user-images.githubusercontent.com/117291117/232605217-1fb584cb-2e83-44ec-b77a-02237abb5c4e.png">
