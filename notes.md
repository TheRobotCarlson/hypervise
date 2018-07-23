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