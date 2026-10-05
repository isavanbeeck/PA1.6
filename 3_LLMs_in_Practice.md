# Programming a Thermostat with AI

In this assignment, you will create a thermostat program that controls the temperature of a room. Code is provided that simulates the temperature evolution in the room for a given scenario in interaction with a heating system. However, the controllers for the thermostat and models for the room and environment are not yet implemented, so the simulation will not work as expected. Your task is to implement the controllers and any auxiliary functions needed to make the simulation work correctly.

Your goal is to use AI to help you write the code for the thermostat. This project introduces you to the typical workflow when working on larger programming projects that contain multiple files and modules. In these cases, copy-pasting code snippets is far less effective than working with an LLM integrated into your programming environment. We highly recommend using GitHub Copilot.

## Assignment Description
A thermostat is a device that regulates the temperature of a system so that the system's temperature is maintained near a desired setpoint. The thermostat will control the temperature of a room by turning a heater on and off based on the current temperature and a desired setpoint. There are two main strategies for controlling the heater: a simple on/off controller and a predictive on/off controller. You will implement the on/off controller (the predictive on/off controller is implemented for you) and compare their performance. This requires you to implement some auxiliary functions in other modules as well.

In this simulation, the room temperature is affected by the heater and the outside temperature. Moreover, there is a "door opening" event that substantially drops the temperature. You can control all of these factors in the scenario files located in the `scenarios` folder. Two example scenarios are provided already: `door_open.yaml` includes a door opening event using a simple onoff thermostat, and `cold_morning.yaml` provides an especially cold morning with a predictive onoff thermostat.

To run the simulation, you need to call the provided `main.py` file with a specific scenario as input. You do this in the CLI with this command:

```bash
python main.py --scenario scenarios/door_open.yaml # Example scenario 1
python main.py --scenario scenarios/cold_morning.yaml # Example scenario 2
```

You can also create your own scenarios by copying and modifying the provided YAML files.
To do this, create copy one of the YAML files in the `scenarios` folder and modify the parameters as desired. The config file has the following structure:

```yaml
env:
  base: # Base outside temperature (C)
  amplitude: # Amplitude of outside temperature variation (C)
  period_s: # Period of outside temperature variation (s)
  door_drop_C: # Temperature drop when door opens (C)
  door_start_s: # Time when door opens (s)
  door_duration_s: # Duration of door opening (s)

sensor:
  sigma: # Standard deviation of sensor noise (C)
  bias: # Bias of sensor (C)
  dropout_prob: # Probability of sensor dropout (0-1)

controller:
  type: # Type of controller (onoff or predictive_onoff)
  setpoint: # Desired temperature setpoint (C)
  deadband: # Deadband around setpoint (C)
  tau: # Lookahead horizon for predictive_onoff (s)
  safety_high: # Safety high temperature limit (C)

model:
  R: # Thermal resistance (C/W)
  C: # Thermal capacitance (J/C)
  P: # Heater power (W)
  process_sigma: # Standard deviation of process noise (C)

sim:
  dt: # Simulation time step (s)
  duration_s: # Duration of simulation (s)
  seed: 123 # Random seed for reproducibility of random events
  init_T: # Initial room temperature (C)
```

## Task 1 Familiarize yourself with the codebase

Use AI to familiarize yourself with the provided codebase. Understand how the different modules interact with each other. Also use it to understand the file structure.

> Example prompt: "Explain the file structure of this project's main.py and how the different modules interact with each other."

## Task 2 Implement the `onoff` controller in `assignment-files/controllers/onoff.py`

This controller should turn the heater on when the temperature is below the setpoint minus half the deadband, and turn it off when the temperature is above the setpoint plus half the deadband.

> Example prompt: "How does the onoff controller work and how can I implement it in Python?"

## Task 3.additional Implement all auxiliary functions in the other modules. 

Implement all auxiliary functions in the other modules. Use AI to help you understand the purpose of each function and how to implement it.

> Example prompt: "What is the purpose of the `update` function in `assignment-files/sensors/filters.py`?"

*Please note that not all implementation are required to pass the assignment, as soon as you've passed the tests you passed the assignment. However, we welcome you to implement as much as you like.*

## Task 4.additional Test your implementation

Test your implementation by running the provided scenarios and checking the plots generated in the `outputs/figures` folder. 

## Task 5.6.additional Modify the scenarios

Use AI to help you modify the scenarios and make the heater more sensitive, more powerful, or to create more challenging scenarios. Then investigate how the duty cycle and temperature regulation change.

> Example prompt: "How can I modify the `cold_morning.yaml` scenario to make the door open event more impactful?"

## Task 6.7.additional Implement Monte Carlo simulations to estimate the uncertainty in the temperature regulation.

This involves running multiple simulations with different random seeds and analyzing the results. Use AI to help you understand how to implement this and analyze the results. This will involve providing the entire project as context, so it is especially useful to use an integrated LLM like GitHub Copilot.

> Example prompt: "How can I implement Monte Carlo simulations in the thermostat?"

> By Tom van Woudenberg and Stanislaw Ostyk-Narbutt, Delft University of Technology. CC BY 4.0, more info [on the Credits page of Workbook](https://mude.citg.tudelft.nl/workbook-2025/credits.html).
