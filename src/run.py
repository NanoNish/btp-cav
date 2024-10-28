import traci
import time

import sys
sys.path.append('C:/Program Files (x86)/Eclipse/Sumo/tools')

# Start SUMO with TraCI
sumoCmd = ["sumo-gui", "-c", "simulation.sumocfg", "--start"]
try:
    traci.start(sumoCmd)
except Exception as e:
    print(e)


time.sleep(10)

try:
    # step = 0
    # while traci.simulation.getMinExpectedNumber() > 0:
    #     traci.simulationStep()
        
    #     # Example: Detect vehicles on the on-ramp and monitor merging
    #     for vehicle_id in traci.vehicle.getIDList():
    #         edge_id = traci.vehicle.getRoadID(vehicle_id)
            
    #         if edge_id == "on_ramp":
    #             # Check if the vehicle is about to merge and adjust speed if needed
    #             speed = traci.vehicle.getSpeed(vehicle_id)
    #             print(f"Vehicle {vehicle_id} is on the ramp with speed {speed}")
                
    #             # Example behavior: Adjust speed to help with merging (if needed)
    #             traci.vehicle.setSpeed(vehicle_id, min(speed + 2, 20))  # Gradual speed increase
        
    #     step += 1
    for step in range(10):
        traci.simulationStep()
        print(f"Simulation step {step} completed")

finally:
    # Close TraCI connection
    traci.close()
