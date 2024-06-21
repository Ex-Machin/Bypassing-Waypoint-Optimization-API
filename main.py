# main.py

import requests
import json
import itertools
from utils import transform_waypoints, generate_rfc3339_string
from time import sleep
import random
from constants import url
from datetime import datetime, timedelta, timezone

with open("data.json", "r", encoding="utf-8") as file:
    points = json.load(file)

# Generate all possible combinations of waypoints that are in the same group
group_keys = ["group_1", "group_2", "group_9"]
combinations = list(itertools.product(*[points[key] for key in group_keys]))

fastest_route = None
best_data_points = None

all_groups = [
    "group_0", "group_1", "group_2", "group_3", "group_4",
    "group_5", "group_6", "group_7", "group_8", "group_9",
    "group_10", "group_11"
]
travel_times = []

start_time = datetime(year=2024, month=7, day=1, hour=7, minute=30, second=0, tzinfo=timezone(timedelta(hours=0)))
# 18:30 hours comes from the assumption that vehicle can be on time at 22:00, when the last point closes
# because avarage time of the route is 3 hours and 48 minutes.
# subsctracting 3 hours and 48 minutes from 22:00 gives us 18:12
# the closest time to 18:12 is 18:00 if we want to stick to 30 minutes intervals
end_time = datetime(year=2024, month=7, day=1, hour=18, minute=0, second=0, tzinfo=timezone(timedelta(hours=0)))

for interval in range(0, (end_time - start_time).seconds // 1800 + 1):
    for combination in combinations:
        data_points = []

        current_time = start_time + timedelta(minutes=30 * interval)

        # print(current_time.isoformat())
        for group in all_groups:
            if group in group_keys:
                data_points.append(combination[group_keys.index(group)])
            else:
                data_points.append(points[group][0])

        # Adjusting the data points to the required format of the API
        transformed_waypoints = transform_waypoints(data_points)

        data = {
            "waypoints": transformed_waypoints,
            "options": {
                "travelMode": "car",
                "vehicleCommercial": False,
                "traffic": "live",
                "departAt": current_time.isoformat(),
                "outputExtensions": ["travelTimes", "routeLengths"],
                "waypointConstraints": {"originIndex": 0, "destinationIndex": 0},
            },
        }
        result = requests.post(url, json=data)

        if result.status_code == 200:
            travel_time = result.json()["summary"]["routeSummary"]["travelTimeInSeconds"]
            if travel_time:
                travel_times.append(travel_time)

            # Check if the current route is faster than the previous one
            if (
                fastest_route is None
                or travel_time
                < fastest_route.json()["summary"]["routeSummary"]["travelTimeInSeconds"]
            ):
                fastest_route = result
                best_data_points = data_points
                print(f"New best route found for time {current_time.isoformat()}. Travel time: {travel_time} seconds.")
        else:
            print(f"Request failed for time {current_time.isoformat()} and combination {combination}")
            print(result.__dict__)

        # Sleep for a random amount of time between 1 and 3 seconds
        # to avoid hitting Too Many Requests error
        sleep(random.randint(1, 2))

print(fastest_route.json())
print(best_data_points)

# Analyze the results
if travel_times:
    average_travel_time = sum(travel_times) / len(travel_times)
    max_travel_time = max(travel_times)
    min_travel_time = min(travel_times)

    print(f"Average travel time: {average_travel_time} seconds")
    print(f"Max travel time: {max_travel_time} seconds")
    print(f"Min travel time: {min_travel_time} seconds")
else:
    print("No travel times were recorded.")