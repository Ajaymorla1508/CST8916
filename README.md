# Rideau Canal Skateway Monitoring System

## Scenario Description

The Rideau Canal Skateway, a UNESCO World Heritage Site and the world's longest naturally frozen skating rink, requires continuous monitoring to ensure the safety of skaters. Key environmental parameters such as ice thickness, surface temperature, snow accumulation, and external weather conditions must be assessed in real time to determine skating conditions.

This project simulates IoT sensors at three key locations along the canal—Dow's Lake, Fifth Avenue, and the National Arts Centre (NAC). The solution uses an end-to-end Azure-based pipeline to collect, process, and store data for further analysis by the National Capital Commission (NCC).

---

## System Architecture

![Architecture Diagram](https://github.com/Ajaymorla1508/CST8916/blob/main/Images/Architecture-diagram.png)

### Data Flow:
1. Simulated IoT sensors generate and send JSON data to Azure IoT Hub.
2. Azure IoT Hub receives the data and forwards it to Azure Stream Analytics.
3. Azure Stream Analytics processes the data using SQL-based queries.
4. The processed output is stored in Azure Blob Storage in JSON format.

---

## Implementation Details

### IoT Sensor Simulation
- Three Python scripts simulate sensors at:
  - Dow's Lake
  - Fifth Avenue
  - NAC
- Each script sends data every 10 seconds with the following payload structure:

```json
{
  "location": "Dow's Lake",
  "iceThickness": 27,
  "surfaceTemperature": -1,
  "snowAccumulation": 8,
  "externalTemperature": -4,
  "timestamp": "2024-11-23T12:00:00Z"
}
```
![Architecture Diagram](https://github.com/Ajaymorla1508/CST8916/blob/main/Images/IOT%20sensor%20outputs.png)

- The scripts use the Azure IoT SDK to authenticate with the IoT Hub and push telemetry.

### Azure IoT Hub Configuration
- An IoT Hub instance was created through the Azure portal.
- Devices for each location were registered.
- Primary connection strings were copied and embedded into the respective Python scripts.
- The IoT Hub routing is configured to direct incoming telemetry to Stream Analytics.



### Azure Stream Analytics Job
- A single job ingests data from the IoT Hub.
- SQL query used:

```sql
SELECT
  location,
  AVG(iceThickness) AS avgIceThickness,
  MAX(snowAccumulation) AS maxSnow,
  System.Timestamp AS windowEnd
INTO
  [BlobStorageOutput]
FROM
  [IoTHubInput]
TIMESTAMP BY timestamp
GROUP BY
  TumblingWindow(minute, 1), location
```
![Architecture Diagram](https://github.com/Ajaymorla1508/CST8916/blob/main/Images/Query.png)
- Input: Azure IoT Hub
![Architecture Diagram](https://github.com/Ajaymorla1508/CST8916/blob/main/Images/input.png)
- Output: Azure Blob Storage
![Architecture Diagram](https://github.com/Ajaymorla1508/CST8916/blob/main/Images/output.png)
### Azure Blob Storage
- Output container named `processed-data`
- Data organized by date and time:
  - `processed-data/location/yyyy/mm/dd/hh/*.json`
- Format: JSON

---
![Architecture Diagram](https://github.com/Ajaymorla1508/CST8916/blob/main/Images/output2.png)

## Usage Instructions

### Running the IoT Sensor Simulation
1. Clone the GitHub repository.
2. Navigate to the sensor simulation directory.
3. Create and activate a virtual environment:
   ```bash
   python3 -m venv myenv
   source myenv/bin/activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the scripts:
   ```bash
   python sensor_dows_lake.py
   python sensor_fifth_avenue.py
   python sensor_nac.py
   ```

### Configuring Azure Services

#### IoT Hub:
- Create an IoT Hub and register three devices.
- Copy the device connection strings into the simulation scripts.

#### Stream Analytics:
- Create a job, set IoT Hub as input and Blob Storage as output.
- Apply the provided SQL query.

### Accessing Stored Data
1. Open Azure Blob Storage.
2. Navigate to the `processed-data` container.
3. Browse or download the JSON files.

---

## 🎯 Results

- Aggregated outputs like average ice thickness and maximum snow depth for every 5 minutes were computed.
- Data stored in structured JSON files per location.
- Example insights:
  ```json
  {
  {"location":"Dow's Lake","windowEnd":"2025-04-14T21:45:00.0000000Z","avgIceThickness":22.82407407407408,"maxSnowAccumulation":19.64}
{"location":"NAC","windowEnd":"2025-04-14T21:45:00.0000000Z","avgIceThickness":24.413703703703707,"maxSnowAccumulation":19.97}
{"location":"Fifth Avenue","windowEnd":"2025-04-14T21:45:00.0000000Z","avgIceThickness":22.637857142857143,"maxSnowAccumulation":17.98}
  }
  ```

---

## Reflection

During the implementation, key challenges included:
- Managing separate environments for each simulated sensor.
- Ensuring correct message routing between IoT Hub and Stream Analytics.
- Debugging query logic and formatting for real-time processing.

Through troubleshooting and iterative testing, a robust and scalable real-time monitoring pipeline was established using Azure's powerful suite of tools.

