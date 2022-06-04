# RpsSimulator

### Description:

RpsSimulator is a pygame program that simulates the evolution of a rock-paper-scissor system. This is my recreation of similar simulators that can be found online. The basic premise of a rock-paper-scissor system is that there exists three types of objects in which each type defeats one and is defeated by another. The simulation ends whe one type of object is left standing when all else has been defeated. Made in a week, this was purely made in order to brush up on my Python.

### Setup:

In order to use this, the first step is to create an assets directory. In this directory, add three image files: paper.png, rock.png, and scissors.png. These files are representations of the rock, paper, and scissor type.

Then you must download all dependencies with:

```bash
pip install -r requirements.txt.
```

Optionally, you can create a move function in index.py, following the notes there to create the function. This function represents how the objects would move. By default objects move at random. However, you can program it to follow a certain strategy, such as "Move away from the type that defeats me" or "Move towards the type that I defeat".

### Example Usage:

To use the simulator, simply run:

```bash
python -m rps.index
```

To run tests, run

```bash
python -m unittest.
```

### Brief Architecture Summary:

- `index.py`: The entrypoint of the game. This is the typical file found in most pygame projects.
- `pieces.py`: A file containing the classes used to create the sprites for the pygame.
- `hands.py`: A file containing classes that manages the sprite groups.
- `rps.py`: A file containing the RPS() class which manages all sprite groups. This is a very important file as it abstracts a lot of the sprite handling.
- `rpstypes.py`: A file containing typing information for custom types.
