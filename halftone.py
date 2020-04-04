from PIL import Image, ImageDraw
import numpy as np

def load_img(img_path, scale=1):
    """ Load image from img_path with PIL module and resize
    
    The image is loaded with Gray-scale.
    Full color version is not available for now.
    Args:
      img_path: A file path of target image for halftone process
      scale : A resize scale value (Default : 1, original size)
    Returns:
      A numpy image array
    """
    img = Image.open(img_path).convert('L')
    img = img.resize((int(img.width*scale), int(img.height*scale)))
    np_img = np.asarray(img)
    
    return np_img

def draw_halftone(np_img, dot_size=10, bg_color='white'):
    """ Draw halftone image from input image
    Args:
      np_img: A numpy image array which will be halftone processed
      dot_size : A size of halftone dot
      bg_color : A background color (white or black), dot color depends on this bg color 
    Returns:
      A PIL image with halftone process
    """
    
    width, height = np_img.shape
    
    if bg_color == 'black':
        dot_color = 255 # dot color is white
    elif bg_color == 'white':
        dot_color = 0 # dot color is black
    else:
        raise "I'm sorry, only black or white is available for bg_color."
    
    new_img = Image.new('L', (height, width), bg_color) # PIL image format is (height, width)
    draw = ImageDraw.Draw(new_img) # A new canvas for halftone process

    for i in range(0, width, dot_size):
        start = dot_size//2 if i%(dot_size*2) else 0 # For hexagonal dotting
        
        for j in range(start, height, dot_size):
            intensity = (np.mean(np_img[i:i+dot_size, j:j+dot_size])/255) # halftone dot size is determined by mean of box intensity
            if bg_color=='white':
                intensity = 1 - intensity # if backgrond color is white (dot color is black), intensity needs to inverse
                
            r = int((dot_size * intensity) ** .5)
            
            draw.ellipse([(j+dot_size//2)-r, (i+dot_size//2)-r, (j+dot_size//2)+r, (i+dot_size//2)+r], fill=dot_color)
            
    return new_img

def save_img(new_img, img_path):
    new_img.save(img_path)
    
    
if __name__ == '__main__':
    np_img = load_img('cat.png', 2)
    
    new_img = draw_halftone(np_img, bg_color='white')
    save_img(new_img, 'halftone_cat_w.jpg')
    
    new_img = draw_halftone(np_img, bg_color='black')
    save_img(new_img, 'halftone_cat_b.jpg')   