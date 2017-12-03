from PIL import Image

class Color:
    def __init__(self, red: int, green: int, blue: int):
        self._color = (red, green, blue)

    def __eq__(self, other: Color) -> bool:
        return self._color == other._color

class PixelCheck:
    def find_matching_pixels(self, image: Image, color: Color) -> [(int, int)]:
        width, height = image.size
        self.find_matching_pixels_in_boundary(image, color, 0, 0, width, height)

    def find_matching_pixels_in_boundary(self, image: Image, color: Color, min_x: int, max_x: int, min_y: int, max_y: int) -> [(int, int)]:
        'min_x and min_y are inclusive, max_x and max_y are exclusive'

        matched_coordinates = []

        for x in range(min_x, max_x):
            for y in range(min_y, max_y):
                if self.get_pixel_color_at_coordinate(image, x, y) == color:
                    matched_coordinates.append((x, y))

        return matched_coordinates


    def get_pixel_color_at_coordinate(self, image: Image, x: int, y: int) -> Color:
        pixel_access = image.load()
        r, g, b = pixel_access[(x, y)]

        return Color(r, g, b)
