# find_nearests_elements.py

from utils import is_close
import json

with open("data_with_no_groups.json", "r", encoding="utf-8") as file:
    waypoints = json.load(file)["waypoints"]

groups = []
used_points = set()

for i, waypoint in enumerate(waypoints):
    if i in used_points:
        continue
    group = [waypoint]
    used_points.add(i)
    for j, other_waypoint in enumerate(waypoints[i + 1 :], start=i + 1):
        if j not in used_points and is_close(waypoint, other_waypoint):
            group.append(other_waypoint)
            used_points.add(j)
    groups.append(group)

for idx, group in enumerate(groups):
    print(f"Group {idx}:")
    for point in group:
        print(
            f"  Longitude: {point['longitude']}, Latitude: {point['latitude']}, ID: {point['id']}"
        )

## Output:

# Group 0:
#   Longitude: 30.48622, Latitude: 50.43872, ID: 0
# Group 1:
#   Longitude: 30.520159, Latitude: 50.486754, ID: 1
#   Longitude: 30.486889, Latitude: 50.489589, ID: 2
# Group 2:
#   Longitude: 30.606813, Latitude: 50.523063, ID: 3
#   Longitude: 30.606269, Latitude: 50.522068, ID: 8
# Group 3:
#   Longitude: 30.610474, Latitude: 50.487101, ID: 4
# Group 4:
#   Longitude: 30.480584, Latitude: 50.520904, ID: 5
# Group 5:
#   Longitude: 30.445587, Latitude: 50.37715, ID: 6
# Group 6:
#   Longitude: 30.635416, Latitude: 50.390768, ID: 7
# Group 7:
#   Longitude: 30.354271, Latitude: 50.440018, ID: 9
# Group 8:
#   Longitude: 30.362271, Latitude: 50.493477, ID: 10
# Group 9:
#   Longitude: 30.280509, Latitude: 50.345789, ID: 11
#   Longitude: 30.283, Latitude: 50.349, ID: 14
# Group 10:
#   Longitude: 30.786833, Latitude: 50.520077, ID: 12
# Group 11:
#   Longitude: 30.909599, Latitude: 50.36951, ID: 13