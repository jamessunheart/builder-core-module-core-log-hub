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
            "last_action": self.logs["executions"][-1] if self.logs["executions"] else None
        }

# Simulate log of current cycle
from self_diagnostic_engine import SelfDiagnosticEngine
from meta_reflection_planner import MetaReflectionPlanner
from autopilot_priority_executor import AutopilotPriorityExecutor

log_hub = CoreLogHub()
diagnostics = SelfDiagnosticEngine().run_diagnostics()
plan = MetaReflectionPlanner().generate_improvement_plan(diagnostics)
result = AutopilotPriorityExecutor().run_autopilot_cycle()

log_hub.record_diagnostic(diagnostics)
log_hub.record_plan(plan)
log_hub.record_execution(result)

print("Summary:", log_hub.summarize())