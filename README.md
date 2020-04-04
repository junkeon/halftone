# Gray scale halftone

It is a simple gray scale halftone effect codes.

You can make halftone processed image with this code.


## Basic usage

You need Numpy and [Pillow][pillow] modules to run this code.

Please make sure that Numpy and pillow module is available in your environment.

```
from halftone import load_img, draw_halftone, save_img

np_img = load_img('/path/to/myimage.jpg')
new_img = draw_halftone(np_img)
save_img(new_img, '/path/to/saveimg.jpg')
```

## Options

There are a number of options to control size of image or halftone options

- scale

```
np_img = load_img('/path/to/myimage.jpg', scale = 3)
```

If you think target image is too small for current dot size, you can upscale the image.
The scale value(default is 1) is for resize the image.

- dot_size

```
new_img = draw_halftone(np_img, dot_size=10)
```

The variable dot_size is size of halftone dot. You can control the size of halftone with this variable.
If dot_size is too small, the dots will be too fine and too small. If dot_size is too big, original image will be not clear.
So I recommand you to set the dot size bigger than 10 and control load image scale.

- bg_color

```
new_img = draw_halftone(np_img, bg_color='white')
```

You can change background color. If bg_color is white, then halftone dot will be processed with black dot and vice versa.


## Examples

### Original image

![Original image](examples/cat.jpg?raw=True)

### Halftone with white background

![white halftone image](examples/halftone_cat_white.jpg?raw=True)

### Halftone with black background

![black halftone image](examples/halftone_cat_black.jpg?raw=True)