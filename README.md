## Objective
The objective of this project is to implement efficient methods to
perform online, parallel hyperparameter search for discrete and
continuous search spaces. Hypervise should be able to manage allocated
resources for parallel searches, split data into training and test sets,
and validate effectiveness on live data.

## Table of Contents
1.) [Design Details](design.md)
2.) [Notes / Resources](notes.md)


## Milestones
[ ] ability to hill climb to optimize simple mathematical functions
    - [ ] discrete spaces
    - [ ] discretized search of continous spaces
[ ] ability to search multi dimensional spaces for optimal parameters for
more advanced mathematical functions
    - [ ] kd-tree simple region division
    - [ ] true continuous search? probably later
[ ] ability to search multidimensional spaces in separate processes
    - [ ] process limiting
    - [ ] resource management
    - [ ] "search slicing" with round robin aggregation
[ ] ability to pause/stop/resume search while continuing with best solution
    - [ ] settings and search saving
    - [ ] stream signaling


## TODO
- [ ] Create sample projects for testing effectiveness of hypervise on various models
  - [ ] simple, discrete model
  - [ ] discrete and continous model
  - [ ] irregular, discrete, continous model
  - [ ] evaulate over hyperopt examples
- [ ] evaluate the effectiveness of Tree of Parzen Estimates (TPE) vs other methods
  - [ ] simulated annealing
  - [ ] hill climbing 
  - [ ] genetic algorithms
- [ ] read most recent research papers for hyperparamater search
- [ ] implement top 3 choices for search or find libraries
- [ ] create search space partitioner
- [ ] create process manager for parallel and distributed search
- [ ] integrate search libs with search space partition algo and process
 manager
- [ ] save and resume functionality (like hyperopt)
- [ ] human suggestions throughout tests providing starting/jump points
- [ ] spawn hybrid models for combining select data regions
- [ ] data augmentation


