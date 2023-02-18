import numpy as np
import OpenGL.GL as gl
from PIL import Image, ImageOps


class Texture:
    """
    Loads a texture from a file and provides necessary binding function for OpenGL

    From paint.net, save as 32-bit depth
    """

    def __init__(self, filename):

        self.id = gl.glGenTextures(1)
        self.bind()

        gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_REPEAT)
        gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_REPEAT)
        gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)
        gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)

        self.img = ImageOps.flip(Image.open(filename))
        self.img_data = np.array(list(self.img.getdata()), np.int8)
        gl.glTexImage2D(
            gl.GL_TEXTURE_2D, 
            0, 
            gl.GL_RGBA, 
            self.img.size[0], 
            self.img.size[1], 
            0, 
            gl.GL_RGBA, 
            gl.GL_UNSIGNED_BYTE, 
            self.img_data
        )
        gl.glGenerateMipmap(gl.GL_TEXTURE_2D)

        # Free memory
        del self.img
        del self.img_data
        
    def bind(self):
        gl.glBindTexture(gl.GL_TEXTURE_2D, self.id)