import time
import random
from azure.iot.device import IoTHubDeviceClient, Message

# Azure IoT Hub device connection string for the sensor at Fifth Avenue.
# This connects the script to the correct device in your IoT Hub instance.
CONNECTION_STRING = "HostName=IOT-hub-rideau-canal.azure-devices.net;DeviceId=sensor2-fiftheave;SharedAccessKey=cMI/ZmWlSPEvH6uQEYHr0offoG1DjbUjdIlT3nbjqm0="

# Simulates environmental data from the Fifth Avenue location.
def get_sensor_data():
    return {
        "location": "Fifth Avenue",  # Sensor location
        "iceThickness": round(random.uniform(5.0, 40.0), 2),           # Ice thickness in cm
        "surfaceTemperature": round(random.uniform(-15.0, 5.0), 2),    # Ice surface temperature in °C
        "snowAccumulation": round(random.uniform(0.0, 20.0), 2),       # Snow accumulation in cm
        "externalTemperature": round(random.uniform(-25.0, 5.0), 2),   # External air temperature in °C
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ")               # Current timestamp in ISO format
    }

# Main function to run the simulation and send data to Azure IoT Hub
def main():
    # Create an IoT Hub client using the connection string
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    print("Starting sensor for Fifth Avenue...")

    try:
        while True:
            # Generate the telemetry data
            telemetry = get_sensor_data()

            # Create a message to send to Azure IoT Hub
            message = Message(str(telemetry))
            message.content_encoding = "utf-8"
            message.content_type = "application/json"

            # Send the message
            client.send_message(message)
            print(f"Sent: {telemetry}")

            # Wait 10 seconds before sending the next reading
            time.sleep(10)
    except KeyboardInterrupt:
        # Gracefully stop the script if interrupted
        print("Fifth Avenue sensor stopped.")
    finally:
        # Disconnect the IoT Hub client
        client.disconnect()

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
