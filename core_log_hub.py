class CoreLogHub:
    def __init__(self):
        self.logs = {
            "diagnostics": [],
            "plans": [],
            "executions": []
        }

    def record_diagnostic(self, report):
        self.logs["diagnostics"].append(report)

    def record_plan(self, plan):
        self.logs["plans"].append(plan)

    def record_execution(self, result):
        self.logs["executions"].append(result)

    def get_all_logs(self):
        return self.logs

    def summarize(self):
        return {
            "total_cycles": len(self.logs["executions"]),
            "diagnostics": len(self.logs["diagnostics"]),
            "plans_made": len(self.logs["plans"]),
            "last_action": self.logs["executions"][-1] if self.logs["executions"] else None,
            "coverage": {
                "self-awareness": len(self.logs["diagnostics"]) > 0,
                "strategic_planning": len(self.logs["plans"]) > 0,
                "autonomy": len(self.logs["executions"]) > 0
            }
        }

# Instantiate and summarize current metrics
hub = CoreLogHub()
print("Core Metrics:", hub.summarize())