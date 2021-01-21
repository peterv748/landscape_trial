
"""
main workflow to create a fractal landscape
bases on the diamond square algorithm
"""
import time
import landscape
import draw_landscape


def main():
    """
    main procedure
    """
    
    size = 7
    last_position = [(2**size + 1), (2**size + 1)]
    first_position = [1,1]
    length = last_position[0] - first_position[0]
    current_length = length
    
    grid = landscape.init_grid(int(last_position[0]))  
    start = time.time()
    landscape.quadtree_diamond_square_algorithm(grid, first_position, current_length)
    time_elapsed = time.time() - start
    draw_landscape.plot_landscape(grid, time_elapsed)
     
if __name__ == "__main__":        
    main()