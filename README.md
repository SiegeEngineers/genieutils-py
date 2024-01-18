# genieutils-py

Python implementation of [genieutils](https://github.com/Tapsa/genieutils).

This library can be used to read and write `empires2_x2_p1.dat` files for Age of Empires II Definitive Edition.


## Supported dat versions

Currently, only the latest version used in Age of Empires II Definitive Edition is supported (`GV_LatestDE2`/`GV_C20`).


## Installation

```shell
pip install genieutils-py
```

## Usage examples

### Dump the whole dat file as json

The package comes with a handy command line tool that does that for you.

```shell
dat-to-json path/to/empires2_x2_p1.dat
```


### Change cost of Loom to 69 Gold

```python
from genieutils.datfile import DatFile

data = DatFile.parse('path/to/empires2_x2_p1.dat')
data.techs[22].resource_costs[0].amount = 69
data.save('path/to/modded/empires2_x2_p1.dat')
```

### Prevent Kings from garrisoning

```python
from genieutils.datfile import DatFile

data = DatFile.parse('path/to/empires2_x2_p1.dat')
for civ in data.civs:
    civ.units[434].bird.task_size -= 1
    civ.units[434].bird.tasks.pop()
data.save('path/to/modded/empires2_x2_p1.dat')
```


## Authors

[HSZemi](https://github.com/hszemi) - Original Author
