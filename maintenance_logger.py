import json
from datetime import datetime

class MaintenanceLogger:
    def __init__(self, log_file="data/maintenance_logs.json"):
        self.log_file = log_file
        self.logs = self._load_logs()

    def _load_logs(self):
        try:
            with open(self.log_file, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def add_entry(self, equipment, action, status, notes=""):
        """Add a maintenance log entry."""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "equipment": equipment,
            "action": action,
            "status": status,
            "notes": notes
        }
        self.logs.append(entry)
        self._save_logs()

    def _save_logs(self):
        with open(self.log_file, "w") as f:
            json.dump(self.logs, f, indent=2)

    def generate_report(self, start_date, end_date):
        """Generate a report for a date range."""
        # Filter logs by date and return as DataFrame or Markdown
        pass

# Example usage
if __name__ == "__main__":
    logger = MaintenanceLogger()
    logger.add_entry(
        equipment="Compressor #1",
        action="Routine inspection",
        status="Completed",
        notes="Vibration levels normal; no leaks detected."
    )
