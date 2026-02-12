import requests
import time
BASE_URL = "https://black-snow.onrender.com/api/house"
HOUSE_ID = None


def setup(house_id):
    """Set your house ID before using other functions."""
    global HOUSE_ID
    HOUSE_ID = house_id


def _api_call(action, params):
    if not HOUSE_ID:
        raise ValueError("Call setup(house_id) first")

    headers = {
        "Content-Type": "application/json",
        "X-House-Id": HOUSE_ID
    }

    body = {
        "action": action,
        "params": params
    }

    response = requests.post(BASE_URL, headers=headers, json=body)
    return response.json()


def _get_status():
    headers = {
        "Content-Type": "application/json",
        "X-House-Id": HOUSE_ID
    }
    response = requests.get(BASE_URL, headers=headers)
    return response.json()


# --------- Lights ---------
def on(room):
    return _api_call("setLight", {"room": room, "on": True})


def off(room):
    return _api_call("setLight", {"room": room, "on": False})


def toggle(room):
    return _api_call("toggleLight", {"room": room})


# --------- Fan ---------
def fan_on(room):
    return _api_call("setFan", {"room": room, "on": True})


def fan_off(room):
    return _api_call("setFan", {"room": room, "on": False})


# --------- Alarm ---------
def alarm_on():
    return _api_call("setAlarm", {"on": True})


def alarm_off():
    return _api_call("setAlarm", {"on": False})


# --------- Door ---------
def open_door():
    return _api_call("setLock", {"open": True})


def close_door():
    return _api_call("setLock", {"open": False})


def toggle_door():
    status = _get_status()
    current_state = status["door"]["open"]
    return _api_call("setLock", {"open": not current_state})


# --------- Blinds ---------
def set_blinds(room, percentage):
    if percentage < 0 or percentage > 100:
        raise ValueError("Percentage must be between 0 and 100")
    return _api_call("setBlinds", {"room": room, "percentage": percentage})


# Optional presets
def blinds_open(room):
    return set_blinds(room, 100)


def blinds_close(room):
    return set_blinds(room, 0)


# --------- Thermostat ---------
def set_thermostat(mode, target):
    valid_modes = ["heating", "cooling", "off"]
    if mode not in valid_modes:
        raise ValueError(f"Invalid mode. Choose from {valid_modes}")
    if target < 60 or target > 85:
        raise ValueError("Target temperature must be between 60 and 85")
    return _api_call("setThermostat", {"mode": mode, "target": target})

def wait(seconds):
    time.sleep(seconds)
    return {"status": "ok", "waited": seconds}
