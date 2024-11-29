from collections import deque  # Import deque for efficient queue management in BFS

# Sample 3x3 grid representing delivery costs
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


# Function to find the highest possible minimum delivery cost for a path across the grid
def binary_search_maximum_min_cost(grid):
    """
    Uses binary search to find the highest minimum delivery cost that allows
    a feasible path from the top-left to the bottom-right corner of the grid.
    Displays each valid path and cost as it validates thresholds.

    Parameters:
    grid - a 2D list of integers representing delivery costs for each location

    Returns:
    The maximum minimum delivery cost that permits a valid path across the grid
    """

    # Step 1: Define the range for binary search by determining the minimum and maximum values in the grid
    low = min(map(min, grid))  # The smallest value in the grid (start of the search range)
    high = max(map(max, grid))  # The largest value in the grid (end of the search range)

    # Initialise the best possible minimum cost threshold as the lowest value in the grid
    best_cost = low

    # Step 2: Begin binary search to find the highest minimum cost threshold with a valid path
    while low <= high:
        # Calculate the midpoint of the current range, representing a possible minimum cost threshold
        mid = (low + high) // 2

        # Step 3: Check if there's a valid shortest path with BFS at the current threshold
        path_bfs = bfs_shortest_path_exists(grid, mid)
        if path_bfs:
            best_cost = mid  # Update the best known minimum cost
            print(f"Threshold: {mid} | Path (BFS): {path_bfs}")  # Display the valid BFS path and threshold
            low = mid + 1  # Shift the search range to look for a higher feasible threshold
        else:
            # If BFS fails, use DFS as an alternative check for path existence
            visited = set()  # Initialise visited set for DFS
            path_dfs = dfs_path_exists(grid, mid, 0, 0, visited, [(0, 0)])
            if path_dfs:
                best_cost = mid  # Update the best known minimum cost if DFS finds a path
                print(f"Threshold: {mid} | Path (DFS): {path_dfs}")  # Display the valid DFS path and threshold
                low = mid + 1
            else:
                # If both BFS and DFS fail, lower the threshold
                high = mid - 1

    # Step 4: Return the highest feasible minimum cost that allows a path from start to destination
    print(f"Optimal Delivery Route Cost: {best_cost}")
    return best_cost


# Modified BFS function to check for a valid shortest path at a given threshold
def bfs_shortest_path_exists(grid, threshold):
    """
    Finds the shortest path from the top-left to the bottom-right of the grid
    while enforcing that all cells in the path meet or exceed a given threshold.

    Parameters:
    grid - a 2D list representing delivery costs
    threshold - an integer representing the minimum delivery cost threshold to check

    Returns:
    List of tuples representing the path if a shortest path exists that meets the threshold,
    or None if no path is found.
    """

    # Get the grid dimensions (number of rows and columns)
    rows, cols = len(grid), len(grid[0])

    # Initialise a queue for BFS starting from the top-left corner, with initial path length 0
    queue = deque([(0, 0, [(0, 0)])])  # (row, col, path_list)

    # Set to track visited cells to avoid reprocessing
    visited = set([(0, 0)])

    # Start BFS loop to explore the grid
    while queue:
        # Dequeue the current cell and its associated path list
        x, y, path = queue.popleft()

        # Check if the destination (bottom-right corner) is reached
        if (x, y) == (rows - 1, cols - 1):
            return path  # Return the path if the destination is reached

        # Explore all possible directions: up, down, left, and right
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            # Calculate the new cell coordinates
            nx, ny = x + dx, y + dy

            # Check if the new cell is within grid boundaries, unvisited, and meets the threshold
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and grid[nx][ny] >= threshold:
                visited.add((nx, ny))  # Mark the cell as visited
                queue.append((nx, ny, path + [(nx, ny)]))  # Enqueue the cell with updated path

    # If BFS completes without reaching the destination, return None
    return None


# DFS-based helper function to check if there's a valid path at a given threshold
def dfs_path_exists(grid, threshold, x, y, visited, path):
    """
    Checks if there exists a path from the top-left to the bottom-right of the grid
    using DFS (depth-first search) where all cells in the path meet or exceed the given threshold.

    Parameters:
    grid - a 2D list representing delivery costs
    threshold - the minimum delivery cost threshold to check
    x, y - the current cell coordinates being processed
    visited - a set to track visited cells to prevent revisits
    path - the current path taken to reach this cell

    Returns:
    List of tuples representing the path if a path exists that meets the threshold,
    or None if no path is found.
    """

    # Get the grid dimensions
    rows, cols = len(grid), len(grid[0])

    # Base case: if the destination (bottom-right corner) is reached, return the path
    if (x, y) == (rows - 1, cols - 1):
        return path

    # Mark the current cell as visited
    visited.add((x, y))

    # Explore all possible directions: up, down, left, and right
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        # Calculate the new cell coordinates
        nx, ny = x + dx, y + dy

        # Check if the new cell is within bounds, unvisited, and meets the threshold
        if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and grid[nx][ny] >= threshold:
            # Recursively perform DFS on the new cell, adding it to the path
            result_path = dfs_path_exists(grid, threshold, nx, ny, visited, path + [(nx, ny)])
            if result_path:
                return result_path  # Return the valid path if found

    # If no valid path is found, backtrack by removing the current cell from visited
    visited.remove((x, y))
    return None


# Main function to initiate the process of finding the optimal delivery route
def find_optimal_delivery_route(grid):
    """
    Wrapper function to find the maximum minimum delivery cost for a feasible route
    from the top-left to the bottom-right corner of the grid.

    Parameters:
    grid - a 2D list of integers representing delivery costs

    Returns:
    The optimal delivery route cost as determined by binary search
    """
    # Use binary search to determine the optimal route by maximising the minimum cost threshold
    return binary_search_maximum_min_cost(grid)


# Run the main function with the sample grid and print the result
optimal_cost = find_optimal_delivery_route(grid)
print("The optimal delivery route cost:", optimal_cost)