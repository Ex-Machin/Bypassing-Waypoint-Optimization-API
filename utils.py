# utils.py

from datetime import datetime, timezone, timedelta

def transform_waypoints(input_data):
    transformed_waypoints = []
    for waypoint in input_data:
        working_hours = waypoint.get("working_hours", None)
        new_waypoint = {
            "point": {
                "longitude": waypoint["longitude"],
                "latitude": waypoint["latitude"],
            },
            "serviceTimeInSeconds": 600
        }
        
        if working_hours:
            new_waypoint["timeWindows"] = [
                {
                    "openingHour": working_hours[0].get('opening_hours', '00:00'),
                    "closingHour": working_hours[0].get('closing_hours', '23:59'),
                }
            ]

        transformed_waypoints.append(new_waypoint)
    return transformed_waypoints

def generate_rfc3339_string(year, month, day, hour, minute, second, offset_hours=0):
    dt = datetime(year, month, day, hour, minute, second, tzinfo=timezone(timedelta(hours=offset_hours)))
    return dt.isoformat()

# Treshold is set to 0.035 to get 12 groups to align it with API restrictions
def is_close(point1, point2, threshold=0.035):
    return (
        abs(point1["longitude"] - point2["longitude"]) < threshold
        and abs(point1["latitude"] - point2["latitude"]) < threshold
    )