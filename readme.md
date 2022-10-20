# Polar Polynomial Interpolation
![image of output equasions](https://i.imgur.com/6wPQ4FH.png)<br>
[Black is the plotted points. Blue is a Cartesian polynomial interpolation. Purple is polynomial interpolation using the Polar coordinates. Red is a spiral-style polynomial interpolation using modified Polar coordinates.]

do not steal please i made this :)

How to use: Change what you want in Settings.txt (a default is provided) run Calculate.exe or the provided python file (if you have python) <br>
This is made to be copy pasted into [Desmos's graphing calculator](https://www.desmos.com/calculator)
<br><br>
How it works: <br>
[See here](https://en.wikipedia.org/wiki/Polynomial_interpolation#Second_proof)<br>
The spiral-style works by giving each Polar point one more full rotation than the last
<br><br>
Tips: <br>
The spiral-like Polar equasion usually needs higher decimals to be accurate.<br>
Sometimes you need to change the bounds of theta in Desmos.<br>
Use full rotations to give theta higher values. For example:<br>
> (3,0) will be Polar (3, π/2) <br>
> (3,0,2) will be Polar (3, 9π/2) <br>