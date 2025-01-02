The most basic case of the Perceptron algorithm
takes in three inputs, with the third input always
being a 1 – acting as the necessary threshold (the
value which must be exceeded for the perceptron
to fire). This means that, in this case, it can be
trained with only four patterns: [ 1, 1, 1 ], [ 1, 0,
1 ], [ 0, 1, 1 ] and [ 1, 1, 1 ]. The expected output
for the: OR gate is [ 1, 1, 1, 0 ], the AND gate is
[ 1, 0, 0, 0 ] and the XOR (Exclusive OR) gate
is [ 0, 1, 1, 0 ]. Initially, all the weights of the Z
perceptron are set to 0. The weights are values
which determine the strength of the connection
between a certain input and Z. After the percep-
tron is presented with one of the patterns, its
weights are updated by multiplying the weight of
the connection (from the input to Z) and the input
itself (either a 1 or 0 in this case). The perceptron
Z then adds up all the values, if it is bigger than
1, then the Z outputs a 1, otherwise it outputs a
0. This is akin to a neurone integrating all of its
inputs from the dendrite and, after having processed 
all the inputs, firing an action potential or
not (Figure 1).

The perceptron training consists of a function
which iterates through all the patterns and of the
pattern’s elements. The training is used for cal-
culating the weights that are needed for correctly
identifying a certain pattern (i.e. the network out-
puts a one when it is meant to be a one).

The way the weights are trained (Algorithm 1)
is that their expected output is subtracted from
their actual output (line 6), then this result is mul-
tiplied by the value of the element of that entry
from the specific pattern the network happens to
be iterating through at that given moment in time
(either a 1 or 0). This is done for all the entries in
the pattern, after this, in line 8 all the weights are
updated simultaneously – this is done to avoid
confusing the network by letting all the percep-
tron weights be updated at once and eventually
converge.
