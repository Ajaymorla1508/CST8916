# Rideau Canal Skateway Real-Time Monitoring System

## 📘 Project Overview

The **Rideau Canal Skateway**, located in Ottawa, is the world's longest naturally frozen skating rink. To ensure public safety, continuous monitoring of key factors like ice thickness, temperature, and snow accumulation is essential. This project simulates IoT sensors positioned at various points along the canal to monitor real-time environmental data.

Using an end-to-end Azure data pipeline, the system collects data from simulated sensors, processes it in real-time, and stores it for long-term analysis. The processed data enables the **National Capital Commission (NCC)** to quickly assess and respond to potential safety concerns.

---

## 🏗️ System Architecture

![Architecture Diagram](https://github.com/Saikarthick07/Rideau-Canal-Project---Real-time-Application/blob/main/Images/ArchitectureDiagram_RideauCanal.png)

### Key System Components:

1. **Simulated IoT Sensors**: These sensors generate environmental data at three locations along the canal and send it to the cloud.
2. **Azure IoT Hub**: Collects real-time data from the simulated IoT devices.
3. **Azure Stream Analytics**: Processes and aggregates incoming sensor data in real-time.
4. **Azure Blob Storage**: Stores the processed data for further analysis.

---

## 🔧 Implementation Details

### 📡 IoT Sensor Simulation

- The `RealTimeProject/sensor1.py` script simulates sensors located at:
  - **Dow's Lake**
  - **Fifth Avenue**
  - **National Arts Centre (NAC)**

- The script generates JSON data every **5 seconds**, which includes details such as ice thickness, temperature, snow accumulation, and timestamp. The data is sent to **Azure IoT Hub**.

Example JSON payload:

```json
{
  "location": "Dow's Lake",
  "iceThickness": 27,
  "surfaceTemperature": -1,
  "snowAccumulation": 8,
  "externalTemperature": -4,
  "timestamp": "2024-11-23T12:00:00Z"
}
