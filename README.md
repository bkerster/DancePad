# DancePad

Credit to Promit. His pad design heavily inspired me, and sensor design in particular was his: https://ventspace.wordpress.com/2018/04/09/danceforce-v3-diy-dance-pad-controller/

Super Make Something also had a substantial influence on my final design: https://www.youtube.com/watch?v=nXjj9IXUaA4

# Design and measurement
Before starting this project I read every DDR build guide I could find and incorporated the pieces I liked into my ultimate design.
I especially liked Promit's design, but had one major issue with it. His uses a giant piece of plexi across the entire pad. I wanted a pad that had discrete physical "buttons." 

I also wanted a pretty heavy pad. I'm a big guy and wanted something I knew would stand up to me stomping on it. A heavier feel would also feel more "arcade-like" to me, especially since I'll be playing on carpet. This led me to go with a larger overall height for my pad (1.5" in total with a 3/4" solid base).

I was able to complete this project 100% on my small outdoor patio while living in a small apartment. With access to a better shop this project would be much easier.


Your plywood will need to be broken down to the following sizes:
Base: 35" x 35" (1)
Edges: 1" x 34" (4)
Static plates: 11" x 11" (5)

I had the base cut out of the original plywood sheet, which was a big help. 
I went into this project with no woodworking experience, and breaking down the wood into the right sizes with nice perpendicular cuts was a major challenge. If you're new to woodworking make sure you have a strategy to ensure you get nice straight cuts. Using a track saw or tablesaw would help a lot, or at least make sure to use carefully positioned guides with a circular saw (which is what I ultimately did).

After cutting all of the plywood I glued the 1" borders to the base, and then spray painted the sides of the base and the borders. I did several coats with a light sanding between each coat.

While waiting for that to dry I added a chamfer to the edges of the "static" plates on the sides where I would want to run wires later. This was one side for the two top corners, and all 4 sides of the center. With that done I then painted these as well (just the top). I then placed these on the pad, but did *not* glue them down yet.

This is a good time to tape a large copper "plus" shape down across the length of the pad. This will serve as the common ground for the sensors later. Doing it now allows you to run under where the center plate will be glued down later.

## Sensor Construction
The next step was to prepare the sensors. These were each constructed out of two pieces of 1/4" MDF, copper tape, and velostat. 
The first piece of MDF is effectively just a riser, to ensure the final total height for the sensor plus a sheet of plexiglass is about the same height as the border.
This piece I cut to 11" x 10.5" The shorter width is to provide space between the sensor and the center plate for wiring.
The second piece of MDF I cut to 9 3/4" x 9 1/4". After cutting to size I covered one side of each piece of MDF completely with copper tape. The smaller sheet I also placed a piece of copper tape such that it started on the copper side and wrapped around to create a small copper tab on the uncovered side. This is to be used later as an attachment point for the wiring, since the copper side will be facedown and inaccessible.

The velostat works as a pressure sensitive resistor, so when its sandwiched between the two copper coated pieces the current across them will change as the pressure on them increases. The next step is to put a sheet of velostat in place. First it needs to be cut just smaller than the dimensions of the larger piece of MDF. Then tape it to the copper side of the larger sheet. I used double sided tape for this on two edges. It's important that the velostat is not stretched when its taped down. It's also a good idea to leave a gap near the middle as well, so you'll have space later to connect this side of the sensor to the rest of the circuit.

After that duct tape the smaller sheet copper side down to the larger sheet with the velostat sandwiched in the middle. I used duct tape for this on two sides. Its important to not tape too tightly so the velostat isn't under too much pressure when your not standing on it. The final step is to add foam to the other two sides. I used 3 small pieces on each side which seemed to provide a good level of firmness and springiness. 

Once you have 4 of those built glue them into place with wood glue. I put the bottom, left, and right sensors back against the border which left about 1/2" of space to use to connect wiring. The top sensor I left the gap between the sensor and the border instead, which makes wiring that sensor and the ground easier.

## Build the electronics compartment
You need a place to store the brains of the pad, namely your microcontroller and circuit board. I also used the same space to place select and back buttons. I used the top right corner of the pad for this. First figure out how much space you'll need by laying out the buttons along with the electronics. Fit can be a bit tight for the buttons I placed them on either side of the circuit board and microcontroller which I stacked together. Pencil this on to the top right corner of the top right plate, and then cut that rectange out with a saw. Then route a channel for the wires to run along the top of the plate into this chamber.

