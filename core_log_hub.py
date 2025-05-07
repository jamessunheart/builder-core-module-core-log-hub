class CoreLogHub:
    """
    Centralized log system for Builder Core.
    Tracks diagnostics, execution, and reflection cycles.
    """

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
            "last_action": self.logs["executions"][-1] if self.logs["executions"] else None
        }