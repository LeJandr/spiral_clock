import cmath
from math import log, pow

from PIL import Image

R, G, B = 0, 1, 2

if __name__ == '__main__':
    img = Image.open("clock.jpg")
    pixels = img.load()
    out = img.point(lambda i: 0)
    size_x = out.size[0]
    size_y = out.size[1]

    for x in range(size_x):
        if x % 100 == 0:
            print(x)
        for y in range(size_y):

            dx = -size_x / 2 + x
            dy = -size_y / 2 + y

            z = complex(dx, dy)
            w = cmath.polar(z)
            r = w[0]
            f = w[1] / cmath.tau

            # Get bounds of the normal turning:
            r_in = pow(2, f - 1) * size_x / 3.0
            r_out = pow(2, f) * size_x / 3.0

            # Get bounds of a current turning:
            if r > 2.0:
                scale = r / r_in
                scale = log(scale, 2)
                if scale > 0.0:
                    scale = int(scale)
                else:
                    scale = int(scale) - 1
                scale = pow(2.0, scale)
                r_in = r_in * scale
                r_out = r_out * scale

                if r_in < r <= r_out:
                    r_orig = (1 + (r - r_in) / (r_out - r_in)) * size_x/4
                    # NOTE: r_orig = (1 + 0..1) * size_x/4
                    # NOTE: r_orig = (1..2) * size_x/4
                    # NOTE: size_x/4 <= r_orig <= size_x/2
                    z_orig = cmath.rect(r_orig, f * cmath.tau)
                    x_orig = int(z_orig.real + size_x/2.0)
                    y_orig = int(z_orig.imag + size_x/2.0)
                    out.putpixel((x, y), pixels[x_orig, y_orig])
                else:
                    breakpoint()

    out.save("clock2.jpg")
    out = Image.open("clock2.jpg")
    out.show()
