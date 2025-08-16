import numpy as np
from tqdm import tqdm


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


def N_body_newmark(starting_positions, starting_velocities, masses, t_end, n_t):
    """
    Solves the equation of motion for the N-body problem with a Newmark method
    """
    n_body = starting_positions.shape[0]
    dt = t_end / (n_t - 1)

    arr_accelerations = np.zeros((n_body, 3, n_t))
    arr_velocities = np.zeros_like(arr_accelerations)
    arr_positions = np.zeros_like(arr_accelerations)

    prev_A = np.zeros((n_body, 3))
    prev_V = starting_velocities
    prev_X = starting_positions

    for i in tqdm(range(n_t)):
        mat_F = compute_N_body_forces(prev_X, masses)
        mat_A_i = mat_F
        for j in range(n_body):
            mat_A_i[j, :] /= masses[j]
        mat_V_i = prev_V + dt * (mat_A_i + prev_A) / 2
        mat_X_i = prev_X + dt * prev_V + 0.25 * (dt ** 2) * (prev_A + mat_A_i)

        arr_accelerations[:, :, i] = mat_A_i
        arr_velocities[:, :, i] = mat_V_i
        arr_positions[:, :, i] = mat_X_i

        prev_A = mat_A_i
        prev_V = mat_V_i
        prev_X = mat_X_i

    return arr_positions, arr_velocities, arr_accelerations
