## Design Details

### splitting search space for parallelization / multiprocessing / distribution

#### kd - tree
- allows for splitting lists into regions
- allows for continous and discrete variable search
- allows for k-NN queries for searched points
- defaults by splitting into regions
- I love kd-trees
- design considerations:
    - order of split:
        1.) split on all list items
        2.) split on discrete variables
        3.) split on continous variables
    - as points come in, split regions based on "expected improvement"[2]
        - methods to balance exploration vs exploitation and prevent
         exploring regions already
        - split region is determined by probability that a higher
        solution is within the region
            - region "score" is average of objective score, weighted
            by the probability distribution
    - partitions are stored in the database with each node so data isn't
     loaded into memory during evaluation. Also allows data to be stored
      with each node


#### searching algorithm
- hybrid of swarm optimization, hill climbing, random intialization
split search space and run in a round-robin tournament
    approach.
        - this would allow easier stop and resume functionality
        - ties into the kd tree approach for region division
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
    and that region becomes the active search region for hill climbing

[2](https://www.cse.wustl.edu/~garnett/cse515t/spring_2015/files/lecture_notes/12.pdf)