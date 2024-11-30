class RoadProject:
    def __init__(self, identifier, priority, cost, area1, area2):
        self.identifier = identifier
        self.priority = priority
        self.cost = cost
        self.area1 = area1
        self.area2 = area2

    def __repr__(self):
        return f"{self.identifier} {self.priority} {self.cost} {self.area1} {self.area2}"


def sort_projects(projects):
    # Sort by priority (descending), and for equal priority by cost (ascending)
    return sorted(projects, key=lambda x: (-x.priority, x.cost))


def binary_search(projects, identifier):
    # Binary search for the project identifier
    projects = [p.identifier for p in projects]
    low, high = 0, len(projects) - 1
    while low <= high:
        mid = (low + high) // 2
        if projects[mid] == identifier:
            return mid
        elif projects[mid] < identifier:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def minimum_spanning_tree(projects):
    parent, rank = {}, {}
    areas = set()

    # Initialize Union-Find structure
    for p in projects:
        areas.update([p.area1, p.area2])
    for a in areas:
        parent[a], rank[a] = a, 0

    def find(area):
        if parent[area] != area:
            parent[area] = find(parent[area])
        return parent[area]

    def union(a, b):
        root1, root2 = find(a), find(b)
        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            elif rank[root1] < rank[root2]:
                parent[root1] = root2
            else:
                parent[root2] = root1
                rank[root1] += 1
            return True
        return False

    # Build MST
    mst_cost, edges_used = 0, 0
    for p in projects:
        if union(p.area1, p.area2):
            mst_cost += p.cost
            edges_used += 1
            if edges_used == len(areas) - 1:
                break
    return mst_cost


def main():
    # Predefined input
    projects = [
        RoadProject("road1", 4, 180, "A1", "A2"),
        RoadProject("road2", 3, 150, "A2", "A3"),
        RoadProject("road3", 5, 200, "A3", "A4"),
        RoadProject("road4", 4, 50, "A4", "A1"),
        RoadProject("road5", 5, 120, "A2", "A4"),
    ]

    # Sort the projects
    projects = sort_projects(projects)

    print("\nSorted list of projects:")
    for p in projects:
        print(p)

    # Search for a specific project
    identifier_to_search = "road4"  # Predefined identifier to search
    index = binary_search(projects, identifier_to_search)
    print(f"\n{identifier_to_search} found at position {index}" if index != -1 else f"\n{identifier_to_search} not found")

    


if __name__ == "__main__":
    main()