# AI Vector Field Navigation
____________________________


This script provides navigation to an autonomous system in just a few simple steps...

1) Increase <b>attractor_field_strength</b> until the robot can reach the goal.
      - this adjusts the heading angle and vector length

2) Put goal behind obstacle and increase rep_field_strength until the robot avoids obstacle.
      - remember to set the size of the object (# rep_field_radius), also, 
        at what distace the robot should start avoiding the obstacle (# rep_field_area).
