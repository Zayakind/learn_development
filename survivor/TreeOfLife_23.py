
class Tree:
    def __init__(self, layers: list):
        self.tree = [
            [1 if i == "+" else 0 for i in layer]
            for layer in layers
        ]

    def to_string(self):
        return [
            "".join(["+" if i == 1 else "." for i in layer])
            for layer in self.tree
        ]

    def even_year(self):
        self.tree = [
            [i + 1 for i in layer] for layer in self.tree
        ]

    def odd_year(self, rows: int, cols: int):
        branch_to_destroy = []
        for i, layer in enumerate(self.tree):
            for j, branch in enumerate(layer):
                if branch >= 3:
                    branch_to_destroy.append((i, j))

        temp_coords = []
        for coord in branch_to_destroy:
            i, j = coord[0], coord[1]
            for shift in [1, -1]:
                if 0 <= i + shift <= rows - 1:
                    temp_coords.append(
                        (i + shift, j)
                    )
                if 0 <= j + shift <= cols - 1:
                    temp_coords.append(
                        (i, j + shift)
                    )
        branch_to_destroy.extend(temp_coords)
        coords_destroy = set(branch_to_destroy)

        for coord in coords_destroy:
            i, j = coord[0], coord[1]
            self.tree[i][j] = 0


def TreeOfLife(height: int, width: int, years: int, tree: list[str]):
    tree = Tree(tree)
    for year in range(years):
        tree.even_year() if year % 2 == 0 else tree.odd_year(height, width)
    return tree.to_string()
