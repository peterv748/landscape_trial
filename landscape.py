"""
boiler plate code for modules
"""
import numpy as np
from numba import jit_module
import random



def compute_average(*args):
    """
    compute the float average of input arguments
    """
    
    return float((sum(args))/len(args))


def random_generator():
    """
    randon generator to use in diamond square algorithm
    """
    
    mu = 0.5
    sigma = 0.25
    
    return random.gauss(mu, sigma)

def init_grid(size):
    """
    initialize the diamond square grid
    """
    i = int(size)
    grid = np.zeros([i, i])
    grid[0,0] = random_generator()
    grid[(i-1), 0] = random_generator()
    grid[(0,(i-1) )] = random_generator()
    grid[((i-1), (i-1))] = random_generator()
    
    return grid

def find_square_step_neighbours(nw_position, current_length):
    """
    find the upper_left (NW), upper_right (NE)
    lower_left (SW), lower_right (SE) neighbours
    for the square_step part of the algorithm
    """

    nw_neighbour = [nw_position[0], nw_position[1]]
    ne_neighbour = [nw_position[0], (nw_position[1] + current_length)]
    sw_neighbour = [(nw_position[0] + current_length), nw_position[1]] 
    se_neighbour = [(nw_position[0] + current_length), (nw_position[1] + current_length)]
   
    return nw_neighbour, \
	    ne_neighbour, \
        sw_neighbour, \
        se_neighbour


def calculate_midpoint(nw_point, ne_point, sw_point, se_point):
    """
    calculate midpoint of the square in the diamond square algorithm
    """
    
    y = (nw_point[1] + ne_point[1]) / 2 
    x = (sw_point[0] + nw_point[0]) / 2
    
    return int(x), int(y)

def recalculate_positions(midpoint, current_length):
    """
    define the uppercorners of the four children
    """
    nw_position = [int((midpoint[0] - current_length)), int((midpoint[1] - current_length))]
    ne_position = [int((midpoint[0] - current_length)),  int(midpoint[1])]
    sw_position = [int(midpoint[0]), int((midpoint[1] - current_length))]
    se_position = [int(midpoint[0]), int(midpoint[1])]

    return nw_position, ne_position, sw_position, se_position


def calculate_squarestep_value(grid, midpoint, upper_left,  upper_right, lower_left, lower_right):
    """
    calculate the new value for the midpoint in the square step
    """ 
    i = int(upper_left[0] - 1)
    j = int(upper_left[1] - 1)
    nw_value = grid[i,j]
    i = int(upper_right[0]-1)
    j = int(upper_right[1] -1)
    ne_value = grid[i,j]
    i = int(lower_left[0]-1)
    j = int(lower_left[1] -1)
    sw_value = grid[i,j]
    i = int(lower_right[0]-1)
    j = int(lower_right[1] -1)
    se_value = grid[i,j]
    new_value = compute_average(nw_value, ne_value, sw_value, se_value) + random_generator()
    i = int(midpoint[0] - 1)
    j = int(midpoint[1] - 1)
    grid[i, j] = new_value
    
    return 

def quadtree_diamond_square_algorithm(grid, nw_position, current_length):
    """
    in this recursive procedure the heavy lifting of calculating the square step and
    diamond step is executed
    """
    midpoint = [0,0]
    
    if  ((current_length % 2) == 0):
        nw_point, ne_point, sw_point, se_point = find_square_step_neighbours(nw_position, current_length)
        midpoint[0], midpoint[1] = calculate_midpoint(nw_point, ne_point, sw_point, se_point)
        calculate_squarestep_value(grid, midpoint, nw_point, ne_point, sw_point, se_point)
        current_length = current_length / 2
        nw_position, ne_position, sw_position, se_position = recalculate_positions(midpoint, current_length)

        quadtree_diamond_square_algorithm(grid, nw_position, current_length)
        quadtree_diamond_square_algorithm(grid, ne_position, current_length)
        quadtree_diamond_square_algorithm(grid, sw_position, current_length)
        quadtree_diamond_square_algorithm(grid, se_position, current_length)
    return

#jit_module(nopython=True)