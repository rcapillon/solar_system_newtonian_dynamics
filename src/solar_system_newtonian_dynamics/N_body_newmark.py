import numpy as np


G = 6.67408e-11


def compute_N_body_forces(positions, masses):
    """
    Computes gravitational forces exerted on each body
    """
    n_body = positions.shape[0]
    mat_forces = np.zeros((n_body, 3))

    for i in range(n_body):
        position_i = positions[i, :]
        mass_i = masses[i]
        for j in range(i + 1, n_body):
            position_j = positions[j, :]
            mass_j = masses[j]

            distance_i_j = np.linalg.norm(position_j - position_i)
            vec_r_i_to_j = (position_j - position_i) / distance_i_j
            F_j_on_i = (G * mass_i * mass_j / distance_i_j ** 2) * vec_r_i_to_j
            mat_forces[i, :] += F_j_on_i
            mat_forces[j, :] -= F_j_on_i

    return mat_forces


def N_body_newmark(starting_positions, masses, delta_t, n_t):
    """"""
