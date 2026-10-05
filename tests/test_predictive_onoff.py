from controllers.predictive_onoff import PredictiveOnOff

def test_predictive_turns_off_early():
    # setpoint 21, deadband 1 -> upper=21.5
    ctrl = PredictiveOnOff(setpoint=21.0, deadband=1.0, tau=30.0, state=1)
    dt = 1.0
    ctrl.update(20.8, dt)
    state = ctrl.update(21.2, dt)  # rising fast -> predicted > upper -> OFF
    assert state == 0, "Controller should turn off when the predicted temperature exceeds the upper threshold."

def test_predictive_on_when_falling():
    ctrl = PredictiveOnOff(setpoint=21.0, deadband=1.0, tau=30.0, state=0)
    dt = 1.0
    ctrl.update(21.0, dt)  # init
    state = ctrl.update(20.0, dt)  # falling -> predicted low -> ON
    assert state == 1, "Controller should turn on when the predicted temperature falls below the lower threshold."
