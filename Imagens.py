import io
import os

import PySimpleGUI as sg
from PIL import Image

file_types = [("JPEG (*.jpeg)", "*.jpeg"),
              ("JPG (*.jpg)", "*.jpg"),
              ("PNG (*.png)", "*.png")]


def main():
    layout = [
        [sg.Image(key="-IMAGE-")],
        [
            sg.Text("Image File"),
            sg.Input(size=(25, 1), key="-FILE-"),
            sg.FileBrowse(file_types=file_types),
            sg.Button("Load Image"),
            sg.Button("Save")
        ],
    ]
    window = sg.Window("Image Viewer", layout)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "Load Image":
            # filename = values["-FILE-"]
            filename = "functions/images/1111.jpeg"
            if os.path.exists(filename):
                # images = Image.open(values["-FILE-"])
                image = Image.open(filename)
                image.thumbnail((180, 180))
                bio = io.BytesIO()
                image.save(bio, format='PNG')
                window["-IMAGE-"].update(data=bio.getvalue())
        elif event == 'Save':
            filename = "functions/images/1111.jpeg"
            image = Image.open(filename)
            image.save(fp='images/1112.jpeg', format='JPEG')

    window.close()


if __name__ == "__main__":
    main()
