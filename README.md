### Load Balancer Simulation

To run example simulation from `input.txt` file, use the main.py file:
```
python main.py
```

To use other files use the following code:
```python
from simulation import Simulation
Simulation(input_filename='input.txt').run(output_filename='output.txt')
```

To run unit tests:
```
python run_tests.py
```
