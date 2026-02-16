class StationStaffMember:
    """
    Represents a station staff member responsible for reporting incidents.
    """

    def report_track_incident(self, incident):
        """Report a newly detected track incident."""
        print(
            f"[STATION STAFF]  {incident.incident_type} Incident {incident.incident_id} "
            f"reported at {incident.location}"
        )
        incident.notify_observers()