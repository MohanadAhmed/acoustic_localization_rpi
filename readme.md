# Acoustic Localization using Ultrasound Signals on Raspberry Pi Controllers

This repository contains codes for the usage of raspberry pi 3 b+ kits for acoustic localization.
The distance from time of flight equation is given by :

$$ \hat{d} = \frac{t_r - t_x}{c_{sound}} $$

Where:

  - $c_{sound}$ : Speed of sound
  - $t_r$ : time of reception
  - $t_x$ : time of transmission
  - $d$ : distance measurement
  
Note that the timing quantities must be measured by the same and clock and will experience various measurement errors. Much of ranging and localization is about estimating and dealing with these errors.
