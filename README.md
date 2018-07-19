## Objective
The objective of this project is to implement efficient methods to
perform online, parallel hyperparameter search for discrete and
continuous search spaces. Hypervise should be able to manage allocated
resources for parallel searches, split data into training and test sets,
and validate effectiveness on live data.


## TODO
- [ ] Create sample projects for testing effectiveness of various models
  - [ ] simple, discrete model
  - [ ] discrete and continous model
  - [ ] irregular, discrete, continous model
  - [ ] evaulate over hyperopt examples
- [ ] evaluate the effectiveness of Tree of Parzen Estimates (TPE) vs
other methods such as simulated annealing, hill climbing, genetic
algorithms, etc
- [ ] read most recent research papers for hyperparamater search
- [ ] implement top 3 choices for search or find libraries
- [ ] create search space partitioner
- [ ] create process manager for parallel and distributed search
- [ ] integrate search libs with search space partition algo and process
 manager
- [ ] save and resume functionality (like hyperopt)


## Important information / notes
- TPE doesn't optimize hyperparameters independently well. If Hp's are
not independent of one another, this might be better. This would suggest
a hybrid approach would be best for generality.[1]



## Current Resources
1.) [hyperopt implementation](https://github.com/hyperopt/hyperopt)

2.) [hyperopt docs](http://hyperopt.github.io/hyperopt/)

3.) [nips paper on hyperparamater optimization (with bengio)](https://papers.nips.cc/paper/4443-algorithms-for-hyper-parameter-optimization.pdf)

4.) [science of model search](https://arxiv.org/pdf/1209.5111.pdf)

5.) [fast ml](http://fastml.com/optimizing-hyperparams-with-hyperopt/)

[1]: http://fastml.com/optimizing-hyperparams-with-hyperopt/
