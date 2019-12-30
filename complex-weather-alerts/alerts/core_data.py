from pathlib import Path
import json


unwanted= ['icon', 'summary', 'apparentTemperature', 'nearestStormBearing', 'nearestStormDistance', 'temperature', 'time']

with Path('alerts/datapoint.json').open() as f:
    datapoint_schema = json.load(f)
