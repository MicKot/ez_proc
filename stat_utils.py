import statsmodels.nonparametric.api as smnp
import scipy.special as s_s
import numpy as np


def get_univariate_dist(
    data, kernel="gau", fft=True, bw="scott", gridsize=100, cut=3, clip=None
):
    kde = smnp.KDEUnivariate(data)
    kde.fit(kernel, bw, fft, gridsize=gridsize, cut=cut, clip=clip)
    grid, y = kde.support, kde.density
    return grid, y


def interpolate_densities(grid_1, density_1, grid_2, density_2):
    def create_new_grid(grids):
        lower_start_boundary = grids[0][0] if grids[0][0] < grids[1][0] else grids[1][0]
        higher_end_boundary = (
            grids[0][-1] if grids[0][-1] > grids[1][-1] else grids[1][-1]
        )
        new_grid = np.linspace(lower_start_boundary, higher_end_boundary, len(grids[0]))
        return new_grid

    new_grid = create_new_grid([grid_1, grid_2])
    new_density_1 = np.interp(new_grid, grid_1, density_1)
    new_density_2 = np.interp(new_grid, grid_2, density_2)
    return new_grid, new_density_1, new_density_2
