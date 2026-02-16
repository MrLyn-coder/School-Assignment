from track_incident_factory import TrackIncidentFactory
from control_centre_system import ControlCentreSystem
from maintenance_response_team import MaintenanceResponseTeam
from station_staff_member import StationStaffMember


# Entry point demonstrating the full system workflow
if __name__ == "__main__":
    # Create system actors
    control_centre = ControlCentreSystem()
    maintenance_team = MaintenanceResponseTeam("MT-01")
    station_staff = StationStaffMember()

    # Create an incident using the Factory pattern
    incident = TrackIncidentFactory.create_track_incident(
        incident_type="vehicle",
        incident_id=301,
        location="Track Section C"
    )

    # Register observers (Observer pattern)
    incident.attach_observer(control_centre)
    incident.attach_observer(maintenance_team)

    print("\n--- INCIDENT REPORTED ---")
    station_staff.report_track_incident(incident)

    print("\n--- RESPONSE ASSIGNED ---")
    control_centre.assign_response_task(maintenance_team, incident)

    print("\n--- FINAL INCIDENT STATUS ---")
    print(f"Incident {incident.incident_id} status: {incident.status}")