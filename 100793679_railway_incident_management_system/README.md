# Railway Incident Management System (RIMS) – CW2

**Module:** Object Oriented Analysis, Design and Implementation (7CS091)  
**Coursework:** CW2 – Backend Implementation 
**Student Name:**  Esomchukwu Ani
**Student Number:** 100793679  

---

## 1. Project Overview

This project implements the backend of a **Railway Incident Management System (RIMS)**, focusing on the **Track Obstruction Reporting Subsystem**.

The implementation is based on the UML class diagram developed in **CW1**, which has been refined in CW2 to incorporate object-oriented design patterns and improved responsibility separation.

The system supports:
- Reporting of railway track obstructions
- Automated notifications to relevant stakeholders
- Centralised task assignment
- Incident status tracking

---

## 2. Object-Oriented Design Patterns Used

### 2.1 Observer Pattern
- **Purpose:** To automatically notify system components when an incident status changes.
- **Implementation:**
  - `TrackIncident` acts as the Subject
  - `IncidentObserver` defines the observer interface
  - `ControlCentreSystem` and `MaintenanceResponseTeam` act as observers

### 2.2 Factory Pattern
- **Purpose:** To decouple incident creation from specific incident subclasses.
- **Implementation:**
  - `TrackIncidentFactory` creates instances of different incident types such as animal, vehicle, or tree obstructions.

### 2.3 Singleton Pattern
- **Purpose:** To ensure a single central authority for coordinating incidents.
- **Implementation:**
  - `ControlCentreSystem` uses a singleton approach to guarantee only one instance exists.

---

## 3. Project Structure

|── incident_observer.py    
├── track_incident.py   
├── track_incident_factory.py   
├── control_centre_system.py    
├── maintenance_response_team.py    
├── station_staff_member.py     
└── main.py


---

## 4. Running the System Demo

No graphical user interface is required for this coursework to be tested or executed, it runs on the console(CommandLine).

To run the backend demonstration:

```bash
python main.py