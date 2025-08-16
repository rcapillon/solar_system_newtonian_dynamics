import numpy as np


G = 6.67408e-11


def compute_N_body_forces(positions, masses):
    """"""
    n_body = positions.shape[0]
    mat_forces = np.zeros((n_body, 3))

    vec_radius = np.sqrt(np.sum(np.power(positions, 2), axis=-1))

    for i in range(n_body):
        radius_i = vec_radius[i]
        position_i = positions[i, :]
        mass_i = masses[i]
        for j in range(i + 1, n_body):
            radius_j = vec_radius[j]
            position_j = positions[j, :]
            mass_j = masses[j]

    return mat_forces


def N_body_newmark(starting_positions, masses, delta_t, n_t):
    """"""
