from util.Assets import Assets
from util.Collisions import Collision
from game.object.Object import Object
from game.component.Collider import Collider
import pygame as p


class TileMap:

    tile_size = 32
    map_data = []
    objects = []

    @staticmethod
    def clear():
        TileMap.map_data.clear()
        TileMap.objects.clear()

    @staticmethod
    def set_level(level):
        with open(f"assets/levels/{level}.txt", "r") as file:
            for line in file:
                TileMap.map_data.append([tile for tile in line.split()])

        i = 0

        for y, row in enumerate(TileMap.map_data):

            new_row = []

            for x, tile in enumerate(row):

                if tile != '0':
                    obj = Object(str(i))
                    collider = Collider(obj)
                    collider.set_rect(p.Rect(0, 0, TileMap.tile_size, TileMap.tile_size), (0, 0))
                    collider.set_layer("TERRAIN")
                    obj.add_component(collider)
                    obj.transform.set_position((x * TileMap.tile_size, y * TileMap.tile_size))
                    obj.transform.set_static(True)
                    Collision.add(obj)
                    new_row.append(obj)

                else:
                    new_row.append(None)

                i += 1

            TileMap.objects.append(new_row)

    @staticmethod
    def render(surface):
        for y, row in enumerate(TileMap.map_data):
            for x, tile in enumerate(row):
                if tile == '0':
                    continue
                tile = Assets.get_image(f"assets/tiles/{tile}.png")
                surface.blit(tile, (x * TileMap.tile_size, y * TileMap.tile_size))

    @staticmethod
    def set_tile(x, y, tile):
        x, y = x - 1, y - 1

        if TileMap.map_data[y][x] == tile:
            return

        TileMap.map_data[y][x] = tile

        if tile == '0':
            Collision.remove(TileMap.objects[y][x])

        else:
            obj = Object(f"{x}, {y}")
            collider = Collider(obj)
            collider.set_rect(p.Rect(0, 0, TileMap.tile_size, TileMap.tile_size), (0, 0))
            collider.set_layer("TERRAIN")
            obj.add_component(collider)
            obj.transform.set_position((x * TileMap.tile_size, y * TileMap.tile_size))
            obj.transform.set_static(True)
            Collision.add(obj)

            TileMap.objects[y][x] = obj
