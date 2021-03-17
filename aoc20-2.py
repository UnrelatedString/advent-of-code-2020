from random import choice

class Tile:
    def __init__(self, grid, tile_id = 0):
        self.grid = grid
        self.rotation = 0 # cw
        self.reflection = False # HORIZONTAL
        self.id = tile_id

    @property
    def rv(self):
        return (-1)**self.reflection

    def rotated(self, rotation, reflection):
        new = Tile(self.grid, self.id)
        new.rotation = rotation + self.rotation #* self.rv
        new.reflection = reflection ^ self.reflection
        return new

    def rotated_to(self, direction, matched_side, reflection):
        reflection ^= self.reflection
        if reflection:
            direction ^= (direction&1)<<1
        rotation = 2 + direction - matched_side
        return self.rotated(rotation, reflection)

    @property
    def rotated_grid(self):
        grid = self.grid
        for _ in range(self.rotation):
            grid = [*zip(*grid[::-1])]
        return [''.join(row[::self.rv]) for row in grid]

    def __str__(self):
        return f'Tile {self.id}:\n'+'\n'.join(self.rotated_grid)

    def side(self, n):
        if self.reflection:
            n ^= (n&1)<<1
        n -= self.rotation
        n %= 4
        if n == 0:
            return self.grid[0][::self.rv]
        elif n == 1:
            return ''.join(row[-1] for row in self.grid)[::-self.rv]
        elif n == 2:
            return self.grid[-1][::-self.rv]
        elif n == 3:
            return ''.join(row[0] for row in self.grid[::-1])[::-self.rv]
        else:
            assert False

tiles_by_id = {}

with open(input('Input file: ')) as f:
    ls = list(f)
lgs = '\n'.join(l.rstrip('\n') for l in ls).rstrip('\n').split('\n\n')
for lg in lgs:
    n, *grid = lg.split('\n')
    tile_id = int(n[5:-1])
    tiles_by_id[tile_id] = Tile(grid, tile_id)

id_adjacencies = {tile_id: [None, None, None, None] for tile_id in tiles_by_id}
ids_by_unmatched_sides = {}

for tile_id in tiles_by_id:
    tile = tiles_by_id[tile_id]
    for n in range(4):
        side = tile.side(n)
        if side in ids_by_unmatched_sides:
            match_id, match_side = ids_by_unmatched_sides.pop(side)
            id_adjacencies[tile_id][n] = (match_id, match_side, False)
            id_adjacencies[match_id][match_side] = (tile_id, n, False)
        elif side[::-1] in ids_by_unmatched_sides:
            match_id, match_side = ids_by_unmatched_sides.pop(side[::-1])
            id_adjacencies[tile_id][n] = (match_id, match_side, True)
            id_adjacencies[match_id][match_side] = (tile_id, n, True)
        else:
            ids_by_unmatched_sides[side] = (tile_id, n)

tiles_by_coordinates = {(0,0): choice([*tiles_by_id.values()])}
unvisited = {(0,0)}
visited = set()

while unvisited:
    x, y = unvisited.pop()
    tile = tiles_by_coordinates[(x, y)]
    visited.add((x, y))
    for direction, match in enumerate(id_adjacencies[tile.id]):
        if match is None:
            continue
        neighbor_id, matched_side, reflection = match
        dx, dy = ((0,1),(1,0),(0,-1),(-1,0))[direction]
        new_coords = x + dx, y + dy
        if new_coords in visited:
            new_tile = tiles_by_id[neighbor_id].rotated_to(direction, matched_side, reflection ^ tile.reflection)
            if new_tile.rotated_grid != tiles_by_coordinates[new_coords].rotated_grid:
                print(new_tile)
                print(tiles_by_coordinates[new_coords])
                print(new_coords)
                assert False
            continue
        unvisited.add(new_coords)
        new_tile = tiles_by_id[neighbor_id].rotated_to(direction, matched_side, reflection ^ tile.reflection)
        tiles_by_coordinates[new_coords] = new_tile
