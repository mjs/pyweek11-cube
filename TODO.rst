
GAMEPLAY
--------

* refactor: The logic in move.directed_move should probably be at least
  partially handled by World or somesuch. I don't want every kind of move
  to have to worry about all this collision checking. The flagrant demeter
  violations in this function hint at this.

* Levels as declarations of locations are very difficult for humans to
  construct. Make level text files as 'nethack style' ASCII maps, eg:

    --start of level file--
    #############
    # s #       #
    #   #   #   #
    #       # e #
    #############

    ##         ##
    # s         #
        #   #    
    #         e #
    ##         ##
    --end of level file--

  Size of level is inferred on loading by:
  + Length of first line of file (13 chars) is level length.
  + Number of contiguous lines until first blank line (5 lines) is level width.
  + Number of repeated blocks of such lines (here there are 2) is level height.
    s=player start location
    e=exit location

* define a bunch of levels as text files
* An 'end of level' method which removes everything from the world,
  gets the next level and puts the player in it. 
* When player reaches exit, call 'end of level' method
  (it would be nice to have multiple interconnected rooms all 'visible' at
  once, but that might be a bit ambitious for now)

* Design other gameplay features but each one must be accompanied by a design
  for a level that uses it. Some ideas:
   * Gate, shaped like a nasty pointy portcullis, and a button in the floor
     that opens and closes it
   * 'sticky' things. If player gets adjacent to them, they stick to the
     player, and move alongside the player from then on, effectively increasing
     the bounds of the player, making it harder to navigate small corridors.
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

* Add bitmaps to our fragment shader
    * give room walls a very low resolution bitmap (one pixel is same size
      as player)
    * add the word 'EXIT' on the horizontal faces of the exit, a la Gauntlet

* when gameitems added to the world are intended to be unmoving ('static'),
  we remove their shape attribute, and append it to a single 'world' multishape
  instead. This allows all static gameitems to be drawn by Render in a single
  glDrawElements call, which is much faster.


VERY OPTIONAL or SPECULATIVE
----------------------------

* in-game text, either as bitmap letters on the walls, or as chunky letters
  formed out of walls:
    * instructions, keys, clues, level names, etc, displayed in-game
    * score, displayed in-game

* maybe let player smoothly speed up or slow down, within the existing
  'stop only at integer ords' constraint.

* It would be nice to have per-pixel lighting. Pretty.

* It would be nice to have mobile lightsources within the world space. Attached
  to in-game items.


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

* Have camera look at the player as they move around
* Maybe have camera float around the ceiling, for funky 3D-ness of it all

* Other obstacles in the world - raised walls or columns in the room.
* Create some sort of exit that the player must reach.
* The exit may be embedded within a wall, so that only one face of it is
  visible
* For some reason, I'm taken with the idea of the exit appearance being a black
  cube (which may be embedded within a wall,thus only exposing a single face)
  Each of the horizontally-facing faces has the word 'exit' in tiny white
  letters on it, a la Gauntlet. This may be a bit silly. Hooray!
* Add shader with simple directional lighting

Collision detection:
    * each item defines its own 'bounds', a set of co-ordinates relative to
      its own center, which represents the space it occupies. For example,
      the set player.bounds = { (0, 0, 0) } # it occupies one cube only
    * world.add adds the item.bounds, plus item.position offset, to the
      world collision dictionary.
    * world.remove removes it
    * when starting to move, an item must check if intended destination is
      occupied. (player collision with room and walls shoudl work now)
    * bug, collision with room does not work (was using Vector3s as dict
      keys. They should be unhashable. Fixed in project Euclid and we now
      use equivalent tuple as the dict key)
    * bug: player cannot move into exit location. It it embedded in the wall,
      which I would like to mean 'remove the wall from the world.collision
      collection at that location'. How to implement? How about: Exit gains
      a bounds, but is flagged as 'collide=False'. When doing start of movement
      collision check, we don't just look for occupied locations, but we look
      for the 'solid' flag on the object that occupies that location.
      Also, when item is added to world, if not solid then it overrides
      any previous solid entry.
    * bug, player cannot move back into player start location, because the
      following is not implemented:
        * When move starts, intended destination must be marked as occupied by
          item. When move complete, old position must be marked as unoccupied.

* level generator populates levels by loading text files

