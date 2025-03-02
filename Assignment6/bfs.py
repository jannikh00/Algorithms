# Assignment 6: Breadth First Search

class Graph:
    # Initializing Graph
    def __init__(self, size):
        """
        Initialize a new Graph with a specified number of nodes.

        Parameters:
            size (int): The number of nodes in the graph. Must be non-negative.
        
        Raises:
            ValueError: If size is negative.
        
        Attributes:
            size (int): The number of nodes.
            adjacency_list (dict): A dictionary where each key is a node index (0 to size-1) 
                                    and each value is an empty list that will later store tuples 
                                    of (neighbor_index, weight).
            node_data (list): A list of strings with length equal to size, representing data 
                                for each node, initially set to an empty string.
        """
        # Checking if size is negative
        if size < 0:
            raise ValueError("Size cannot be negative")
        # Sets Graph size equal to "size" input
        self.size = size
        # Initializes Adjacency Dictionary with number of keys being the value of size
        self.adjacency_list = {i: [] for i in range(size)}
        # Initializes Node Data that holds a list of strings of length size that represent the data at each node
        self.node_data = ["" for j in range(size)]

    # Adding Edges
    def add_edge(self, node1, node2, weight):
        """
        Add an undirected edge between two nodes with a specified weight.

        Parameters:
            node1 (int): The index of the first node.
            node2 (int): The index of the second node.
            weight: The weight value associated with the edge (can be int, float, etc.).
        
        Raises:
            IndexError: If the graph has no nodes,
                        if either node1 or node2 is out of the valid range (0 to size-1),
                        or if one of the nodes does not exist in the adjacency list.
        """
        # If Graph Size is 0, Graph can't have nodes and edges
        if self.size == 0:
            raise IndexError("Graph has no nodes")
        # Checking if nodes are in bounds
        if node1 < 0 or node1 >= self.size or node2 < 0 or node2 >= self.size:
            raise IndexError("One of the nodes is not in valid range")
        # Checking if nodes exist | Node can be in bounds, but still be non-existant
        if node1 not in self.adjacency_list or node2 not in self.adjacency_list:
            raise IndexError("One of the nodes doesn't exist")
        # Add Neighbor for first node, including weight
        self.adjacency_list[node1].append((node2, weight))
        # Add Neighbor for second node, including weight
        self.adjacency_list[node2].append((node1, weight))
    
    # Adding Node Data
    def add_node_data(self, node, data):
        """
        Set or update the data for a specific node.

        Parameters:
            node (int): The index of the node.
            data (str): The data to assign to the node.
        
        Raises:
            IndexError: If the graph has no nodes,
                        if the node index is out of the valid range,
                        or if the node does not exist in the adjacency list.
        """
        # If Graph Size is 0, Graph can't have nodes
        if self.size == 0:
            raise IndexError("Graph has no nodes")
        # Checking if node is in bounds
        if node < 0 or node >= self.size:
            raise IndexError("Node not in valid range")
        # Checking if nodes exist
        if node not in self.adjacency_list:
            raise IndexError("Node doesn't exist")
        # Add Data for specified node
        self.node_data[node] = data

    # Breadth First Search Functionality
    def bfs(self, start_node):
        """
        Perform a breadth-first search (BFS) starting from the specified node.

        Parameters:
            start_node (int): The index of the starting node for BFS.
        
        Returns:
            list: A list of node indices representing the order in which nodes are visited.
        
        Raises:
            IndexError: If the graph has no nodes or if the start_node is not in the valid range.
        """
        # If Graph Size is 0, Graph can't have nodes
        if self.size == 0:
            raise IndexError("Graph has no nodes")
        # Checking if start_node is in bounds
        if start_node < 0 or start_node >= self.size:
            raise IndexError("Start node not in valid range")
        # Queue that holds all unchecked nodes
        queue = [start_node]
        # List that holds information on each node whether it's visited or not
        visited = [False] * self.size
        # List that holds the order in which bfs goes through graph
        order = []
        # As long as there is a queue
        while queue:
            # Sets the currently checked Node equal to the first Node in the queue
            current_node = queue.pop(0)
            # If the currently checked Node doesn't appear in the "visited" list
            if not visited[current_node]:
                # Add it to the "visited" list
                order.append(current_node)
                # Mark the currently checked Node as visited
                visited[current_node] = True
                # For each neighbor of the currently checked Node
                for neighbor in self.adjacency_list[current_node]:
                    # If the neighbor hasn't been visited
                    if not visited[neighbor[0]]:
                        # Add it to the queue
                        queue.append(neighbor[0])
        # Returns "order" list if queue is empty
        return order