You'll also need a lid for this chamber. I made mine out of some extra 1/4" MDF, cut to size (make sure to leave overhang so you have room to screw it into place later),  chamfered the top edges, and then painted it black. The chamfering is to ensure it doesn't hurt too bad if you should accidently step on the lid. Also drill two 30mm holes where you want your buttons. You can do this either before or after painting.

## Wiring 
First connect the bottom side of each sensor to the copper "plus" you laid down earlier with a bit of copper tape. Then for the smaller side of each sensor you'll need to run some copper tape from the bit of copper tape wrapped to the top side down onto the base plate. Be careful to do this in away that doesn't touch the bottom part of the sensor, especially without velostat in the way. I put down a layer of duct tape, and ran the copper tape along that. Then place a two small layers of copper tape on top of where you landed on the base plate. This will serve as a soldering pad. Repeat the process for each sensor.

Each sensor will need one signal wire, and one additional wire will need to be connected to the ground "plus." For each wire make sure to carefully measure to ensure you have enough to run from the soldering pad for that sensor to the electronics compartment (plus a bit of extra). Then solder the wires to their pads and run them into the electronics compartment. I used a bit of hot glue for wire management.

## Install Supports
Create thin 1/2" supports by gluing to thin pieces of 1/4" MDF scrap together. These will be placed into the wiring gap in such a way that they don't interfere with the wiring itself. These basically prevent the top acrylic top plates from slipping down if you step on the edges of the pad. Two of these support blocks in the gap for each sensor worked well for me.

## Finishing the electronics 
I used a small circuit board to manage the circuit connections between the sensors, buttons, and the microcontroller. I recommend wiring up the microcontroller and other pieces first (like resistors, that way the only soldering you have to do AT the pad are the 5 wires to the circuit board.
You will also need a way to connect the microcontroller to the outside world. I used a pair of USB-C extenders plugged into each other as my method of doing this. I used a drill bit about the height of the USB extenders and drilled a couple of holes through the border, and waggled the drill bit around until I had made a hole about the shape of the USB extenders, and the could be snuggly pushed into place. Once I was confident the hole and location were going to work (make sure you can plug the microcontroller into the extenders from inside the electronics compartment!) I used some 2 part epoxy to permantly mount the extenders into the wood. The creates a USB-C port on the outside, and you can still remove the microcontroller readily if needed. Once everything is wired up you can attach the circuit board to the base plate (either screw it down, or use a bit of tape). 
At this point everything is wired up so you might want to hook up to your computer and do some initial testing.

## Finish Gluing the static plates.
At this point its time to use wood glue to permanantly affix the static plates to the base plate. I put this off for so long because it gives you the freedom to easily adjust the dimensions of the plates in case things don't fit quite right.

## Build the top plates
Cut acrylic into 11" x 11" squares. These should fit neatly into the gaps between the static plates. I used a circular saw to cut them to size, with somewhat mixed results. Some pieces had a bit of chipping along the cut edges, while some cut smoothly. If you can source acrylic already cut to the right size it could save a lot of hassle. With them cut I used a craft spray adhesive to attach the acrylic to laminated printouts of DDR arrows. I found this quite tricky. If you put too much adhesive it will be visible and your arrows won't look as good. This is the best method I've found so far though. With the lamination my art was slightly larger than the acrlyic so I used an X-acto to clean up the edges. 

## Testing and Calibration
At this point you now have all of the components essentially complete, so its a good time to do some testing before closing everything up. Set up the code on the microcontroller and check what voltage values make sense for each button. Depending how tightly they've been taped and other factors you might have some small differences between them. I recommend playing a simple song or two to check if your calibration is working or if you notice any major issues.

## Corner brackets and Closing everything up
To keep the top plates in place I made very simple corner brackets out of 1/8" MDF. Basically just strips about 1" wide run across the corners of each sensor, and screw into the static plates and border. To construct the brackets I cut the strips to be about 1" x 2.5". I then used 120 grit sandpaper on a sanding block smooth out the the top edges, and rounded off the corners. Your foot will fall onto these so you want to ensure there are now sharp corners. Then I painted them to match the rest of the pad. 

When you have enough of those to cover every corner of each sensor its time to screw them into place, locking the top plates in. I used #6 1/2" screws, and drilled pilot holes with a 3/32" drill bit with a built in countersink. It's important to use pilot holes here since splitting any of the wood this far into the project could be disastrous. I just put one screw on each side. 

Once the brackets are all in place screw down the electronics compartment lid. You'll probably want a slightly longer screw (3/4" or so) since the lid is thicker than the brackets. With that your DDR pad is complete and its time to start playing!



