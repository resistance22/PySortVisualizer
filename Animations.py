import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class Bubble_sort_anim:
    def __init__(self,max,interval=200):
        self._max = max
        self._fig = plt.figure()
        self._x = [x for x in range(0,max)]
        self._y = np.random.randint(0,max*4,max)
        self._plot = plt.bar(self._x,self._y)
        self._frame = max - 1
        self._interval = interval
        self._anim = None

        #making The window appear fullScreen
        figManager = plt.get_current_fig_manager()
        figManager.window.showMaximized()



    def frame_generator(self):
        f = 0
        while f <= self._frame:
            yield f
            f += 1

    def start_anim(self):
        #Starting and then showing the plot animation
        self._anim = FuncAnimation(self._fig, self.animate,frames=self.frame_generator, interval=self._interval,repeat=True)
        plt.show()

    def stop_anim(self):
        self._anim.event_source.stop()

    def animate(self,i):
        #first setting all the Bars color to original Blue
        for p in self._x:
            self._plot[p].set_color('b')
        #The animation logic
        self._plot[i].set_color('r')
        self._plot[i+1].set_color('g')
        if( self._y[i] > self._y[i+1] ):
            self._y[i], self._y[i+1] = self._y[i + 1], self._y[i]
            self._plot[i].set_height(self._y[i])
            self._plot[i+1].set_height(self._y[i+1])
        #decresing the frame 
        if( i+1 == self._frame ):
            self._frame = self._frame - 1
        #Implementing the end logic
        if( self._frame == 0):
            for p in self._x:
                self._plot[p].set_color('g')
                self.stop_anim()

        return self._plot







def main():
    anim1 = Bubble_sort_anim(10)
    anim1.start_anim()

if __name__ == "__main__" : main()
        
   



