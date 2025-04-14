import time
import random
from azure.iot.device import IoTHubDeviceClient, Message

CONNECTION_STRING = "HostName=IOT-hub-rideau-canal.azure-devices.net;DeviceId=sensor2-fiftheave;SharedAccessKey=cMI/ZmWlSPEvH6uQEYHr0offoG1DjbUjdIlT3nbjqm0="

def get_sensor_data():
    return {
        "location": "Fifth Avenue",
        "iceThickness": round(random.uniform(5.0, 40.0), 2),
        "surfaceTemperature": round(random.uniform(-15.0, 5.0), 2),
        "snowAccumulation": round(random.uniform(0.0, 20.0), 2),
        "externalTemperature": round(random.uniform(-25.0, 5.0), 2),
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ")
    }

def main():
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    print("Starting sensor for Fifth Avenue...")

    try:
        while True:
            telemetry = get_sensor_data()
            message = Message(str(telemetry))
            message.content_encoding = "utf-8"
            message.content_type = "application/json"
            client.send_message(message)
            print(f"Sent: {telemetry}")
            time.sleep(10)
    except KeyboardInterrupt:
        print("Fifth Avenue sensor stopped.")
    finally:
        client.disconnect()

if __name__ == "__main__":
    main()
