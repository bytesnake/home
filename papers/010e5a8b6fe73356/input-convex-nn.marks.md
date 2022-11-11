vim : ft=markdown.linked spell spelllang=en :

  - max margin structured prediction versus maximum aposterior prediction
  - structured predictions
  - energy based models
  - https://scholar.google.de/scholar?cites=8658835360066668486&as_sdt=2005&sciodt=0,5&hl=en

  - solve constraint with splitting based on the cross entropy

# 4BxYyzpjltlz - Convex conjugate of entropy function

To make the energy convex with respect to the input, a [barrier function]($P/stash/input-convex-nn.pdf#rier” function to the optimization) keeps
the values in unit range. The negative entropy approaches infinite gradient at
boundaries zero and one.

For the simple case of a vector product energy function, the problem is equivalent
to the [convex conjugate](convex_conjugates.pdf#Negative Entropy) solution. The optimal, unconstraint model solution, 
is therefore projected with the [sigmoid function]($P/stash/input-convex-nn.pdf#equivalent to simply taking the sigmoid) to the feasible unit range. This 
result maximizes the vector product similarity while fulfilling constraints.

Under augmented lagrangian, this solution is unfortunately not as simple
anymore. The resulting problem does not have a closed form solution.

# IBucG0HX0e3z - Energy based learning

Encoding associatations between features and targets is the key goal of machine
learning. A energy based model (EBM) takes both as input and produces an energy
score, assessing its quality. It performs inference over the targets by using
optimization techniques and iterative update schemes.

This has the advantage that complex models can be used for the [output space]($P/stash/input-convex-nn.pdf#general model is built over the output space) which
is similar to traditional neural networks for the input features. This is
normally achieved by making this model [easy]($P/stash/input-convex-nn.pdf#energy-based models operates) or have more sophisticated models
over the output space. We make here a tradeoff between model complexity and
training performance by ensuring that the models is convex but can have an 
[arbitrary]($P/stash/input-convex-nn.pdf#specify them manually) structure. See [convex functions](@EuTzPF2b5iil) for the proposed architecture.

Another application of energy based learning is to [fill-in]($P/stash/input-convex-nn.pdf#imputes the likely val-) values with the
highest probability (e.g. lowest energy) based on the given data. For example
spectrogram completion uses information from lower frequency region to predict
those of higher regions.

# maXIBKPnd9mT - Optimizing the model's parameters

One method to solve the energy based learning problems follows [max-margin](./max-margin.pdf)
structure predictions. The training data target should be optimal compared to
all other possible values, and the distance should be as large as possible.
Henceforth the max-margin approach. In order to avoid mode collaps into a
constant energy (which would fufill the inequality constraint), add a small
scaling factor, which grows by distance of value to optimal target. The
objective regularizes weights and maximizes slack as much as possible.

For a more traditional weight optimization method, we need to [differentiate]($P/stash/input-convex-nn.pdf#direct differentiation of the argmin)
through the `argmin` operator of the target estimation. The alternative approach
uses the [KKT optimality]($P/stash/input-convex-nn.pdf#implicit differentiation of the KKT opti-) condition as objective. This results in a gradient
estimation step consisting of a linear equation system and two adjoint diff
operators. The complexity scales linear with k but as Newton method requires
only a few iterations, this is neglegible. We can use any [loss function](]($P/stash/input-convex-nn.pdf#respect to an) for
our distance metric between target and estimation.

# cQc2zwld2G3g - Training convex neural networks

[Fitting data to convex]($P/stash/input-convex-nn.pdf#sums of rectified half-planes to data) functions is not so common, normally you either look at 
linear decision boundaries or complex non-linear functions. The fitting
algorithm is often convex, for example for support vector machines.

We want to train a convex function, because it makes learning the estimation 
[guaranteed to be easy]($P/stash/input-convex-nn.pdf#optimization over the output is guaranteed) and global. The training does not capture probabilistic
[semantics]($P/stash/input-convex-nn.pdf#probabilistic semantics at all) at all and only models the [input and output space]($P/stash/input-convex-nn.pdf#input and output example space).

The [bundle method](./bundle-method.pdf) requires only a few [forward and backward]($P/stash/input-convex-nn.pdf#forward and backward passes) passes.

# EuTzPF2b5iil - Convex functions

For [efficient optimization](@m4RN9zTWLoQC) a convex model architecture can help. The simplest
approach are purely convex functions, where a [sum of]($P/stash/input-convex-nn.pdf#sums of convex functions are also convex) convex projections defines
the structure.

Using a mixture of convex (for the target) and non-linear (for the embedding of
input) can capture [complex joint models]($P/stash/input-convex-nn.pdf#capture complex joint models) while making [training](@cQc2zwld2G3g) them simple.

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