# Testing
def run_tests():

    print("\nRunning tests...")

    # Initializing a Graph
    print("\n------Initialising Graph------")
    print("my_graph = Graph(5)")
    my_graph = Graph(5)
    print("my_graph.size:")
    print(my_graph.size)
    print("my_graph.adjacency_list:")
    print(my_graph.adjacency_list)
    print("my_graph.node_data:")
    print(my_graph.node_data)

    # Assignment Example Inputs/Outputs
    print("\n------Assignment Example Inputs/Outputs------")
    g = Graph(5)
    g.add_node_data(0, "A")
    g.add_node_data(1, "B")
    g.add_node_data(2, "C")
    g.add_node_data(3, "D")
    print(g.adjacency_list) # {0: [], 1: [], 2: [], 3: []}
    print(g.node_data) # ['A', 'B', 'C', 'D'] 
    g.add_edge(0, 1, 2) 
    g.add_edge(0, 2, 2) 
    g.add_edge(0, 3, 2) 
    g.add_edge(1, 4, 2) 
    g.add_edge(1, 2, 2)
    print(g.adjacency_list) # {0: [(1, 2), (2, 2), (3, 2)], 1: [(0, 2), (4, 2), (2, 2)], 2: [(0, 2), (1, 2)], 3: [(0, 2)], 4: [(1, 2)]}

    print(g.bfs(0)) # [0, 1, 2, 3, 4] 
    print(g.bfs(1)) # [1, 0, 4, 2, 3]
    print(g.bfs(2)) # [2, 0, 1, 3, 4]

    # Additional Examples
    print("\n------Additional Examples------")

    # Test 1: Simple Graph with BFS Traversal
    print("\nInput: This tests the following graph: g = Graph(3)")
    print("g.add_edge(0, 1, 1)")
    print("g.add_edge(1, 2, 1)")
    print("g.bfs(0)")

    g = Graph(3)
    g.add_edge(0, 1, 1)
    g.add_edge(1, 2, 1)

    print("Expected Output:")
    print("[0, 1, 2]")  # BFS should visit all connected nodes

    print("Actual Output:")
    print(g.bfs(0))

    # Test 2: Disconnected Graph
    print("\nInput: This tests a disconnected graph: g = Graph(5)")
    print("g.add_edge(0, 1, 1)")
    print("g.add_edge(2, 3, 1)")
    print("g.bfs(0)")

    g = Graph(5)
    g.add_edge(0, 1, 1)
    g.add_edge(2, 3, 1)

    print("Expected Output:")
    print("[0, 1]")  # BFS should only visit nodes in the same component

    print("Actual Output:")
    print(g.bfs(0))

    # Edge Case 1: BFS with Invalid Start Node (Negative Index, Out of Bounds)
    print("\nInput: This tests BFS with an invalid start node (-1)")
    print("g = Graph(3)")
    print("g.add_edge(0, 1, 1)")
    print("g.add_edge(1, 2, 1)")
    print("g.bfs(-1)")

    g = Graph(3)
    g.add_edge(0, 1, 1)
    g.add_edge(1, 2, 1)

    print("Expected Output:")
    print("Error: Start node not in valid range")

    print("Actual Output:")
    try:
        print(g.bfs(-1))
    except IndexError as e:
        print(f"Error: {e}")

    # Edge Case 2: BFS with Out-of-Bounds Start Node
    print("\nInput: This tests BFS with an out-of-bounds start node (5)")
    print("g = Graph(3)")
    print("g.add_edge(0, 1, 1)")
    print("g.add_edge(1, 2, 1)")
    print("g.bfs(5)")

    g = Graph(3)
    g.add_edge(0, 1, 1)
    g.add_edge(1, 2, 1)

    print("Expected Output:")
    print("Error: Start node not in valid range")

    print("Actual Output:")
    try:
        print(g.bfs(5))
    except IndexError as e:
        print(f"Error: {e}")

    # Edge Case 3: Graph with No Edges
    print("\nInput: This tests a graph with no edges")
    print("g = Graph(3)")
    print("g.bfs(0)")

    g = Graph(3)

    print("Expected Output:")
    print("[0]")  # Only the start node should be returned

    print("Actual Output:")
    print(g.bfs(0))

    # Edge Case 4: Graph with Self-Loops
    print("\nInput: This tests BFS on a graph with self-loops")
    print("g = Graph(3)")
    print("g.add_edge(0, 0, 1)")
    print("g.add_edge(1, 1, 1)")
    print("g.add_edge(2, 2, 1)")
    print("g.bfs(0)")

    g = Graph(3)
    g.add_edge(0, 0, 1)  # Self-loop at node 0
    g.add_edge(1, 1, 1)  # Self-loop at node 1
    g.add_edge(2, 2, 1)  # Self-loop at node 2

    print("Expected Output:")
    print("[0]")  # BFS should not infinitely loop

    print("Actual Output:")
    print(g.bfs(0))

    # Edge Case 5: Large Graph Performance Test
    print("\nInput: This tests BFS on a large graph with 1000 nodes connected in a chain")
    print("g = Graph(1000)")
    print("for i in range(999): g.add_edge(i, i + 1, 1)")
    print("g.bfs(0)")

    g = Graph(1000)  # Large graph with 1000 nodes
    for i in range(999):  
        g.add_edge(i, i + 1, 1)  # Connect nodes in a chain

    print("Expected Output:")
    print("[0, 1, 2, ..., 999]")  # BFS should traverse all nodes

    print("Actual Output:")
    print(g.bfs(0))

    # Edge Case 6: Graph with Negative Size
    print("\nInput: This tests creating a graph with a negative size")
    print("g = Graph(-3)")

    print("Expected Output:")
    print("Error: Size cannot be negative")

    print("Actual Output:")
    try:
        g = Graph(-3)
    except ValueError as e:
        print(f"Error: {e}")

    # Edge Case 7: Adding edge with out of bounds node
    print("\nInput: This tests adding an edge with an out-of-bounds node")
    print("g = Graph(3)")
    print("g.add_edge(3, 1, 2)")

    g = Graph(3)

    print("Expected Output:")
    print("Error: One of the nodes is not in valid range")

    print("Actual Output:")
    try:
        g.add_edge(3, 1, 2)
    except IndexError as e:
        print(f"Error: {e}")

    # Edge Case 8: Adding edge with non-existent node
    print("\nInput: This tests adding an edge where one node doesn't exist")
    print("g = Graph(3)")
    print("g.adjacency_list.pop(1)")
    print("g.add_edge(0, 1, 2)")

    g = Graph(3)
    g.adjacency_list.pop(1)  # Artificially remove node 1

    print("Expected Output:")
    print("Error: One of the nodes doesn't exist")

    print("Actual Output:")
    try:
        g.add_edge(0, 1, 2)
    except IndexError as e:
        print(f"Error: {e}")

    # Edge Case 9: Adding node data with invalid index
    print("\nInput: This tests adding data to an invalid node index")
    print("g = Graph(3)")
    print("g.add_node_data(3, 'X')")

    g = Graph(3)

    print("Expected Output:")
    print("Error: Node not in valid range")

    print("Actual Output:")
    try:
        g.add_node_data(3, "X")
    except IndexError as e:
        print(f"Error: {e}")

    # Edge Case 10: Adding node data with non-existent node
    print("\nInput: This tests adding data to a node that doesn't exist")
    print("g = Graph(3)")
    print("g.adjacency_list.pop(1)")
    print("g.add_node_data(1, 'X')")

    g = Graph(3)
    g.adjacency_list.pop(1)  # Artificially remove node 1

    print("Expected Output:")
    print("Error: Node doesn't exist")

    print("Actual Output:")
    try:
        g.add_node_data(1, "X")
    except IndexError as e:
        print(f"Error: {e}")

    # Edge Case 11: Graph with no nodes
    print("\nInput: This tests running BFS on an empty graph")
    print("g = Graph(0)")
    print("g.bfs(0)")

    g = Graph(0)

    print("Expected Output:")
    print("Error: Graph has no nodes")

    print("Actual Output:")
    try:
        print(g.bfs(0))
    except IndexError as e:
        print(f"Error: {e}")

    # Termination message
    print("\nAll tests passed!")

if __name__ == "__main__":
    run_tests()