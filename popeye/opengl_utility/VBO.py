import OpenGL.GL as gl


class VBO:

    def __init__(self) -> None:
        self.id = gl.glGenBuffers(1)
        self.bind()

    def bind(self) -> None:
        gl.glBindBuffer(gl.GL_ARRAY_BUFFER, self.id)

    def set_data(self, size: int, data):
        self.bind()
        gl.glBufferData(gl.GL_ARRAY_BUFFER, size, data, gl.GL_DYNAMIC_DRAW)
    
    def update_data(self, offset: int, size: int, data):
        """
        Offset and size are to be specified as integers representing byte indices in the data store
        """
        self.bind()
        gl.glBufferSubData(gl.GL_ARRAY_BUFFER, offset, size, data)