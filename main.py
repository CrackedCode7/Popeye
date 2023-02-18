import glfw
import OpenGL.GL as gl
import numpy as np
import json

from popeye.window import window_setup
from popeye.shaders.Shader import Shader
from popeye.fps_counter.fps_counter import FPS_Counter
from popeye.opengl_utility.VAO import VAO
from popeye.opengl_utility.VBO import VBO
from popeye.textures.Texture import Texture

from popeye.utility.get_filenames_in_directory import get_filenames_in_directory
from popeye.utility.merge_images import merge_images


def main():
    
    # Create window
    window = window_setup.create_window()
    if not window:
        return

    # Set up shader program
    shader = Shader("popeye/shaders/shader.vs", "popeye/shaders/shader.fs")
    shader.use()

    # Set up texture
    texture = Texture("popeye/textures/textures.png")
    texture.bind()
    with open("popeye/textures/texture_map.json", "r") as file:
        texture_map = json.load(file)
    #list_of_filenames = get_filenames_in_directory("popeye/textures/cards")
    #merge_images(list_of_filenames, "popeye/textures/test.png", "popeye/textures/texture_map.json", scale=1/4)

    # Items to draw
    vertices = np.array([
        0, 0, 0,
        125/182*9/16/2, 0, 0,
        125/182*9/16/2, 1/2, 0,
        0, 0, 0,
        125/182*9/16/2, 1/2, 0,
        0, 1/2, 0
    ],
    dtype = np.float32)

    card = "Sun Flower"

    tex_coords = np.array([
        texture_map[card][0], texture_map[card][2],
        texture_map[card][1], texture_map[card][2],
        texture_map[card][1], texture_map[card][3],
        texture_map[card][0], texture_map[card][2],
        texture_map[card][1], texture_map[card][3],
        texture_map[card][0], texture_map[card][3]
    ],
    dtype=np.float32)

    vao = VAO()
    vao.bind()

    vertex_vbo = VBO()
    vertex_vbo.set_data(
        vertices.size * vertices.itemsize,
        vertices.data
    )
    vao.set_vertex_data(vertex_vbo, 0, 3, gl.GL_FLOAT, gl.GL_FALSE, 0, None)

    tex_coords_vbo = VBO()
    tex_coords_vbo.set_data(
        tex_coords.size * tex_coords.itemsize,
        tex_coords.data
    )
    vao.set_vertex_data(tex_coords_vbo, 1, 2, gl.GL_FLOAT, gl.GL_FALSE, 0, None)

    '''tex_coords_vbo.update_data(int(tex_coords.size/2)*tex_coords.itemsize, int(tex_coords.size/2)*tex_coords.itemsize, np.array([
        0, 0,
        1, 0,
        1, 1
    ],dtype=np.float32).data)'''

    # Main loop
    fps_counter = FPS_Counter()
    while not glfw.window_should_close(window):

        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

        # Update framerate
        fps_counter.update(window)

        # Set shader
        shader.use()

        # Draw
        gl.glDrawArrays( gl.GL_TRIANGLES, 0, int(vertices.size / 3) )

        glfw.swap_buffers(window)
        glfw.poll_events()
    
    glfw.terminate()

    return


if __name__ == "__main__":
    main()