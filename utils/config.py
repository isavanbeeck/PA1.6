from dataclasses import dataclass
import yaml

@dataclass
class EnvConfig:
    base: float = 5.0
    amplitude: float = 2.0
    period_s: float = 7200.0
    door_drop_C: float = 5.0
    door_start_s: float = 1200.0
    door_duration_s: float = 120.0

@dataclass
class SensorConfig:
    sigma: float = 0.2
    bias: float = 0.3
    dropout_prob: float = 0.02

@dataclass
class ControllerConfig:
    type: str = 'predictive_onoff'  # 'onoff' or 'predictive_onoff'
    setpoint: float = 21.0
    deadband: float = 1.0
    tau: float = 30.0
    safety_high: float = 26.0

@dataclass
class ModelConfig:
    R: float = 0.5
    C: float = 10000.0
    P: float = 200.0
    process_sigma: float = 0.0

@dataclass
class SimConfig:
    dt: float = 1.0
    duration_s: float = 3600.0
    seed: int = 42
    init_T: float = 18.0

@dataclass
class Config:
    env: EnvConfig
    sensor: SensorConfig
    controller: ControllerConfig
    model: ModelConfig
    sim: SimConfig

def load_config(path: str) -> Config:
    with open(path, "r") as f:
        raw = yaml.safe_load(f)
    env = EnvConfig(**raw.get("env", {}))
    sensor = SensorConfig(**raw.get("sensor", {}))
    controller = ControllerConfig(**raw.get("controller", {}))
    model = ModelConfig(**raw.get("model", {}))
    sim = SimConfig(**raw.get("sim", {}))
    return Config(env=env, sensor=sensor, controller=controller, model=model, sim=sim)
