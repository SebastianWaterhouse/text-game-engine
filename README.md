# text-game-engine

JSON-extensible engine written in Python for Zork-like games


# Requirements

- Python 3
- Basic command line knowledge

# To Use

- Clone git repo OR download ZIP
- Navigate to directory
- Run `main.py` with Python 3

## Changelog

- `0.05` "things to do"
  - "info"
    - expand functions available built-in
    - will be composed of several mini-updates
  - `0.05` "things to do - health"
    - added functions pertaining to health
    - Little bit janky. Expect polishing in 0.0505
- `0.045` "updated code"
  - Moved some things around
  - Did some code cleaning
  - Added error handling into main loop. Use the `-v` option to disable.
  - Added some command line options help
- `0.04` "finished!!!"
  - Takes up 2 version numbers due to the size of the update
  - Added support for modders to add their own packages
     - Variety of package types: cats, for categories, branches, for new stories, and dual for both.
     - Data loader
     - Combines all category files loaded
     - Chooses last branches file loaded for story
  - Cleaned up code a bit.
- `0.025` "begin 0.03"
  - Mostly finished transition to 0.03
- `0.021` "instructions"
  - Updated readme
     - Added "to use" section
     - Added possibilities section
     - General improvements
- `0.02` "functional"
  - Made program functional
- `0.01` "ok?"
  - Initialized git repo


## Plans

- `0.051` "things to do - health expansion"
  - add target specification to health
- `0.052` "things to do - inventory"
  - add functions relating to player inventory
- `0.06` "save"
  - add functions relating to player saves
- `0.07` "sandbox"
  - a sandbox so that they don't mess up your computer with viruses.
- `0.08` "freedom"
  - allow modders to add code of their own
     - code.py file, will integrate with existing code function.

### Possibilities

- Make it even easier to make your own stories
