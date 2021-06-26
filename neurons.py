import numpy
import cv2
import argparse
import numpy as np

class Neurons:
    def __init__(self):
        pass
    def get_output_layers(self, net):
        layer_names = net.getLayerNames()
        output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
        return output_layers
    def whatIsIt(self, path):
        image = cv2.imread(path)
        scale = 0.00392
        classes = None
        with open("yolov3.txt", 'r') as f:
            classes = [line.strip() for line in f.readlines()]
        net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
        blob = cv2.dnn.blobFromImage(image, scale, (608, 608), (0, 0, 0), True, crop=False)
        net.setInput(blob)
        outs = net.forward(self.get_output_layers(net))
        class_ids = []
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.2:
                    class_ids.append(class_id)
        y = [classes[ids] for ids in  class_ids]
        print(y)
        x = [0, 0, 0, 0, 0]
        if "kruche" in y:
            x[1]=1
        elif "niebezpieczne" in y:
            x[4]=1
        elif "biohazard" in y:
            x[4]=1
        elif "radioaktywne" in y:
            x[3]=1
        elif "latwopalne" in y:
            x[2]=1
        else:
            x[0]=1
        print(x)
        if x[0]==1:
            print("Zwykła")
        if x[1]==1:
            print("Kruchy")
        if x[2]==1:
            print("Łatwopalny")
        if x[3]==1:
            print("Radioaktywny")
        if x[4]==1:
            print("Niebezpieczny")
        return [list(x)]
