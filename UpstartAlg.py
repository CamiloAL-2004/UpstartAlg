print("Basic perceptron");
print("----------------");
# it learns, AND, OR (stabilizes) but not XOR (does not stabilize)

# include third input "1" which is the necessary threshold or "bias".
training_inputs_z = [ [1, 1, 1] , [1, 0, 1], [0, 1, 1], [0, 0, 1] ];
# We want to add another entry to X, corresponding to Z output to the patterns above  
training_inputs_x = [ [1, 1, 1], [1, 0, 1], [0, 1, 1], [0, 0, 1] ];
expected_output_z = [ 1, 0, 0, 0 ];
expected_output_x = [ 1, 0, 0, 1 ];

z_weights = [ 0, 0, 0 ];
x_weights = [ 0, 0, 0 ];
session_counter = 0;

def z_perceptron_output(input): # this is for getting the output value of the perceptron 
    global z_weights; # you're importing "weights"

    output=0;
    for j in range(0, len(z_weights)): # this process happens for each training input (each pink bracket)
        output+=z_weights[j]*input[j];
    
# inhibitory daughter unit 

    output += x_perceptron_output(input)*-10

    if (output >= 0): # this is the total output, from the sum of all the output values.`   `
        return 1;
    else:
        return 0;

def x_perceptron_output(input): # this is for getting the output value of the perceptron 
    inhibitory_patterns = [[ 1, 1, 0], [0, 0, 1]]
    for i in inhibitory_patterns:
        t = 0
        for j in range(0,len(i)):
            if i[j] == input[j]:
                t += 1
        if t == len(i):
            return 1
    return 0

    # if (output >= 0): # this is the total output, from the sum of all the output values.`   `
    #    return 1;
    # else:
    #    return 0;

# Z training phase:
def z_training():
    global z_weights;
    global session_counter;


    o_idx = 0;
    delta_weight=[0, 0, 0];
    session_counter += 1;
    print("training session number: ", session_counter)
    for t_i in training_inputs_z: # this is for iterating between all the patterns (pink square brackets)
        for j in range(0, len(t_i)):
            delta_weight[j]=(expected_output_z[o_idx]-z_perceptron_output(t_i))*t_i[j]
        for j in range(0, len(t_i)):
            z_weights[j]+=delta_weight[j] # this updates the weights (if necessary) for a pattern
        print("iteration_z "+str(o_idx)+" weights "+str(z_weights))
        o_idx+=1;

# X training phase:
def x_training():
    global x_weights;

    o_idx = 0;
    delta_weight=[0, 0, 0];

    for t_i in training_inputs_x: # this is for iterating between all the patterns (pink square brackets)
        for j in range(0, len(t_i)):
            delta_weight[j]=(expected_output_x[o_idx]-x_perceptron_output(t_i))*t_i[j]
        for j in range(0, len(t_i)):
            x_weights[j]+=delta_weight[j] # this updates the weights (if necessary) for a pattern
        print("iteration_x "+str(o_idx)+" weights "+str(x_weights))
        o_idx+=1;

print("before training Z: ",z_weights);
print("before training X: ",x_weights);

#Train Z
for i in range(0, 8):
    z_training();




print("after training Z: ", z_weights);
print("after training X: ", x_weights);

print("z_trained perceptron:");
print("Input [1 1] should be 1 and it is:",z_perceptron_output([1, 1, 1]));
print("Input [0 1] should be 0 and it is:",z_perceptron_output([0, 1, 1]));
print("Input [1 0] should be 0 and it is:",z_perceptron_output([1, 0, 1]));
print("Input [0 0] should be 0 and it is:",z_perceptron_output([0, 0, 1]));


print("x_trained perceptron:");
print("Input [1 1] should be 1 and it is:",x_perceptron_output([1, 1, 1]));
print("Input [1 0] should be 0 and it is:",x_perceptron_output([1, 0, 1]));
print("Input [0 1] should be 0 and it is:",x_perceptron_output([0, 1, 1]));
print("Input [0 0] should be 1 and it is:",x_perceptron_output([0, 0, 1]));

# if actual_output != expected_output:
#   if actual_output == 1 and expected_output == 0:
#       Add a unit with a heavy inhibitory (negative) connection terminating at Z
#   elif actual_output == 0 and expected_output== 1:
#       Add a unit with a heavy excitatory (positive) connection terminating at Z
#   else:
#       Do nothing