import json
from utils import format_time, format_point

with open("best_data_points.json", "r", encoding="utf-8") as file:
    best_data_points = json.load(file)

with open("best_result.json", "r", encoding="utf-8") as file:
    best_results = json.load(file)

with open("data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

leg_summaries = best_results["summary"]["legSummaries"]
travel_time_in_seconds = best_results["summary"]["routeSummary"]["travelTimeInSeconds"]
departure_time = best_results["summary"]["routeSummary"]["departureTime"]
arrival_time = best_results["summary"]["routeSummary"]["arrivalTime"]
group_keys = [1, 2, 9]

print(f"Travel time: {format_time(travel_time_in_seconds)}")
print(f"Departure time: {departure_time}")
print(f"Arrival time: {arrival_time}")

for i in range(len(leg_summaries)):
    origin_index = leg_summaries[i]["originIndex"]
    current = best_data_points[origin_index]
    if current["group_id"] in group_keys:
        format_point(current)
        # iterate over the waypoints to find the point with the same group_id
        for group_id in data.keys():
            if group_id == "group_" + str(current["group_id"]):
                for waypoint in data[group_id]:
                    if waypoint["address"] != current["address"]:
                        format_point(waypoint)
    else:
        format_point(current)

print(f"Південний вокзал")