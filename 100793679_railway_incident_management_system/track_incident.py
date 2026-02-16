from incident_observer import IncidentObserver


class TrackIncident:
    """
    Base class representing a railway track incident.
    Acts as the Subject in the Observer design pattern.
    """

    def __init__(self, incident_id, location):
        self.incident_id = incident_id          # Unique identifier for the incident
        self.location = location                # Track location of the incident
        self.status = "Reported"                # Current status of the incident
        self._observers = []                    # Registered observers

    def attach_observer(self, observer: IncidentObserver):
        """Register an observer to receive incident updates."""
        self._observers.append(observer)

    def notify_observers(self):
        """Notify all registered observers of a state change."""
        for observer in self._observers:
            observer.on_incident_update(self)

    def update_status(self, new_status):
        """
        Update the incident status and notify observers.
        :param new_status: New status value (e.g. In Progress, Resolved)
        """
        self.status = new_status
        self.notify_observers()


# ---- Specialized Incident Types (Inheritance) ----

class AnimalTrackIncident(TrackIncident):
    """Represents an animal-related track obstruction."""

    def __init__(self, incident_id, location):
        super().__init__(incident_id, location)
        self.incident_type = "Animal Obstruction"


class VehicleTrackIncident(TrackIncident):
    """Represents a vehicle-related track obstruction."""

    def __init__(self, incident_id, location):
        super().__init__(incident_id, location)
        self.incident_type = "Vehicle Obstruction"


class TreeTrackIncident(TrackIncident):
    """Represents a fallen tree track obstruction."""

    def __init__(self, incident_id, location):
        super().__init__(incident_id, location)
        self.incident_type = "Tree Obstruction"