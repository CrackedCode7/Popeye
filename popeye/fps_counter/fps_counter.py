import glfw


class FPS_Counter:

    def __init__(self):

        self.previous_time = glfw.get_time()
        self.time = glfw.get_time()
        self.delta_time = glfw.get_time()
        self.last_update_time = glfw.get_time()

        self.frames = 0

    def update(self, window):

        self.time = glfw.get_time()
        self.delta_time = self.time - self.previous_time
        self.previous_time = self.time

        if (self.time - self.last_update_time >= 1):
            self.frames = 1 / self.delta_time
            glfw.set_window_title(window, "{:.0f}".format(self.frames))
            self.last_update_time = self.time