class IncidentObserver:
    """
    Observer interface for the Observer design pattern.
    Any class interested in incident updates must implement this interface.
    """

    def on_incident_update(self, incident):
        """
        Called automatically when an incident changes state.
        :param incident: TrackIncident object that triggered the update
        """
        raise NotImplementedError("Subclasses must implement this method")
