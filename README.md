# AppChallenge2019
*Created by Michael M, Ty D, Gabriel C of District 21, Florida.*

## What is this?
This App Challenge project is a neural network (written with Java and Python) which generates abstract art.
The network is trained -- so far -- using cubist works.

## What is the file structure?
The project so far consists of one Python file which uses Pillow (`pip install Pillow`) in order to transform images in `~/Training Images/inputs` (for instance image x) into three RGB components in one folder, located `~/Training Images/outputs/x`. The files themselves are jpegs; inputs are numbered 1-n, outputs are in folders with `x` being the original image name (also technically 1-n).
