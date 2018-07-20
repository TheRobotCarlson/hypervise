## Objective
The objective of this project is to implement efficient methods to
perform online, parallel hyperparameter search for discrete and
continuous search spaces. Hypervise should be able to manage allocated
resources for parallel searches, split data into training and test sets,
and validate effectiveness on live data.


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


## design details

- on splitting search space for parallelization / multiprocessing / distribution
    - using a custom kd-tree
        - allows for splitting lists into regions
        - allows for continous and discrete variable search
        - allows for k-NN queries for searched points
        - defaults by splitting into regions
        - I love kd-trees

- searching algorithm
    - swarm optimization
        - high resources for multiple instances of resource-intensive tests
        - OR have to split search space and run in a round-robin tournament
        approach.
            - this would allow easier stop and resume functionality
            - ties into the kd tree approach for region division
        - allows for effective search of parameter space
    - hybrid of swarm optimization, hill climbing, random intialization
        - initialize randomly by region of space-partitioned kd-tree
        - pick the highest, non-negative scorer from
        the objective function.
            - If non-negative not available? Not sure
        - return this as the active model
        - begin hill climbing within this region
        - begin stochastic swarm optimization within other regions
            - if another agent has already left this region, decrease
            probability of movement towards.
            - This can be tracked by the leaf nodes of the kd trees and
            propagated upwards into larger regions.
        - when a higher scorer appears, that becomes the new active model
        and that region becomes the active search region for hill climing


## Important information / notes
- TPE doesn't optimize hyperparameters independently well. If Hp's are
not independent of one another, this might be better. This would suggest
a hybrid approach would be best for generality.[1]

- to use gradient descent/search methods, you have to use continous
search spaces or map discrete values into discrete search spaces (duh)



## Current Resources
1.) [hyperopt implementation](https://github.com/hyperopt/hyperopt)

2.) [hyperopt docs](http://hyperopt.github.io/hyperopt/)

3.) [nips paper on hyperparamater optimization (with bengio)](https://papers.nips.cc/paper/4443-algorithms-for-hyper-parameter-optimization.pdf)

4.) [science of model search](https://arxiv.org/pdf/1209.5111.pdf)

5.) [fast ml](http://fastml.com/optimizing-hyperparams-with-hyperopt/)

6.) [neural architecture search (darts)](https://www.groundai.com/project/darts-differentiable-architecture-search/)


## Related Resources
- [on neural nets](neural_nets.md)

[1]: http://fastml.com/optimizing-hyperparams-with-hyperopt/