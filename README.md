# Moonsweeper — A minesweeper clone, on a moon with aliens, in PyQt.

> This project has been cloned from [pythonguis-examples](https://github.com/pythonguis/pythonguis-examples).

## Set up 
Make sure you have [Python](https://www.python.org/downloads/) installed.

### In Visual Studio Code
- Clone the repository
- Open the repository folder in Visual Studio Code
- Make sure you have the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) installed
- Open the Command Palette (View > Command Palette...) and run the command: "Python: Create Environment"
- Select the `venv` and the `requirements.txt` file to install the dependencies
- Now open the `main.py` file and click on the top-right play button to run the game! Or run the "Python: Run Python File in Terminal" command from the Command Palette.

### In a terminal
- Clone the repository
- In a terminal, navigate to the repository:
```cd /path/to/moonsweeper```
- Create a virtual environment:
```python -m venv venv``` 
> Note: You may need to use `python3` or `py` instead of `python` depending on your system.
- Activate the virtual environment:
  - On Windows:
  ```venv\Scripts\activate```
  - On macOS and Linux:
  ```source venv/bin/activate```
- Install the dependencies:
```pip install -r requirements.txt```
- Run the game:
```python main.py```


## About the game 
Explore the mysterious moon of Q'tee without getting too close to the alien natives!

Moonsweeper is a single-player puzzle video game. The objective of the game is to explore the area around your landed space rocket, without coming too close to the deadly B'ug aliens. Your trusty tricounter will tell you the number of B'ugs in the vicinity.



![Moonsweeper](screenshot-minesweeper1.jpg)

This a simple single-player exploration game modelled on _Minesweeper_
where you must reveal all the tiles without hitting hidden mines.
This implementation uses custom `QWidget` objects for the tiles, which
individually hold their state as mines, status and the
adjacent count of mines. In this version, the mines are replaced with
alien bugs (B'ug) but they could just as easily be anything else.

![Moonsweeper](screenshot-minesweeper2.jpg)

> If you want to learn more about build GUI applications with Python,
take a look at my [PyQt5 tutorials](https://www.pythonguis.com)
which covers everything you need to know to start building your own applications with PyQt5.

## Code notes

### Cheating the first turn

In many *Minesweeper* variants the initial turn is considered a free
go — if you hit a mine on the first click, it is moved somewhere else.
Here we cheat a little bit by taking the first go for the player, ensuring that it is on a non-mine spot. This allows us not to worry about the bad first move which would require us to recalculate the adjacencies.
We can explain this away as the "initial exploration around the rocket"
and make it sound completely sensible.

## Other licenses

Icons used in the application are by [Yusuke Kamiyaman](http://p.yusukekamiyamane.com/).
