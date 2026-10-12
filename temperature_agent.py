# Lab 6 - Rabia Ashraf

# Task 3: Model-based reflex agent managing heaters in two rooms
model = {"Room1": None, "Room2": None}        # last known reading of each room
heater_on_count = {"Room1": 0, "Room2": 0}    # times the heater was turned ON


def temperature_agent(room, reading):
    """Update the internal model, then decide on an action."""
    model[room] = reading

    if reading == "Cold":
        heater_on_count[room] += 1
        return "Turn Heater ON"
    elif reading == "Hot":
        return "Turn Heater OFF"
    elif model["Room1"] == "Normal" and model["Room2"] == "Normal":
        return "All Rooms Comfortable - Idle"
    else:
        return "Move to Other Room to Check"


percept_sequence = [("Room1", "Cold"), ("Room1", "Normal"),
                    ("Room2", "Hot"), ("Room2", "Normal")]

print("Room\tReading\tAction\t\t\t\tModel")
for room, reading in percept_sequence:
    action = temperature_agent(room, reading)
    print(f"{room}\t{reading}\t{action:<30}\t{model}")
print("Heater ON count:", heater_on_count)