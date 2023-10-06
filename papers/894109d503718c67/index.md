vim: filetype=markdown.home.linked :

The chapter on [Fourier Series]($P/894109d503718c6u7/index.pdf) starts with a short historical summary ofthe 
origin and invention of fourier series.

In the [Warmup Section]($P/894109d503718c67/index.pdf#A real- or complex-valued) the periodicity condition of functions, the trigonometric 
and exponential series and the relation to Fourier series are introduced.
Further examples series developments for simple odd-even rectangular and 
triangular functions are derived in examples.

Exercises of [1. exponential forms]($P/894109d503718c67/index.pdf#1. EXPONENTIAL) were simple with substiution for (a) and 
linear argument for (b). For [2. amplitude-phase formulation]($P/894109d503718c67/index.pdf#2. AMPLITUDE-PHASE) application of 
`sin(a+b)` trigonometric law, gives the desired result. With the remark on
[2p period]($P/894109d503718c67/index.pdf#Remark PERIOD 2p INSTEAD) it is obvious that the Fourier series for `f(ct)` is the same for 
`p=c\pi` when [changing scale]($P/894109d503718c67/index.pdf#SCALE CHANGE). From the periodic property of the Fourier series 
it follows for [time shift]($P/894109d503718c67/index.pdf#TIME SHIFT) same coefficients `a_n`, `b_n` with different series 
development in argument. The remark on [linearity]($P/894109d503718c67/index.pdf#REMARK LINEARITY OF FOURIER) of fourier operators makes the
scaled and shifted odd square wave [exercise 4.4]($P/894109d503718c67/index.pdf#Fourier series of f) simple. For the next exercise, 
we simply need to [apply series development]($P/894109d503718c67/index.pdf#FOURIER SERIES AND COEFFICIENTS) of section to find the results for 
[functions]($P/894109d503718c67/index.pdf#Find the Fourier series of the). Exponentials Fourier series in [exercise 6.]($P/894109d503718c67/index.pdf#Find the exponential Fourier) are derived with the
the [Fourier series]($P/894109d503718c67/index.pdf#FOURIER SERIES AND COEFFICIENTS). For (a) we can simply use the periodicity of integral. 
Both are terms of `integrate xe^x`. The [derivative]($P/894109d503718c67/index.pdf#is differentiable, must the derivative) of a periodic function is 
periodic. The [integral]($P/894109d503718c67/index.pdf#is integrable over all closed intervals) only if the function is odd in period (see condition).

For coefficients `1/sqrt(n)` [there is not function]($P/894109d503718c67/index.pdf#Does there exist an) as the energy is not bounded. 
For coefficients `1/n` a Log function clamps between 0/2pi boundaries, as can be
seen in this [Stack Exchange](https://math.stackexchange.com/questions/3310746/fourier-series-with-all-coefficients-frac1n).

For Parseval theorem of [function products]($P/894109d503718c67/index.pdf#13. PRODUCTS Let) substituting the complex definition 
with [trigonometric coefficients]($P/894109d503718c67/index.pdf#of the trigonometric series into exponential form) yields the required identity. The sine 
[orthonormal basis]($P/894109d503718c67/index.pdf#14. Show that) exercise can be solved by using sine law, integrating over
cosine terms and recognizing the resulting sinc function.

For every smooth function there exists also a [Fourier Sine and Cosine]($P/894109d503718c67/index.pdf#Fourier Sine Series and Cosine Series) series.
Actually three strategies exist for function in half-intervals, we can either
extend [odd]($P/894109d503718c67/index.pdf#Fourier sine series.) to the second half, [even]($P/894109d503718c67/index.pdf#Fourier cosine series) or periodic with the [scaling]($P/894109d503718c67/index.pdf#Remark PERIOD 2p INSTEAD) defined in 
previous section.

To understand the [exercises](papers/894109d503718c67/index.pdf#4.3) of section 4.3, I started to recap some analysis 
of previous chapter. The example for continuity of [one point vs. other points](papers/894109d503718c67/index.pdf#has nothing to do with continuity at other points)
is a really interesting example, making sense because `pi + x` still irrational
and the in-between reciprocal for denominator of rational number cannot be
filled. They then discuss [convergence in the mean](papers/894109d503718c67/index.pdf#CONVERGENCE IN THE MEAN) and point out that this 
doesn't implies point-wise convergence, affecting the Dirichlet function and
leading to Gibbs phenomenon. [Uniform convergence](papers/894109d503718c67/index.pdf#UNIFORM CONVERGENCE) on the other hand measures 
in inf-norm and implies therefore pointwise-convergence. 

Read [proof of Riemann-Lebesgue](papers/894109d503718c67/index.pdf#If a or b is finite, define)



[source]($P/894109d503718c6u7/index.pdf)
[source]($P/894109d503718c67/time_freq_analysis.pdf)

[source]($P/894109d503718c67/index.pdf#classical subject of Fourier)
