# Written Justification: Municipal Infrastructure Damage Reporting App

**Name: Dharani S**
**SRN: PES2UG24CS157**
**Section: C**
**Architecture Selection:** We chose **Microservices Architecture** for the Municipal Infrastructure Damage Reporting System.
## Reason 1: Independent Scaling for Variable Load
Photo upload and EXIF GPS extraction are CPU- and I/O-intensive operations that spike during peak reporting hours, while GIS routing and notification traffic stay comparatively flat. A microservices architecture lets the Photo/GPS Service scale independently without over-provisioning the entire system, keeping the citizen-facing app responsive under load.

## Reason 2: Fault Isolation Across Independent Concerns
The system spans distinct, loosely related responsibilities, photo processing, GIS lookup, ticket dispatch, and engineer notification. If the Notification Service fails, citizens can still submit reports and tickets still get created and persisted; only the engineer alert is delayed. A monolithic or tightly layered design would risk a single failure cascading across all functionality.

## Security Advantage
Each service exposes only the interface required for its function, the GIS Routing Service never has access to raw photo data, and the Notification Service never touches the ticket database directly. This minimizes the attack surface per service and limits the blast radius of a compromised component.

## Performance Benefit
Independent deployment and scaling mean the Report API and offline-sync path remain responsive even when the GIS Routing or Notification services are under heavy load. This directly supports NFR-001, which requires offline report drafting with reliable auto-sync once connectivity resumes.