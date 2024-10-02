To start, I gathered all the data from the Epicenter website, including opening times and coordinates for all stores in the city of Kyiv. Then, using the script find_nearest_elements.py, I identified nearby stores and grouped them. I chose a coordinate deviation of 0.035, which allows us to create exactly 12 groups from 15 locations.

I converted these groups into objects and assigned them to specific variables in main.py, where the main logic takes place. First, we generate all possible combinations of elements within each group. This helps us choose which point within the group will make the route faster. There will be about 8 combinations of points within the groups in total. Next, we create 30-minute intervals and, for each combination and for every possible time slot (7:30, 8:00, 8:30, ..., 18:00), we send a request to the Waypoint Optimization API. The end time of 18:00 was selected based on the assumption that the delivery person will be able to deliver the goods by 22:00, which is the latest closing time of the stores. This is also based on the calculated average from the first run of the program – 3 hours and 48 minutes.

Then, we find the best result with the lowest travelTimeInSeconds. We also add a random delay of 1 to 2 seconds to avoid a "Too Many Requests" error. This request may result in errors if the predicted route is too complex, but this will not prevent us from finding the best route.

We copy these results into JSON files best_data_points.json and best_results.json. Then, using the script find_best_results.py, we format the results from main.py, taking into account the grouping we did earlier.

The results can be found in the file result.md.

If you want to test the program yourself, you will need to insert the api_key in the file constants.py. This api_key will be linked to an email address.
