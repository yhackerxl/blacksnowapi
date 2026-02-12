import requests
import time


class SmartHouseAPI:
    BASE_URL = "https://black-snow.onrender.com/api/house"

    def __init__(self, house_id):
        if not house_id:
            raise ValueError("house_id is required")
        self.house_id = house_id

    def _headers(self):
        return {
            "Content-Type": "application/json",
            "X-House-Id": self.house_id
        }

    def _api_call(self, action, params):
        body = {
            "action": action,
            "params": params
        }
        response = requests.post(self.BASE_URL, headers=self._headers(), json=body)
        return response.json()

    def _get_status(self):
        response = requests.get(self.BASE_URL, headers=self._headers())
        return response.json()

    # --------- Lights ---------
    def light_on(self, room):
        return self._api_call("setLight", {"room": room, "on": True})

    def light_off(self, room):
        return self._api_call("setLight", {"room": room, "on": False})

    def toggle_light(self, room):
        return self._api_call("toggleLight", {"room": room})

    # --------- Fan ---------
    def fan_on(self, room):
        return self._api_call("setFan", {"room": room, "on": True})

    def fan_off(self, room):
        return self._api_call("setFan", {"room": room, "on": False})

    # --------- Alarm ---------
    def alarm_on(self):
        return self._api_call("setAlarm", {"on": True})

    def alarm_off(self):
        return self._api_call("setAlarm", {"on": False})

    # --------- Door ---------
    def open_door(self):
        return self._api_call("setLock", {"open": True})

    def close_door(self):
        return self._api_call("setLock", {"open": False})

    def toggle_door(self):
        status = self._get_status()
        current_state = status["door"]["open"]
        return self._api_call("setLock", {"open": not current_state})

    # --------- Blinds ---------
    def set_blinds(self, room, percentage):
        if percentage < 0 or percentage > 100:
            raise ValueError("Percentage must be between 0 and 100")
        return self._api_call("setBlinds", {"room": room, "percentage": percentage})

    def blinds_open(self, room):
        return self.set_blinds(room, 100)

    def blinds_close(self, room):
        return self.set_blinds(room, 0)

    # --------- Thermostat ---------
    def set_thermostat(self, mode, target):
        valid_modes = ["heating", "cooling", "off"]
        if mode not in valid_modes:
            raise ValueError(f"Invalid mode. Choose from {valid_modes}")
        if target < 60 or target > 85:
            raise ValueError("Target temperature must be between 60 and 85")
        return self._api_call("setThermostat", {"mode": mode, "target": target})

    # --------- Utility ---------
    def wait(self, seconds):
        time.sleep(seconds)
        return {"status": "ok", "waited": seconds}
