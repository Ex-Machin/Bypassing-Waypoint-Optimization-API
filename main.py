# main.py

import requests
from PIL import Image
from io import BytesIO
import json
import itertools
from utils import transform_waypoints, generate_rfc3339_string

api_key = "R9ig8OCACmamWAzsHIGmvniYUBKWyqhs"
base_url = "https://api.tomtom.com"
endpoint = "routing"
version = 1
url = f"{base_url}/{endpoint}/waypointoptimization/1?key={api_key}"

with open("data.json", "r", encoding="utf-8") as file:
    points = json.load(file)

# Generate all possible combinations of waypoints that are in the same group
group_keys = ["group_1", "group_2", "group_9"]
combinations = list(itertools.product(*[points[key] for key in group_keys]))

best_result = None
best_combination = None

all_groups = [
    "group_0", "group_1", "group_2", "group_3", "group_4",
    "group_5", "group_6", "group_7", "group_8", "group_9",
    "group_10", "group_11"
]

for combination in combinations:
    current_points = []
    current_points.append(points["group_0"][0])
    current_points.append(combination[0])
    current_points.append(combination[1])
    current_points.append(points["group_3"][0])
    current_points.append(points["group_4"][0])
    current_points.append(points["group_5"][0])
    current_points.append(points["group_6"][0])
    current_points.append(points["group_7"][0])
    current_points.append(points["group_8"][0])
    current_points.append(combination[2])
    current_points.append(points["group_10"][0])
    current_points.append(points["group_11"][0])

    transformed_waypoints = transform_waypoints(current_points)
    print(transformed_waypoints)

    # data = {
    #     "waypoints": transformed_waypoints,
    #     "options": {
    #         "travelMode": "car",
    #         "vehicleCommercial": False,
    #         "traffic": "live",
    #         "departAt": generate_rfc3339_string(
    #             year=2024, month=7, day=1, hour=7, minute=30, second=0, offset_hours=0
    #         ),  # 7:30 AM on July 1, 2024, Monday
    #         "outputExtensions": ["travelTimes", "routeLengths"],
    #         "waypointConstraints": {"originIndex": 0, "destinationIndex": 0},
    #     },
    # }

    # response = requests.post(url, json=data)

    # print(response.json())
    # print(current_points)
    # break
