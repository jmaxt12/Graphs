---------------------------DAY 1: GRAPHS------------------------------
#  TIP: MEMORIZE the algorithms for:
    #  -BREADTH FIRST SEARCH
    #  -DEPTH FIRST SEARCH
     
#  WHY? 
    #  -To MORE easily recognize this data structure when encountering it
    #  -To conserve brain power when solving problems using these 
    #   algorigthms.
#  What is a 'GRAPH'?
    #  -Graphs are data structures that are used to represent
    #   relationships.
    #  -Runtime complexity of Adjacency List: O(n * e), 
        #  -In this case, n = nodes, e = average # of edges per vertex,
        #   E = total number of edges
    #  -Runtime complexity of Adjacency Matrix: O(n^2)
    
#  What are graphs composed of?
    #  -Nodes (AKA "Vertices" or "Vertexes")
        #  -Holds values
        #  -i.e. - friends on Facebook
    #  -Edges (can be arrows or lines)
        #  -Used to describe kinds of relationships between two nodes
    #  -Graphs can be either: 
        #  -WEIGHTED or UNWEIGHTED:
            #  -WEIGHTED graph = a graph with specficied values on each   
            #   edge that emphasize the importance/priority of that edge
            #   in comparison to other edges. 
                #  -i.e. - Google maps uses weighted graphs to help users
                #   find the shortest path between two points on a map.
            #  -UNWEIGHTED graph = a graph WITHOUT specficed values on   
            #   each edge to emphasize the importance/priority of that edge
            #   in comparison to other edges. 
        #  -DIRECTED or UNDIRECTED:
            #  -DIRECTED graph = demonstrates a relationship between  
            #   two nodes where only ONE node is directly affected by
            #   their relationship with the other. 
                #  -i.e. - Your Twitter account and your followers
                    #  -Just because someone follows you on Twitter does
                    #   NOT mean that you must follow them
            #  -UNDIRECTED graph = demonstrates a bi-directional 
            #   relationship between two nodes where only BOTH nodes are 
            #   directly affected by their relationship with one other.
                #  -i.e. - Friends on Facebook
                    #  -When someone is your friend on Facebook, you are
                    #   automatically assumed to be THEIR friend as well.    
        #  -CYCLIC or ACYCLIC:
            #  -CYCLIC graph = a graph that contains related nodes where
            #   you can travel along the edges and end up at a previously-
            #   visited node.
            #  -ACYCLIC graph = a graph that DOES not contain any related
            #   nodes where you can travel along the edges and end up at 
            #   a previously-visited node.
        #  -SPARSE or DENSE:
            #  -SPARSE graph = a graph that has a low number of edges 
            #   for each node.
            #  -DENSE graph = a graph that has a high number of edges 
            #   for each node.   
#  PROBLEM SOLVING WITH GRAPHS:
    #  (1)  Understand/Translate the Problem
    #  (2)  Create the graph
    #  (3)  Traverse the graph 
        #  "Traversal"?
            #  Going through an entire data structure to either:
                #  (a) "touch" (visit) each and every node
                #  (b) find a specific node
            #  Traversal of a list = O(n) runtime complexity
                      
    
#  BREADTH FIRST SEARCH (BFS) AKA "LEVEL ORDER TRAVERSAL"
    #  -Algorithm used to search a graph, starting at levels closest
    #   to the root and finishing at those furthest away.
    #  -Searches a graph for a particular node by:
    #     (1) Starting at the root node (or "starting vertex")
    #     (2) Move down to LEFT-MOST node in the NEXT level (from root)
    #         and move from LEFT to RIGHT, across that level
    #     (3) Continue this pattern until either:
    #             #  (a) you reach the node you're looking for
    #             #  (b) you reach the end of the tree
    #  -Explores all possible paths to find one with smallest weight,
    #   traversing ACROSS before traversing DOWN.
    #  -USEFUL FOR:
        #  -Solving a problem where you know the solution is very CLOSE
        #   to the root
        #  -Routing or path-finding problems (i.e. - google maps)
        #  -Providing the SHORTEST path to get to a given node
        #  -Suggesting people you may know in social networks
    #  -REMEMBER:
        #  -***BFS NEVER revisits nodes
        #  -***You cannot perform BFS recursively.
    
    #  -STEPS FOR TRAVERSAL:
    #  (1)  Create a queue to hold a list of nodes to explore
    #  (2)  Add starting vertex (s) to the queue
    #  (3)  Start exploration, beginning with the starting vertex (s)
        #  (a) while there are unscheduled vertices that are one edge 
        #      away from the current vertex...
            #  (i) schedule these adjacent vertices to be explored 
            #      by adding them to the queue
    #  (4)  Mark vertex as 'explored' by removing it from the queue
    
#  DEPTH FIRST SEARCH (DFS)
    #  -Algorithm used to search a graph, traversing each branch, down
    #   to its deepest level BEFORE exploring another branch.
    #  -Explores all possible paths to find one with smallest weight,
    #   traversing DOWN a branch before traversing ACROSS the same level.
    #  -It is like a 3-line recursive search algorithm
    #  -Goes as deep as possible with each parent => child before moving
    #   next node.
    #  -USEFUL FOR:
        #  -Solving a problem where you know the solution is very FAR
        #   from the root
        #  -Finding the ONE, correct solution amongst many
        #   #  -i.e. - finding the correct path in a maze
        #  -Traversing strongly connected components
    #  -REMEMBER:
        #  -***DFS NEVER revisits nodes
        #  -DFS requires LESS memory than BFS b/c not necessary to store
        #   all child pointers
        
    #  -STEPS FOR TRAVERSAL:
    #  (1)  Create a STACK to hold a list of nodes to explore
    #  (2)  Add starting vertex (s) to the STACK
    #  (3)  Start exploration, beginning with the starting vertex (s)
        #  (a) while there are unscheduled vertices that are one edge 
        #      away from the current vertex (moving DOWN the branch)...
            #  (i) schedule these adjacent vertices to be explored 
            #      by adding them to the STACK
    #  (4)  Mark vertex as 'explored' by removing it from the STACK
#  SIMILARITIES between BFS vs DFS
    #  -BFS (with a QUEUE) runtime complexity = O(n), 
    #   where "n" = # of nodes
    #  -BFS (with a QUEUE) space complexity = O(n), 
    #   because, worst case, you'll still need to hold 
    #   all the vertices in the queue.
    
    #  -DFS runtime complexity = O(n), where "V" = # of nodes
    #  -DFS (recursive with a QUEUE) space complexity = O(h), where 
    #   "h" = max depth of tree
    #  -DFS (iterative with a STACK) space complexity = O(n), where 
    #   "n" = # of nodes
    
#  BFS PROS
    #  -Great for finding the shortest path between a starting point
    #   and any other reachable node.
    #  -If a node of interest is likely at the upper level of the 
    #   tree/graph, BFS will be better/faster.
    
#  BFS CONS
    #  -Requires more memory than DFS.
    
#  DFS PROS
    #  -Requires LESS memory than BFS.
    #  -Better for determining if a path exists between two nodes.
    
#  DFS CONS
    #  -Traversal can get slow for large trees.
#  BFS vs DFS
#  If you know a solution is NOT far from the root of the tree: 
    #  BFS
    
#  If the tree is very deep and solutions are RARE: 
    #  BFS (because DFS will take too long)
    
#  If the tree is very WIDE:
    #  DFS (because BFS will need too much memory)
    
#  If solutions are frequent but located deep in the tree:
    #  DFS
    
#  Determining whether a path exists between two nodes: 
    #  DFS
    
#  Finding the shortest path:
    #  BFS