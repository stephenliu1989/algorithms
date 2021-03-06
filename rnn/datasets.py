import numpy as np
from  theano import config

def sinewaves(timesteps, n):
    """
    Artificially generate sine wave data. 


    returns:

        x_train of shape (n, timesteps, 1)
            - this is the input data
        y_train of shape (n, timesteps, 1)
            - basically x_train shifted back 1 time step

    """
    rng = np.random.RandomState(888)
    t = np.arange(timesteps).astype(config.floatX)
    frequency_weights = rng.rand(n).astype(config.floatX)
    amplitude_weights = rng.rand(n).astype(config.floatX)
    t_scaled = frequency_weights[:, np.newaxis] * t
    x_train = amplitude_weights[:, np.newaxis] * np.sin(t_scaled)
    y_train = np.roll(x_train, -1, axis=1)

    # add on new dimension
    x_train = x_train[:, :, np.newaxis]
    y_train = y_train[:, :, np.newaxis]

    return x_train, y_train