import numpy as np
import tensorflow as tf

rps = ('R', 'P', 'S')
rps2int = {'R' : 0, 'P' : 1, 'S' : 2, '' : 3}
int2rps = {rps2int[c] : c for c in rps2int}
rps_to_int = lambda hist : [rps2int[c] for c in hist]

inp0 = tf.keras.Input(shape = (None,), batch_size = 1)
x0 = tf.keras.layers.Embedding(input_dim = 3, output_dim = 2, mask_zero = False)(inp0)
x0 = tf.keras.layers.GRU(units = 1, stateful = True, recurrent_initializer = 'glorot_uniform')(x0)
inp1 = tf.keras.Input(shape = (None,), batch_size = 1)
x1 = tf.keras.layers.Embedding(input_dim = 3, output_dim = 2, mask_zero = False)(inp1)
x1 = tf.keras.layers.GRU(units = 1, stateful = True, recurrent_initializer = 'glorot_uniform')(x1)
x2 = tf.keras.layers.concatenate([x0, x1])
x2 = tf.keras.layers.Dense(units = 3, kernel_initializer = 'glorot_uniform')(x2)
model = tf.keras.Model(inputs = (inp0, inp1), outputs = x2)
model.compile(loss = tf.keras.losses.CategoricalCrossentropy(from_logits = True),    # this loss function works because it's applied across the last dimension of the predictions
              optimizer = tf.keras.optimizers.Adam(learning_rate = 0.01))
weights_0 = model.get_weights()    # will be used to reset the model
nn = enumerate([6, 3, 3, 11])    # how much history to pass while training for each player

def player(prev_play, opponent_history=[], self_history=[], n0 = [6]):
    opponent_history.append(prev_play)
    # this resetting of model is done because main.py code keeps appending opponent history to this list but starts any new play with ''. this also allows to set any custom parameter for a specific player, like how n0 is used here
    if opponent_history[-1] == '':
        tf.keras.backend.clear_session()
        model.set_weights(weights_0)
        model.reset_metrics()
        model.reset_states()
        opponent_history[:] = []
        self_history[:] = []
        n0[0] = next(nn)[1]
    nhist = len(opponent_history)
    if nhist > 1:
        n = n0[0]
        x0 = rps_to_int(opponent_history[-min(nhist, n):])
        x1 = rps_to_int(self_history[-min(nhist, n):])
        y = [0.0, 0.0, 0.0]
        y[x0[-1]] = 1.0
        dataset = tf.data.Dataset.from_tensors(((np.array([x0[:-1]]), np.array([x1[:-1]])), np.array([y])))
        model.fit(dataset, epochs = 8, verbose = 0)
        guess = rps[(1 + np.argmax(model.predict((np.array([x0]), np.array([x1])), verbose = 0))) % 3]
    else:
        guess = np.random.choice(rps)
    self_history.append(guess)
    return guess
