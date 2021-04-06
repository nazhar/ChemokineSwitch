
## About This Project

This repo contains the code for the boolean model described in 'A Putative “Chemokine Switch” that Regulates Systemic Acute Inflammation in Humans'. 


## Getting Started
To get a local copy up and running follow these simple steps.

### Prerequisites

* Python 2.7

* BooleanNet 1.2.8
  ```sh
  pip install booleannet==1.2.8
  ```
* Navigate to the folder where booleannet was installed and fix an error in ```network.py``` (See [this](https://github.com/devAbnull/booleannet/issues/1) open issue)
  ```sh
  sed -i 's/from networkx import component/from networkx import components/g' /path/to/boolean2/network.py
  ```
* pandas
  ```sh
  pip install pandas
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/nazhar/ChemokineSwitch.git
   ```

## Usage

The folder 'model_rules' contains text files for different versions of the model created during the model building process. To run simulations for each of these models:
```sh 
python sim.py
``` 
This creates a directory named 'model_output' and write csv files with the simulation results.

An short R script ```plot_sim_results.R``` is also included for plotting the results in figures similar to the ones in the paper.

To generate a state transition diagram for each of the models for both moderate and severe injury:

```sh 
python state_transition.py
```
This will write '.gml' files for each model and injury severity which can then be viewed in your favorite graph viewer. The figures in the paper were generated using [yEd](https://www.yworks.com/products/yed)

 
Figures 2 and 3 from the paper were generated using Model B. Figures 3-5 and the Figure S3 were generated using Model C. Model E explores the behavior if the mutual repression between chemokines was removed. 

This repo may be update with a docker image for easier setup in the future.