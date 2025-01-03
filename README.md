Bypassing Waypoint Optimization
Bypassing Waypoint Optimization is an open-source project designed to optimize delivery routes efficiently by leveraging geographic and time-based data. This tool provides a framework for determining the best routes among multiple waypoints while considering store locations, opening hours, and API constraints.

Features
Data Collection: Gathers location coordinates and opening hours for stores (currently configured for Kyiv's Epicenter locations).
Dynamic Grouping: Groups stores into clusters based on geographic proximity with a customizable coordinate deviation.
Combination Analysis: Generates all possible route combinations within clusters to identify optimal paths.
API Integration: Interacts with a Waypoint Optimization API to evaluate route efficiency for various time slots.
Error Handling: Includes random delays to prevent "Too Many Requests" errors and gracefully manages complex-route API limitations.
Result Storage: Outputs the best routes and travel times to JSON files for easy reuse and further analysis.
How It Works
Data Initialization: Extracts and processes store data, grouping them into clusters. For example, 15 locations can be grouped into 12 clusters with a coordinate deviation of 0.035.
Route Simulation: Runs simulations for all possible time slots (e.g., every 30 minutes from 7:30 AM to 6:00 PM) and evaluates combinations using the Waypoint Optimization API.
Optimal Route Selection: Identifies the route with the lowest travel time, ensuring practical delivery schedules (e.g., delivery by the latest store closing time of 10:00 PM).
Result Compilation: Stores results in best_data_points.json and best_results.json for further analysis. Provides formatted output via result.md.
Getting Started
Prerequisites
Python 3.x
A valid API key for the Waypoint Optimization API (insert in constants.py).
Setup Instructions
Clone this repository:
bash
Copy code
git clone https://github.com/yourusername/bypassing-waypoint-optimization.git
cd bypassing-waypoint-optimization
Install dependencies:
bash
Copy code
pip install -r requirements.txt
Insert your API key in constants.py.
Running the Program
Prepare your data:
Modify the data source if needed (e.g., for a different city or dataset).
Update coordinate deviations or time slot ranges in main.py.
Execute the main logic:
bash
Copy code
python main.py
View results:
JSON outputs: best_data_points.json and best_results.json.
Formatted summary: result.md.
Contributing
Contributions are welcome! If you'd like to add new features, fix bugs, or expand the project's compatibility, please fork the repository and submit a pull request. Make sure to follow the existing coding conventions.

License
This project is licensed under the MIT License. See LICENSE for details.
