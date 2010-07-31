#!/usr/bin/python
# -*- coding: utf-8 -*-

#        Copyright (C) 2009 Daniel Fett
#         This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#        Author: Daniel Fett advancedcaching@fragcom.de
#


import openstreetmap

import logging
logger = logging.getLogger('abstractmap')
import geo
import math




class AbstractMapLayer():
    def __init__(self):
        self.result = None

    def draw(self):
        pass

    def clicked_screen(self, screenpoint):
        pass

    def clicked_coordinate(self, center, topleft, bottomright):
        pass

    def resize(self):
        pass

    def attach(self, map):
        self.map = map

class AbstractMap():
    MAP_FACTOR = 0
    RADIUS_EARTH = 6371000.0

    @classmethod
    def set_config(Map, map_providers, map_path, placeholder_cantload, placeholder_loading):

        Map.noimage_cantload = Map._load_tile(placeholder_cantload)
        Map.noimage_loading = Map._load_tile(placeholder_loading)
        Map.tile_loaders = []

        for name, params in map_providers:
            tl = openstreetmap.get_tile_loader( ** params)
            tl.noimage_loading = Map.noimage_loading
            tl.noimage_cantload = Map.noimage_cantload
            tl.base_dir = map_path
            #tl.gui = self
            Map.tile_loaders.append((name, tl))

    def __init__(self, center, zoom, tile_loader = None):
        self.active_tile_loaders = []
        self.double_size = False
        self.layers = []
        self.osd_message = None

        if tile_loader == None:
            self.tile_loader = self.tile_loaders[0][1]
        else:
            self.tile_loader = tile_loader
        self.dragging = False
        self.drag_offset_x = 0
        self.drag_offset_y = 0
        self.zoom = zoom
        self.total_map_width = 256 * 2 ** zoom
        self.set_center(center, False)
        #self.set_zoom(zoom)

        ##############################################
        #
        # Controlling the layers
        #
        ##############################################

    def add_layer(self, layer):
        self.layers.append(layer)
        layer.attach(self)


    def set_osd_message(self, message):
        self.osd_message = message

        ##############################################
        #
        # Controlling the map view
        #
        ##############################################

    def set_center(self, coord, update = True):
        if self.dragging:
            return
        self.map_center_x, self.map_center_y = self.deg2num(coord)
        self.center_latlon = coord
        self.draw_at_x = 0
        self.draw_at_y = 0
        if update:
            self._draw_map()

    def set_center_lazy(self, coord):
        if self.dragging:
            return
        old_center_x, old_center_y = self.coord2point(self.center_latlon)
        new_center_x, new_center_y = self.coord2point(coord)

        if abs(old_center_x - new_center_x) > \
            self.map_width * self.LAZY_SET_CENTER_DIFFERENCE or \
            abs(old_center_y - new_center_y) > \
            self.map_height * self.LAZY_SET_CENTER_DIFFERENCE:
            self.set_center(coord)
            logger.debug('Not lazy!')
            return True
        logger.debug('Lazy!')
        return False


    def get_center(self):
        return self.center_latlon

    def relative_zoom(self, direction=None):
        if direction != None:
            self.set_zoom(self.zoom + direction)


    def set_zoom(self, newzoom):
        if newzoom < 1 or newzoom > self.tile_loader.MAX_ZOOM:
            return
        logger.debug('New zoom level: %d' % newzoom)
        self.zoom = newzoom
        self.total_map_width = (256 * 2**self.zoom)
        self.set_center(self.center_latlon)

    def get_zoom(self):
        return self.zoom

    def get_max_zoom(self):
        return self.tile_loader.MAX_ZOOM

    def get_min_zoom(self):
        return 0

    def _move_map_relative(self, offset_x, offset_y):
        self.map_center_x += (float(offset_x) / self.tile_loader.TILE_SIZE)
        self.map_center_y += (float(offset_y) / self.tile_loader.TILE_SIZE)
        self.map_center_x, self.map_center_y = self.check_bounds(self.map_center_x, self.map_center_y)
        self.center_latlon = self.num2deg(self.map_center_x, self.map_center_y)

        ##############################################
        #
        # Marker handling
        #
        ##############################################

    def add_marker_type(self, type):
        self.marker_types.append(type)

    def del_all_markers(self):
        for x in self.marker_types:
            x.del_all_markers()


        ##############################################
        #
        # Configuration
        #
        ##############################################

    def set_double_size(self, ds):
        self.double_size = ds

    def get_double_size(self):
        return self.double_size

    def set_tile_loader(self, loader):
        self.tile_loader = loader
        self.emit('tile-loader-changed', loader)
        self.relative_zoom(0)

    def set_placeholder_images(self, cantload, loading):
        self.noimage_cantload = self._load_tile(cantload)
        self.noimage_loading = self._load_tile(loading)

        ##############################################
        #
        # Coordinate Conversion and Checking
        #
        ##############################################

    def point_in_screen(self, point):
        a = (point[0] >= 0 and point[1] >= 0 and point[0] < self.map_width and point[1] < self.map_height)
        return a

    def coord2point(self, coord):
        point = self.deg2num(coord)
        size = self.tile_loader.TILE_SIZE
        p_x = int(point[0] * size + self.map_width / 2) - self.map_center_x * size
        p_y = int(point[1] * size + self.map_height / 2) - self.map_center_y * size
        return (p_x % self.total_map_width , p_y)

    def screenpoint2coord(self, point):
        size = self.tile_loader.TILE_SIZE
        coord = self.num2deg(\
                                ((point[0] - self.draw_root_x - self.draw_at_x) + self.map_center_x * size - self.map_width / 2) / size, \
                                ((point[1] - self.draw_root_y - self.draw_at_y) + self.map_center_y * size - self.map_height / 2) / size \
                                )
        return coord

    def get_visible_area(self):
        return (self.screenpoint2coord((0, 0)), self.screenpoint2coord((self.map_width, self.map_height)))


        ##############################################
        #
        # Tile Number calculations
        #
        ##############################################
    def tile_size(self):
        return self.tile_loader.TILE_SIZE

    def get_meters_per_pixel(self, lat):
        return math.cos(lat * math.pi / 180.0) * 2.0 * math.pi * self.RADIUS_EARTH / self.total_map_width

    def deg2tilenum(self, lat_deg, lon_deg):
        lat_rad = math.radians(lat_deg)
        n = 2 ** self.zoom
        xtile = int((lon_deg + 180) / 360 * n)
        ytile = int((1.0 - math.log(math.tan(lat_rad) + (1.0 / math.cos(lat_rad))) / math.pi) / 2.0 * n)
        return(xtile, ytile)

    def deg2num(self, coord):
        lat_rad = math.radians(coord.lat)
        n = 2 ** self.zoom
        xtile = (coord.lon + 180.0) / 360 * n
        ytile = (1.0 - math.log(math.tan(lat_rad) + (1.0 / math.cos(lat_rad))) / math.pi) / 2.0 * n
        return(xtile, ytile)

    def num2deg(self, xtile, ytile):
        n = 2 ** self.zoom
        lon_deg = xtile / n * 360.0 - 180.0
        lat_rad = math.atan(math.sinh(math.pi * (1 - 2 * ytile / n)))
        lat_deg = lat_rad * 180.0 / math.pi
        return geo.Coordinate(lat_deg, lon_deg)

    def check_bounds(self, xtile, ytile):
        max_x = 2**self.zoom
        max_y = 2**self.zoom
        return (
            xtile % max_x,
            ytile % max_y
        )