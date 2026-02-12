# BlacksnowAPI

Beginner-friendly Python library to control a smart house using the Black Snow API.

BlacksnowAPI v1.0.0 introduces a clean, class-based interface for controlling:

* Lights
* Fan
* Alarm
* Door
* Blinds
* Thermostat

## Installation

```bash
pip install blacksnowapi
````

## Quick Start

```python
from blacksnowapi import SmartHouseAPI

house = SmartHouseAPI("YOUR_HOUSE_ID")

house.light_on("living")
house.fan_on("bedroom")
house.set_thermostat("cooling", 72)
```

## Setup

Create an instance of `SmartHouseAPI` using your house ID:

```python
from blacksnowapi import SmartHouseAPI

house = SmartHouseAPI("YOUR_HOUSE_ID")
```

* `YOUR_HOUSE_ID`: The unique 5-letter ID assigned to your smart house. You can obtain it from [Black Snow Smart House Labs](https://black-snow.onrender.com/labs/smart-house).
* Required before calling any method.

# Features

## Lights

### Turn On Lights

```python
house.light_on("living")
```

### Turn Off Lights

```python
house.light_off("bedroom")
```

### Toggle Lights

```python
house.toggle_light("kitchen")
```

* `room`: One of the following strings: `"living"`, `"bedroom"`, `"kitchen"`, `"office"`, `"outdoor"`


## Fan

### Turn Fan On

```python
house.fan_on("living")
```

### Turn Fan Off

```python
house.fan_off("bedroom")
```

* `room`: Same as lights: `"living"`, `"bedroom"`, `"kitchen"`, `"office"`, `"outdoor"`
* Value: `True` = on, `False` = off

## Alarm

### Turn Alarm On

```python
house.alarm_on()
```

### Turn Alarm Off

```python
house.alarm_off()
```

* Value: `True` = on, `False` = off


## Door

### Open Door

```python
house.open_door()
```

### Close Door

```python
house.close_door()
```

### Toggle Door

```python
house.toggle_door()
```

* Value: `True` = open, `False` = closed

## Blinds

### Set Blinds Percentage

```python
house.set_blinds("living", 50)
house.set_blinds("bedroom", 0)
house.set_blinds("kitchen", 100)
```

* `room`: `"living"`, `"bedroom"`, `"kitchen"`
* `percentage`: Integer between 0–100 (0 = fully open, 100 = fully closed)

### Fully Open Blinds

```python
house.blinds_open("living")
```

### Fully Close Blinds

```python
house.blinds_close("bedroom")
```

## Thermostat

### Set Thermostat

```python
house.set_thermostat("heating", 72)
house.set_thermostat("cooling", 70)
house.set_thermostat("off", 65)
```

* `mode`: `"heating"`, `"cooling"`, `"off"`
* `target`: Number between 60–85


## Utility

### Wait

```python
house.wait(5)
```

Pauses execution for a number of seconds.

# Full Example

```python
from blacksnowapi import SmartHouseAPI

house = SmartHouseAPI("ABCDE")

# Lights
house.light_on("living")
house.light_off("bedroom")
house.toggle_light("kitchen")

# Fan
house.fan_on("living")
house.fan_off("bedroom")

# Alarm
house.alarm_on()
house.alarm_off()

# Door
house.open_door()
house.close_door()
house.toggle_door()

# Blinds
house.set_blinds("living", 50)
house.blinds_open("bedroom")
house.blinds_close("kitchen")

# Thermostat
house.set_thermostat("heating", 72)
house.set_thermostat("cooling", 70)
house.set_thermostat("off", 65)
```

# Notes

* A valid `house_id` is required when creating `SmartHouseAPI`. You can obtain it from [Black Snow Smart House Labs](https://black-snow.onrender.com/labs/smart-house).
* Room names must match your house configuration: `"living"`, `"bedroom"`, `"kitchen"`, `"office"`, `"outdoor"`.
* Blinds percentage must be between 0–100.
* Thermostat temperature must be between 60–85.
* Thermostat mode must be `"heating"`, `"cooling"`, or `"off"`.
* Lights, fan, alarm, and door values are boolean (`True` = on/open, `False` = off/closed).
* Version 1.0.0 uses a class-based interface (older function-based versions are deprecated).
