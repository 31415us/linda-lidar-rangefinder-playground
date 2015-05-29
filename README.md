# linda-lidar-rangefinder-playground
playground to play with some ideas for indoor localisation using a lidar range scanner

# visualization

additionally to the dependencies for the linda package, visualization depends
on:

* matplotlib for plotting simulated measurments
* pygame to visualize the robot moving

## measurement\_visualizer.py

usage:

```shell
python measurement_visualizer.py
```

you can move the robot with wasd keys
and toggle noise on measurements with n

plotting measurements is slow so we only replot them every few seconds

if measurement plot isn't shown immediately just move around the robot for
a few seconds

there is currently no collision detection implemented


