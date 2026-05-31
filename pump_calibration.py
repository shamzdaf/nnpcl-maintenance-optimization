class PumpCalibrator:
    def __init__(self, flow_rate, pressure):
        self.flow_rate = flow_rate
        self.pressure = pressure
        self.leak_threshold = 0.1  # 10% deviation = potential leak

    def detect_leak(self, measured_flow):
        """Detect leaks based on flow rate deviation."""
        deviation = abs(measured_flow - self.flow_rate) / self.flow_rate
        return deviation > self.leak_threshold

    def calibrate(self, target_flow):
        """Adjust pump to match target flow rate."""
        # Placeholder: PID controller logic
        return f"Pump calibrated to {target_flow} L/min."

# Example usage
if __name__ == "__main__":
    pump = PumpCalibrator(flow_rate=100, pressure=50)
    leak_detected = pump.detect_leak(measured_flow=95)
    print("Leak detected:", leak_detected)
