import OpenGL.GL as gl
from OpenGL.GL import GL_VERTEX_SHADER, GL_FRAGMENT_SHADER


class Shader:

    def __init__(self, vertex_shader_file, fragment_shader_file):

        self.id = gl.glCreateProgram()

        vertex_shader = self.load_shader(vertex_shader_file, gl.GL_VERTEX_SHADER)
        fragment_shader = self.load_shader(fragment_shader_file, gl.GL_FRAGMENT_SHADER)

        gl.glAttachShader(self.id, vertex_shader)
        gl.glAttachShader(self.id, fragment_shader)

        gl.glLinkProgram(self.id)

        # Check for linking errors
        success = gl.glGetProgramiv(self.id, gl.GL_LINK_STATUS)
        if not success:
            error_message = gl.glGetProgramInfoLog(self.id)
            print("ERROR::SHADER::PROGRAM::LINKING_FAILED\n", error_message, sep="")

        gl.glDeleteShader(vertex_shader)
        gl.glDeleteShader(fragment_shader)

    def load_shader(self, shader_file, shader_type):

        with open(shader_file, 'r') as file:
            shader_source = file.read()

        shader = gl.glCreateShader(shader_type)
        gl.glShaderSource(shader, shader_source)
        gl.glCompileShader(shader)
        # Error checking
        success = gl.GLint()
        gl.glGetShaderiv(shader, gl.GL_COMPILE_STATUS, success)
        if not success:
            error_message = gl.glGetShaderInfoLog(shader)
            print("ERROR::SHADER::", shader_type, "::COMPILATION_FAILED\n", error_message, sep="")

        return shader

    def use(self):
        gl.glUseProgram(self.id)