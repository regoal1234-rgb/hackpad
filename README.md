# Junsuh's macropad
Hello! This is my submission for hackpad! This was made for Hackpad v1.

## Features
- A big 0.96" OLED screen
- 16x whole cherry keys 
- kmk firmware! Control your mouse with this macropad

## PCB
Here are pictures of my pcb:

| **Schematic** | **PCB** |
|---------------|---------|
|![img](https://github.com/regoal1234-rgb/img/blob/408740627681958383da83e0f286efe40ce83e7d/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202025-12-18%20000135.png)|
![img](https://github.com/regoal1234-rgb/img/blob/aed19abdb678c6f83908cacce41fac740f18d572/fffinal.png)|



[x] I ran DRC and there are 0 errors

## CAD
Designed using FreeCAD! It was painful. Be glad you have the current guide, I spent 10+ hours figuring out how to do everything correctly (and even like this I still did stupid stuff).

![img](https://github.com/regoal1234-rgb/img/blob/aed19abdb678c6f83908cacce41fac740f18d572/fffinal.png)

Everything fits together with 4 m3 screws and bolts

## Firmware

I wrote the firmware using kmk, you can see it inside the repo. It can be used to control your mouse!

## Notes
Making the pad was fun enthough i went through hardships. Ended up learning how to use OpenSCAD and FreeCAD.

## BOM
- 1 Seeed XIAO RP2040
- 15x [MX-Style switches]
- 15x Through-hole 1N4148 Diodes
- 1x 0.91 inch OLED displays (5V VCC, 3.3V logic, I2C)
- 1x 3D PRINTED CASE
- 15x Blank DSA keycaps
- 1x EC11 Rotary encoders
- 4x M3x16mm screws
- 4x M3x5mx4mm heatset inserts
