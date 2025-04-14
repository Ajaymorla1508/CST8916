import time
import random
from azure.iot.device import IoTHubDeviceClient, Message

# Connection string for the IoT device registered in Azure IoT Hub.
# This string uniquely identifies your device and allows it to communicate with the IoT Hub.
CONNECTION_STRING = "HostName=IOT-hub-rideau-canal.azure-devices.net;DeviceId=sensor1-dows;SharedAccessKey=9/8dmTD+bPile7AcQ7LupmTbBCMzHg8BG0QlmXBwdMs="

# Function to simulate environmental sensor data at Dow's Lake.
def get_sensor_data():
    return {
        "location": "Dow's Lake",
        "iceThickness": round(random.uniform(5.0, 40.0), 2),           # Simulated ice thickness in cm
        "surfaceTemperature": round(random.uniform(-15.0, 5.0), 2),    # Surface temperature in Celsius
        "snowAccumulation": round(random.uniform(0.0, 20.0), 2),       # Snow accumulation in cm
        "externalTemperature": round(random.uniform(-25.0, 5.0), 2),   # Ambient external temperature in Celsius
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ")               # Current timestamp in ISO 8601 format
    }

# Main function to initialize the IoT client and send telemetry data
def main():
    # Create a client instance using the connection string
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    print("Starting sensor for Dow's Lake...")

    try:
        while True:
            # Generate simulated sensor readings
            telemetry = get_sensor_data()

            # Create a message with the telemetry data
            message = Message(str(telemetry))
            message.content_encoding = "utf-8"  # Ensure UTF-8 encoding
            message.content_type = "application/json"  # Set content type to JSON

            # Send the message to Azure IoT Hub
            client.send_message(message)
            print(f"Sent: {telemetry}")  # Log the data to console

            # Wait 10 seconds before sending the next message
            time.sleep(10)
    except KeyboardInterrupt:
        # Gracefully handle termination with Ctrl+C
        print("Dow's Lake sensor stopped.")
    finally:
        # Disconnect the client when done
        client.disconnect()

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
