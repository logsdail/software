'''
This example shows how to use the get_k_grid() function which allows to determine reciprocal space sampling
k_grid setting based on simulation cell size and converged value of minimum sampling density.
Useful when running calculations for variable sizes of supercells (e.g. surfaces)
'''

def test_run_k_grid():
    from carmm.run.aims_calculator import get_k_grid

    #### Traditional ASE functionality #####
    from data.model_gen import get_example_slab as slab
    slab = slab(adsorbate=True)
    #########
    sampling_density = 0.02 # example value of sampling density /Angstrom
    k_grid = get_k_grid(slab, sampling_density, surface=True, verbose=True )
    assert(k_grid[0] == 6)
    assert(k_grid[1] == 6)
    assert(k_grid[2] == 1)

test_run_k_grid()
