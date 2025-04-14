import time
import random
from azure.iot.device import IoTHubDeviceClient, Message

# Connection string to Azure IoT Hub for the NAC device.
CONNECTION_STRING = "HostName=IOT-hub-rideau-canal.azure-devices.net;DeviceId=sensor3-nac;SharedAccessKey=KYKcWFa6sVoDptEqa+DqAgl9w/kFZ87qlvDEEDMoHXI="

# Function to simulate sensor data for NAC
def get_sensor_data():
    return {
        "location": "NAC",  # Device location (National Arts Centre)
        "iceThickness": round(random.uniform(5.0, 40.0), 2),           # Simulated ice thickness in cm
        "surfaceTemperature": round(random.uniform(-15.0, 5.0), 2),    # Surface temperature of ice
        "snowAccumulation": round(random.uniform(0.0, 20.0), 2),       # Snow accumulation on the surface
        "externalTemperature": round(random.uniform(-25.0, 5.0), 2),   # External weather temperature
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ")               # ISO-formatted UTC timestamp
    }

# Main logic to run the NAC sensor simulation
def main():
    # Create a device client from the connection string
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    print("Starting sensor for NAC...")

    try:
        while True:
            # Generate simulated telemetry data
            telemetry = get_sensor_data()

            # Create a message object with the telemetry data
            message = Message(str(telemetry))
            message.content_encoding = "utf-8"
            message.content_type = "application/json"

            # Send message to Azure IoT Hub
            client.send_message(message)
            print(f"Sent: {telemetry}")

            # Wait 10 seconds before sending the next message
            time.sleep(10)
    except KeyboardInterrupt:
        # Stop the script when the user presses Ctrl+C
        print("NAC sensor stopped.")
    finally:
        # Disconnect the IoT client gracefully
        client.disconnect()

# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()
