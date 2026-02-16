from incident_observer import IncidentObserver


class ControlCentreSystem(IncidentObserver):
    """
    Represents the central railway control centre.
    Implements the Singleton design pattern to ensure a single instance.
    """

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ControlCentreSystem, cls).__new__(cls)
        return cls._instance

    def on_incident_update(self, incident):
        """Receive incident updates via the Observer pattern."""
        print(
            f"[CONTROL CENTRE] {incident.incident_type} Incident {incident.incident_id} "
            f"at {incident.location} is now '{incident.status}'"
        )

    def assign_response_task(self, response_team, incident):
        """Assign an incident to a maintenance response team."""
        response_team.handle_incident(incident)