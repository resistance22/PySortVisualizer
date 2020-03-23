import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from Sorts import bubble_sort


class Bubble_sort_anim:
    def __init__(self,max):
        self._max = max
        self._fig = plt.figure()
        self._x = [x for x in range(0,max)]
        self._y = [2,5,6,2,31,24,9,8,3,10]
        self._plot = plt.bar(self._x,self._y)
        self._frame = max - 1
        self._anim = None


        figManager = plt.get_current_fig_manager()
        figManager.window.showMaximized()

    def start_anim(self):
        self._anim = FuncAnimation(self._fig, self.animate,frames=self._frame, interval=300,repeat=True)
        plt.show()


    def animate(self,i):
        for p in self._x:
            self._plot[p].set_color('b')
        if( i <= self._frame ):
            self._plot[i].set_color('r')
            self._plot[i+1].set_color('g')
            if( self._y[i] > self._y[i+1] ):
                self._y[i], self._y[i+1] = self._y[i + 1], self._y[i]
                self._plot[i].set_height(self._y[i])
                self._plot[i+1].set_height(self._y[i+1])
        if( i+1 == self._frame ):
            self._frame = self._frame - 1

        return self._plot







def main():
    anim1 = Bubble_sort_anim(10)
    anim1.start_anim()

if __name__ == "__main__" : main()
        
   




