import PySimpleGUI as sg
import numpy as np
from PIL import Image
import io
import re

from SliceObserver import SliceObserver


class SliceObserverGUI:

    def __init__(self, voxel: np.ndarray):

        self.sliceObserver = SliceObserver()
        self.sliceObserver.setVoxel(voxel)

        self.width = 500
        self.height = 500

        self.layout = [
            [sg.Text(key="-INDEX-", font=("Arial", 12), size=(20, 1), pad=(self.width // 5, 0))],
            [sg.Image(key="-IMAGE-", size=(self.width, self.height))],
            [
                sg.Button("Up", size=(14, 1)),
                sg.Button("Down", size=(14, 1)),
                sg.Input(size=(14, 1), key="-JUMPINDEX-"),
                sg.Button("Jump To", size=(14, 1))
            ]
        ]

        self.window = sg.Window("Voxel Slice Observer", self.layout)

        self.indexParameterPattern = re.compile("\\d+") # regex to accept only integers

        while True:

            event, values = self.window.read()

            if event == "Exit" or event == sg.WIN_CLOSED:
                break

            elif event == "Up":
                self.sliceObserver.incrementCurrentIndex()
            elif event == "Down":
                self.sliceObserver.decrementCurrentIndex()
            elif event == "Jump To":
                match = self.indexParameterPattern.search(values["-JUMPINDEX-"])

                if (match is not None):
                    self.sliceObserver.setCurrentIndex(int(match.group(0)))
                else:
                    pass # throw error or smth

            self.window["-INDEX-"].update("At Z-Index: {}".format(self.sliceObserver.getCurrentIndex()))

            # set the image from np array to a png encoding that pysimplegui accepts
            bio = io.BytesIO()
            curr_im = self.sliceObserver.getCurrentImage()
            im = Image.fromarray(self.sliceObserver.getCurrentImage(), mode="P")
            im_rsz = im.resize((self.width, self.height), resample=Image.NEAREST)
            im_rsz.save(bio, format="PNG")
            self.window["-IMAGE-"].update(data=bio.getvalue())

        self.window.close()
