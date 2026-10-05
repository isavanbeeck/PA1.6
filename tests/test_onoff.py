from controllers.onoff import OnOffThermostat

def test_on_below_lower():
    t = OnOffThermostat(setpoint=21.0, deadband=1.0)
    t.state = 0
    assert t.update(20.4) == 1, "Thermostat should turn on below the lower threshold"

def test_off_above_upper():
    t = OnOffThermostat(setpoint=21.0, deadband=1.0)
    t.state = 1
    assert t.update(21.6) == 0, "Thermostat should turn off above the upper threshold"

def test_hold_inside_band():
    t = OnOffThermostat(setpoint=21.0, deadband=1.0)
    t.state = 1
    assert t.update(21.0) == 1, "Thermostat should remain on when temperature is inside the deadband"
    t.state = 0
    assert t.update(21.0) == 0, "Thermostat should remain off when temperature is inside the deadband"

def test_safety_cutoff():
    t = OnOffThermostat(setpoint=21.0, deadband=1.0, safety_high=25.0)
    t.state = 1
    assert t.update(25.0) == 0, "Thermostat should shut off at the safety high cutoff"
