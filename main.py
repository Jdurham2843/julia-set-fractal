from PIL import Image

WIDTH, HEIGHT = 1080, 720
MIN, MAX = -1, 1
THRESHOLD = 2
DISTANCE = abs(MIN) + MAX

def generate(pix):
    for wi in range(0, WIDTH):
        real = pixel_start_value_x(wi)
        for yi in range(0, HEIGHT):
            img = pixel_start_value_y(yi)
            count = 0
            z = f(complex(real, img))
            while abs(z) < THRESHOLD and count < 255:
                z = f(z)
                count += 1
            pix[wi, yi] = count

def pixel_start_value_x(i: int) -> float:
    return MIN + ((i * DISTANCE) / WIDTH)

def pixel_start_value_y(i: int) -> float:
    return MAX - ((i * DISTANCE) / HEIGHT)

def f(val: float):
    return (val * val) - complex(0.221, 0.713)

if __name__ == '__main__':
    image = Image.new('L', (WIDTH, HEIGHT))
    pix = image.load()
    generate(pix)
    image.save('fractal.png')
        



