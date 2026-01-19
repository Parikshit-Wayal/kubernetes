| Probe Type | Purpose | Action on Failure |
| :--- | :--- | :--- |
| **1. Liveness Probe** | Detects if the application is **alive** and running. | The container is **restarted**. |
| **2. Readiness Probe** | Detects if the application is **ready to serve traffic**. | The Pod is **removed from Service endpoints** (no traffic is routed to it). |
| **3. Startup Probe** | Prevents premature restarts for **slow-booting** applications. | The container is **restarted** (only after the initial failure period/threshold). |

<br>

----


| Deployment Strategy | Purpose | Traffic Behavior |
| :--- | :--- | :--- |
| **1. Rolling Update** | Updates the application **gradually with zero downtime**. | Traffic is **shifted incrementally** from old Pods to new Pods. |
| **2. Blue-Green Deployment** | Runs **two identical environments** (Blue = current, Green = new). | Traffic is **switched instantly** from Blue to Green. |
| **3. Canary Deployment** | Tests a new version with a **small subset of users** before full rollout. | Traffic is **partially routed** to the new version, then increased gradually. |
