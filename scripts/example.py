import numpy as np
import matplotlib.pyplot as plt
import imageio
from pathlib import Path

from solar_system_newtonian_dynamics.N_body_newmark import N_body_newmark


if __name__ == '__main__':
    ####
    # Bodies in order:
    # - Sun
    # - Mercury
    # - Venus
    # - Earth
    # - Mars
    # - Jupiter
    # - Saturn
    # - Uranus
    # - Neptune

    ####
    # Data from NASA, 2016-Aug-22 00:00:00.0000 (HORIZONS)

    masses = np.zeros((9, ))
    masses[0] = 1.989e30
    masses[1] = 3.285e23
    masses[2] = 4.867e24
    masses[3] = 5.972e24
    masses[4] = 6.39e23
    masses[5] = 1.898e27
    masses[6] = 5.683e26
    masses[7] = 8.681e25
    masses[8] = 1.024e26

    starting_positions = np.zeros((9, 3))
    starting_positions[0, :] = np.array([0., 0., 0.])
    starting_positions[1, :] = np.array([5.852296973118354E+06, -6.845655330121294E+07, -6.130597684372377E+06]) * 1e3
    starting_positions[2, :] = np.array([-1.014943608323032E+08, -3.631935237687530E+07, 5.358850622229887E+06]) * 1e3
    starting_positions[3, :] = np.array([1.298356164938387E+08, -7.768755378090946E+07, 2.506807156201452E+03]) * 1e3
    starting_positions[4, :] = np.array([8.368950352943902E+07, -1.940918763164824E+08, -6.121237598765135E+06]) * 1e3
    starting_positions[5, :] = np.array([-8.148488151253015E+08, -1.031242990916091E+07, 1.827608679125831E+07]) * 1e3
    starting_positions[6, :] = np.array([-3.809742255115976E+08, -1.451800052313166E+09, 4.039970136346608E+07]) * 1e3
    starting_positions[7, :] = np.array([2.773635090276258E+09, 1.102736378354509E+09, -3.181865449348283E+07]) * 1e3
    starting_positions[8, :] = np.array([4.218927972303070E+09, -1.508862041236476E+09, -6.615516445881832E+07]) * 1e3

    starting_velocities = np.zeros((9, 3))
    starting_velocities[0, :] = np.array([0., 0., 0.]) * 1e3
    starting_velocities[1, :] = np.array([3.876634762566754E+01, 6.651816783564274E+00, -3.012971582507838E+00]) * 1e3
    starting_velocities[2, :] = np.array([1.156446952109234E+01, -3.313288922088748E+01, -1.121643883638605E+00]) * 1e3
    starting_velocities[3, :] = np.array([1.481300439040604E+01, 2.543927926404054E+01, -3.696599799773992E-05]) * 1e3
    starting_velocities[4, :] = np.array([2.316368548220578E+01, 1.167653937274012E+01, -3.237966470060969E-01]) * 1e3
    starting_velocities[5, :] = np.array([1.040159803700254E-02, -1.245986409623953E+01, 5.153611376745282E-02]) * 1e3
    starting_velocities[6, :] = np.array([8.816852606697767E+00, -2.490214724126964E+00, -3.083133186345777E-01]) * 1e3
    starting_velocities[7, :] = np.array([-2.563602724397541E+00, 5.998481547630901E+00, 5.543786926740690E-02]) * 1e3
    starting_velocities[8, :] = np.array([1.795291433032886E+00, 5.138113732226138E+00, -1.469947457693157E-01]) * 1e3

    # t_end = 395 * 24 * 3600  # a year + a month in seconds
    t_end = 2 * 717 * 24 * 3600  # a martian year + sixty earth days in seconds
    # t_end = 10 * 365 * 24 * 3600  # 10 years
    n_t = int(3e5)
    save_interval = int(1e3)
    plot_interval = int(1e2)

    arr_positions, _, _ = N_body_newmark(starting_positions, starting_velocities, masses, t_end, n_t)

    n_plotted_bodies = 5
    colors = ['k', 'tab:gray', 'tab:orange', 'tab:blue', 'tab:red']
    count = 1
    for i in range(0, n_t, save_interval):
        fig = plt.figure(figsize=(8, 8), dpi=100)
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(arr_positions[0, 0, :i],
                arr_positions[0, 1, :i],
                arr_positions[0, 2, :i],
                'o', color=colors[0], markersize=5)
        for j in range(1, n_plotted_bodies):
            ax.plot(arr_positions[j, 0, :i:plot_interval],
                    arr_positions[j, 1, :i:plot_interval],
                    arr_positions[j, 2, :i:plot_interval],
                    '-', color=colors[j], linewidth=0.5)
            ax.plot(arr_positions[j, 0, i],
                    arr_positions[j, 1, i],
                    arr_positions[j, 2, i],
                    'o', color=colors[j])
            ax.set_xlim(-3e11, 3e11)
            ax.set_ylim(-3e11, 3e11)
            ax.set_zlim(-8e10, 8e10)
            ax.set_aspect('equal')
            ax.grid(False)
        plt.savefig(f'./frame_{count:05d}.png')
        plt.close(fig)
        count += 1

    images = []
    pathlist = Path('./').glob('./*.png')
    for path in pathlist:
        image_path = str(path)
        images.append(image_path)

    writer = imageio.get_writer('./2_mars_years.mp4', fps=10)
    for im in sorted(images):
        writer.append_data(imageio.v2.imread(im))
    writer.close()