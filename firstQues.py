def maximum_movies(n, preferences):
    # Create an adjacency list to represent the graph
    graph = [[] for _ in range(n)]
    for i in range(n):
        graph[i] = [int(x) - 1 for x in preferences[i]]  # Convert to 0-based indexing

    # Array to store which superstar is matched with whom
    match = [-1] * n  # -1 means not matched

    # DFS to find a match for a superstar
    def find_match(superstar, visited):
        for partner in graph[superstar]:
            if not visited[partner]:  # If this partner has not been visited
                visited[partner] = True  # Mark this partner as visited
                # Check if the partner is not matched or can be rematched
                if match[partner] == -1 or find_match(match[partner], visited):
                    match[partner] = superstar
                    return True
        return False

    # Try to find matches for each superstar
    max_movies = 0
    for superstar in range(n):
        visited = [False] * n  # Reset visited for each DFS
        if find_match(superstar, visited):
            max_movies += 1

    return max_movies // 2  # Each movie involves 2 superstars, so divide by 2


# Input
n = 4  # Number of superstars
preferences = [
    "2 3",  # Superstar 1 wants to work with 2 and 3
    "1 4",  # Superstar 2 wants to work with 1 and 4
    "1 4",  # Superstar 3 wants to work with 1 and 4
    "2 3"   # Superstar 4 wants to work with 2 and 3
]

# Convert preferences into a format for processing
preferences = [line.split() for line in preferences]

# Call the function and print the output
print(maximum_movies(n, preferences))
