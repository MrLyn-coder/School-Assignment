from incident_observer import IncidentObserver


class MaintenanceResponseTeam(IncidentObserver):
    """
    Represents a railway maintenance response team.
    Observes incidents and resolves assigned tasks.
    """

    def __init__(self, team_identifier):
        self.team_identifier = team_identifier  # Team reference ID

    def on_incident_update(self, incident):
        """Receive notification when an incident state changes."""
        print(
            f"[MAINTENANCE TEAM {self.team_identifier}] "
            f"Received update for  {incident.incident_type} incident at {incident.location}"
        )

    def handle_incident(self, incident):
        """Resolve the assigned incident."""
        print(
            f"[MAINTENANCE TEAM {self.team_identifier}] "
            f"Responding to incident {incident.incident_id}"
        )
        incident.update_status("Resolved")