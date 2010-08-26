
GAMEPLAY
--------

* Player collides with room and wall obstacles
* maybe even let player smoothly speed up or slow down, within the above
  constraints.

* Other obstacles in the world - raised walls or columns in the room.
* Player collides with these obstacles

* Have camera look at the player as they move around
* Maybe have camera float around the ceiling, for funky 3D-ness of it all

* Create some sort of exit that the player must reach.
* The exit may be embedded within a wall, so that only one face of it is
  visible
* For some reason, I'm taken with the idea of the exit appearance being a black
  cube (which may be embedded within a wall,thus only exposing a single face)
  Each of the horizontally-facing faces has the word 'exit' in tiny white
  letters on it, a la Gauntlet. This may be a bit silly. Hooray!
* reaching the exit progresses to the next room?
  (it would be nice to have multiple interconnected rooms all 'visible' at
  once, but that might be a bit ambitious for now)

* Design other gameplay features but each one must be accompanied by a design
  for a level that uses it. Some ideas:
   * Gate, shaped like a nasty pointy portcullis, and a button in the floor
     that opens it
   * Things that chase the player? Rolling balls? Pacman-ghost shapes?
     (random thought: Should we give up and just write 3D rendered 'pacman',
     with occasional gameplay tweaks to exploit third dimension? It does fit
     in with the 'caught' theme.)
   * A lift. Toggles up, down when you stand on it.
   * a power-up that makes the player leave a trail. This enables them to
     press several buttons at once.
   * power-up, enables player to climb walls
   * power-up, enables player to move directly upwards into empty space
   * power-up, player moves very quickly (instantly?) as far as possible
     in the direction pressed before colliding. Good for getting around fast,
     but can't turn until brought to a stop by collision.


ENGINE
------

* Add shader with simple directional lighting


VERY OPTIONAL or SPECULATIVE
----------------------------

* Add bitmaps to our fragment shader

* big colored pixels on the walls (same size as player's cube)

* writing on the wall (one letter per 

* It would be nice to have per-pixel lighting. Pretty.

* It would be nice to have mobile lightsources within the world space.


`--DONE------------------------------------------------------------`

* a single cube is visible

* Shapes should be composeable into a multishape for performance. The whole
  room and any static geometry within it could be a single shape on a single
  gameitem, for example.

* Create a large cuboid room (say 20x20x20)
* Position the camera near the ceiling.

* Put player, shape=Cube(1, white), within the room

* Create a large cuboid room (say 20x20x20)
* Position the camera near the ceiling.
* Put player, shape=Cube(1, white), within the room
* Let player move around with cursor keys. The player (like all things) can
  only come to rest or change direction at integer ordinates, but moves
  smoothly from one location to the next.
* player movement should continue when key held down

