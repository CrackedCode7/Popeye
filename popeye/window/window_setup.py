import OpenGL.GL as gl
import glfw


window_size = [960, 540]


def framebuffer_size_callback(window, width, height):

    global window_size
    window_size = [width, height]
    
    gl.glViewport(0, 0, width, height)


def initialize_GLFW():

    if not glfw.init():
        return False
    
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, True)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    return True


def create_window():

    if not initialize_GLFW():
        print("Failed to initialize glfw")
        return None

    window = glfw.create_window(window_size[0], window_size[1], "Popeye", None, None)

    if window == None:
        print("Failed to create GLFW window")
        glfw.terminate()

    glfw.make_context_current(window)
    glfw.swap_interval(0)
    glfw.set_framebuffer_size_callback(window, framebuffer_size_callback)

    gl.glClearColor(0, 0, 0, 0)
    gl.glEnable(gl.GL_CULL_FACE)
    gl.glEnable(gl.GL_DEPTH_TEST)

    # Alpha blending
    gl.glEnable(gl.GL_BLEND)
    gl.glBlendFunc(gl.GL_SRC_ALPHA, gl.GL_ONE_MINUS_SRC_ALPHA)

    return window
    