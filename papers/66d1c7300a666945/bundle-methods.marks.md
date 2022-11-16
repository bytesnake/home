vim: filetype=markdown.linked :

# tQ0VLGpv6SG3 - Linear function family and bounds

The bundle method is based on the observation that the [Taylor approximation](./bundle-methods.pdf#Taylor approximation is a lower bound) is
a lower bound of convex functions. Further linearizing the function works well
for subgradients, as any value from the set can be used when augmenting the
minorizing function. It is therefore easily used for [non-smooth](./bundle-methods.pdf#optimize a non-smooth) functions.

The generated function is described by the [maximium of all hyperplanes](./bundle-methods.pdf#following lower bounds) plus a
possible regularizing term. At each step a new minimum of the current function
is estimated and the next function created by sampling the subdifferentials and
adding it to the lower-bound constraints set.

# IBVD2uGMGmU2 - Problem and dual solutions

Finding a minimum for the [function family](@tQ0VLGpv6SG3) can be solved with linear programming
and is given by the minimal extreme point. With a regularization the problem
becomes convex and can be [solved in the dual space](./bundle-methods.pdf#considerably easier in the dual space) with number of dual variables 
depending on the sampled Taylor approximations.

The resulting dual problem depends on convex conjugate of the regularization
term. When the regularization term is l2, then the problem is [quadratic](./bundle-methods.pdf#dual optimization problem is a quadratic program).

Finally a [simplified algorithm](./bundle-methods.pdf#simplified algorithm has essentially), performing a line search for the weight update 
step, gives similar convergence property. It has the advantage that no
information for the gradients has to be stored, and only the offset needs to be
kept.

# YcAGvBRFiD6Y - Flexibility and applications

The bundle method algorithm is quite flexible with respect to the empirical risk
and regularization term. The empirical risk does not have to decompose into a 
summation and multivariate loss terms, such as [SVM Ranking](./bundle-methods.pdf#SVM Ranking), [ν-trick](./bundle-methods.pdf#margin settings using the ν-trick ) and 
[Precision@k](./bundle-methods.pdf#Precision@k), can used. Further it is not necessarily in closed form and sampling 
methods can be used, e.g. for [intractable graphical models](./bundle-methods.pdf#intractable graphical models).

Finally the regularization term does not have to be smooth, only the convex
conjugate needs to exist. Together with the [quadratic or line search](@IBVD2uGMGmU2) solution
this provides a flexible template for solving such problems.
