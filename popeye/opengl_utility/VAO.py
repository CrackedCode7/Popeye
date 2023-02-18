import OpenGL.GL as gl

from popeye.opengl_utility import VBO


class VAO:

    def __init__(self) -> None:
        self.id = gl.glGenVertexArrays(1)
        self.bind()

    def bind(self) -> None:
        gl.glBindVertexArray(self.id)

    def set_vertex_data(
        self,
        vbo: VBO,
        attribute_index: int,
		size: int,
		type, # GLenum type, can be gl.GL_FLOAT, gl.GL_INT, etc.
		normalized: bool,
		stride: int,
		pointer: None
    ) -> None:
        
        self.bind()
        vbo.bind()
        gl.glVertexAttribPointer(
            attribute_index,
            size,
            type,
            normalized,
            stride,
		    pointer
	    )
        gl.glEnableVertexAttribArray(attribute_index)
