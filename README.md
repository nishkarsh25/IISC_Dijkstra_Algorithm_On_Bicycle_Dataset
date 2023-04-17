# Difficulty viewing large code files?

If you're having trouble viewing large code files on GitHub, you may find it helpful to download a ZIP file containing the entire repository. To do so, follow these steps:

1. Click on the green "Code" button on the repository page.
2. Select "Download ZIP" from the dropdown menu.
3. Save the ZIP file to your computer.

This can be particularly useful if you're experiencing issues with GitHub's web interface or if you need to access the repository without an internet connection. If you have any questions or concerns, please don't hesitate to contact us. 
<img width="700" alt="image" src="https://user-images.githubusercontent.com/117291117/231703905-7469ae09-6d82-4f77-ad05-fa29142ac9a8.png">
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

The function `Part2` is a Python function that takes a DataFrame `df` as input and performs various operations to analyze a dataset containing information about bicycle trips in a bicycle-sharing system. Let's go through the code step by step to understand what it does:
1. Convert "started_at" column to datetime data type using `pd.to_datetime()` function.
2. Filter DataFrame to keep only rows where "started_at" time is between 6:00 AM and 6:00 PM or exactly 6:00 PM using hour, minute, and second components of "started_at" column.
3. Merge filtered DataFrame with itself, joining on "end_lat" and "end_lng" columns of the first instance, and "start_lat" and "start_lng" columns of the second instance, using `pd.merge()` function.
4. Filter merged DataFrame to keep only pairs where "ended_at" time of the first trip is earlier than or equal to "started_at" time of the second trip.
5. Calculate total number of feasible pairs by counting length of filtered DataFrame.
6. Filter feasible pairs DataFrame again to keep only rows where either "trip_id_x" or "trip_id_y" is equal to 4611.
7. Create a new DataFrame containing selected columns from the filtered feasible pairs DataFrame.
8. Return the new DataFrame as the final output of the function.

