# NNPCL Maintenance Optimization Toolkit

A **Python-based toolkit** to optimize maintenance workflows for **pumps, compressors, valves, and pipelines**, inspired by the internship experience at **NNPCL Ejigbo Depot**. Focuses on:

- Predictive maintenance (vibration/thermal analysis).
- Automated maintenance logging and reporting.
- Root cause analysis (RCA) for recurring failures.
- Pump calibration and leak detection.

---

## **Features**


| Module                      | Description                                                             | Key Functions                               |
| --------------------------- | ----------------------------------------------------------------------- | ------------------------------------------- |
| `predictive_maintenance.py` | Detects anomalies in equipment data (vibration, temperature, pressure). | `detect_anomalies()`, `forecast_failures()` |
| `maintenance_logger.py`     | Automates maintenance logs and generates reports.                       | `add_entry()`, `generate_report()`          |
| `rca_analyzer.py`           | Structured RCA for equipment failures.                                  | `analyze()`, `generate_rca_report()`        |
| `pump_calibration.py`       | Simulates pump calibration and leak detection.                          | `detect_leak()`, `calibrate()`              |


---

## **Installation**

1. Clone the repository:
  ```bash
   git clone https://github.com/shamzdaf/nnpcl-maintenance-optimization.git
   cd nnpcl-maintenance-optimization
  ```
2. Install dependencies:
  ```bash
   pip install -r requirements.txt
  ```
   (Requires: `pandas`, `numpy`, `scikit-learn`)

---

## 📂 **Data Structure**

### **Input Data (`data/equipment_data.csv`)**


| Column        | Description            | Example            |
| ------------- | ---------------------- | ------------------ |
| `timestamp`   | Date/time of reading   | `2023-05-01 14:00` |
| `equipment`   | Equipment ID           | `Compressor_01`    |
| `vibration`   | Vibration level (mm/s) | `2.5`              |
| `temperature` | Temperature (°C)       | `75.0`             |
| `pressure`    | Pressure (bar)         | `5.2`              |


---

## **Usage Examples**

### **1. Predictive Maintenance**

```python
from scripts.predictive_maintenance import PredictiveMaintenance

pm = PredictiveMaintenance("data/equipment_data.csv")
anomalies = pm.detect_anomalies()
print("Potential failures:", anomalies)
```

### **2. Maintenance Logging**

```python
from scripts.maintenance_logger import MaintenanceLogger

logger = MaintenanceLogger()
logger.add_entry(
    equipment="Pump_03",
    action="Calibration",
    status="Completed",
    notes="Flow rate adjusted to 100 L/min; no leaks."
)
```

### **3. Root Cause Analysis**

```python
from scripts.rca_analyzer import RCAAnalyzer

rca = RCAAnalyzer()
causes = rca.analyze("pump", ["high_vibration", "leakage"])
print("Root causes:", causes)
```

### **4. Pump Calibration**

```python
from scripts.pump_calibration import PumpCalibrator

pump = PumpCalibrator(flow_rate=100, pressure=50)
leak = pump.detect_leak(measured_flow=95)
print("Leak detected:", leak)
```

---

## **Outputs**

- **Anomaly Reports**: CSV/JSON files with flagged equipment.
- **Maintenance Logs**: Structured JSON logs for auditing.
- **RCA Reports**: Markdown/PDF templates for failure analysis.
- **Calibration Certificates**: Validation reports for pumps.

---

## **Customization**

- **Add Equipment**: Extend `failure_modes` in `rca_analyzer.py`.
- **Improve Models**: Replace `IsolationForest` with LSTM for time-series forecasting.
- **Integrate IoT**: Connect to live sensors using `pymodbus` or `opcua`.
