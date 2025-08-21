# solar_system_newtonian_dynamics
Simulates Newtonian N-body interaction between objects in the solar system with a Newmark method, according to NASA-given starting positions

## Installation

Create and/or activate a virtual environment of your choice. Clone the repository in the folder of your choice using:
```
git clone git@github.com:rcapillon/solar_system_newtonian_dynamics.git
```
Then install the package using:
```
cd solar_system_newtonian_dynamics/
pip install .
```

## Usage
The example script in the repository simulates the sun and the 8 planets of the solar system for a little more than
2 martian years and makes a video showing the first 4 planets (Mercury, Venus, Earth and Mars) and the sun.

This example code can be tinkered with in order to simulate longer periods, have more time-steps for precision, 
and show more or less of the planets.

## Example animation
Roughley 2 martian years:
<img src="https://github.com/rcapillon/solar_system_newtonian_dynamics/blob/main/readme_files/2_mars_years.gif" width="400">

## Intended features
- Fetch initial planets' positions and velocities directly from NASA HORIZONS using their API, allowing the user to
simulate from a given time, for a given period, then maybe fetch actual data at the end time of the simulation and 
calculate the error.