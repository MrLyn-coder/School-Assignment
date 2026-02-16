from track_incident import (
    AnimalTrackIncident,
    VehicleTrackIncident,
    TreeTrackIncident
)


class TrackIncidentFactory:
    """
    Factory class responsible for creating TrackIncident objects.
    Implements the Factory design pattern.
    """

    @staticmethod
    def create_track_incident(incident_type, incident_id, location):
        """
        Create and return a specific TrackIncident subclass.
        :param incident_type: Type of incident (animal, vehicle, tree)
        """
        if incident_type == "animal":
            return AnimalTrackIncident(incident_id, location)
        elif incident_type == "vehicle":
            return VehicleTrackIncident(incident_id, location)
        elif incident_type == "tree":
            return TreeTrackIncident(incident_id, location)
        else:
            raise ValueError("Unsupported track incident type")
