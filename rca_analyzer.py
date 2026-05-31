class RCAAnalyzer:
    def __init__(self):
        self.failure_modes = {
            "pump_failure": ["bearing_wear", "seal_leakage", "misalignment"],
            "valve_failure": ["corrosion", "actuator_malfunction"],
        }

    def analyze(self, equipment, symptoms):
        """Identify potential root causes."""
        causes = []
        for mode, possible_causes in self.failure_modes.items():
            if equipment in mode:
                causes.extend(possible_causes)
        return list(set(causes))  # Remove duplicates

    def generate_rca_report(self, equipment, symptoms, root_cause, recommendations):
        """Generate an RCA report template."""
        report = f"""
        # Root Cause Analysis Report
        **Equipment:** {equipment}
        **Symptoms:** {', '.join(symptoms)}
        **Root Cause:** {root_cause}
        **Recommendations:** {', '.join(recommendations)}
        """
        return report

# Example usage
if __name__ == "__main__":
    rca = RCAAnalyzer()
    causes = rca.analyze("pump", ["high_vibration", "leakage"])
    print("Potential root causes:", causes)
