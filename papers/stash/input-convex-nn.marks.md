 > energy-based models operates [source]($P/stash/input-convex-nn.pdf#energy-based models operates)
 > direct differentiation of the argmin [source]($P/stash/input-convex-nn.pdf#direct differentiation of the argmin)
 > general model is built over the output space [source]($P/stash/input-convex-nn.pdf#general model is built over the output space)
 > forward and backward passes [source]($P/stash/input-convex-nn.pdf#forward and backward passes)
 > specify them manually [source]($P/stash/input-convex-nn.pdf#specify them manually)
 > probabilistic semantics at all [source]($P/stash/input-convex-nn.pdf#probabilistic semantics at all)
 > optimization over the output is guaranteed [source]($P/stash/input-convex-nn.pdf#optimization over the output is guaranteed)
 > imputes the likely val- [source]($P/stash/input-convex-nn.pdf#imputes the likely val-)
 > sums of rectified half-planes to data [source]($P/stash/input-convex-nn.pdf#sums of rectified half-planes to data)
 > capture complex joint models [source]($P/stash/input-convex-nn.pdf#capture complex joint models)
 > max-margin structured [source]($P/stash/input-convex-nn.pdf#max-margin structured)
 > arbitrary loss function [source]($P/stash/input-convex-nn.pdf#arbitrary loss function)
 > adient descent is the bundle [source]($P/stash/input-convex-nn.pdf#adient descent is the bundle)
 > other regularizers are also possi- [source]($P/stash/input-convex-nn.pdf#other regularizers are also possi-)
 > [respect to an]($P/stash/input-convex-nn.pdf#respect to an)
 > implicit differentiation of the KKT opti- [source]($P/stash/input-convex-nn.pdf#implicit differentiation of the KKT opti-)
 > first-order optimality [source]($P/stash/input-convex-nn.pdf#first-order optimality)
 > equivalent to simply taking the sigmoid [source]($P/stash/input-convex-nn.pdf#equivalent to simply taking the sigmoid)
 > rier” function to the optimization [source]($P/stash/input-convex-nn.pdf#rier” function to the optimization)

  - max margin structured prediction versus maximum aposterior prediction
  - structured predictions
  - energy based models

  - solve constraint with splitting based on the cross entropy


# cQc2zwld2G3g - Training convex neural networks

# EuTzPF2b5iil - Convex functions

For [efficient optimization](@m4RN9zTWLoQC) a convex model architecture can help. The simplest
approach are purely convex functions, where a [sum of]($P/stash/input-convex-nn.pdf#sums of convex functions are also convex) convex projections defines
the structure.

 > input and output example space [source]($P/stash/input-convex-nn.pdf#input and output example space)

# m4RN9zTWLoQC - Inference via Optimization

Normally inference happens with a function evaluation given some arguments
defined by their features of the data sample. When doing inference via
optimization, we use have a input-output pair and are trying to find the best
fitting condition for this pair. 

This is an iterative method, trying to find a stationary point for our
derivatives regarding the input.

To have it efficient, a fast optimization routine is crucial. Convex functions
have better convergence properties than deep neural networks and making the
input [convex]($P/stash/input-convex-nn.pdf#we can optimize over the convex inputs) we can optimize with traditional methods, such as the bundle entropy 
method. In a general setting the structured approach is given in [SPANs]($P/stash/input-convex-nn.pdf#structured prediction energy).
