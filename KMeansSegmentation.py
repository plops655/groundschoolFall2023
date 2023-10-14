import cv2
import numpy as np
import sklearn
from sklearn.cluster import KMeans
import pandas as pd

class KDominantColors:

    def __init__(self, colors = 3):
        self.colors = colors

    def RGBtoHSV(self, val):
        R, G, B = val
        R = R / 255.0
        G = G / 255.0
        B = B / 255.0
        max_color = max(R, G, B)
        min_color = min(R, G, B)
        diff = max_color - min_color

        if diff == 0:
            H = 0
        elif max_color == R:
            H = (60 * ((G - B) / diff) + 360) % 360
        elif max_color == G:
            H = (60 * ((B - R) / diff) + 120) % 360
        elif max_color == B:
            H = (60 * ((B - G) / diff) + 240) % 360
        if max_color == 0:
            S = 0
        else:
            S = (diff / max_color) * 100

        V = max_color * 100;

        return H, S, V

    def dominantColors(self, image):

        cv2_image = cv2.imread(image)


        RGB_img = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2RGB)
        RGB_img = RGB_img.reshape((RGB_img.shape[0] * RGB_img.shape[1], 3))
        kmeans = KMeans(n_clusters=self.colors)
        kmeans.fit(RGB_img)

        RGB_vals = kmeans.cluster_centers_.astype(int)
        dominant_colors = list()

        # S = 100
        # H ~
        # 340 - 359 Red  excp: 50 <= S <= 60 -> pink
        # 302-339 Pink
        # 255 - 301 Purple
        # 210 - 254 Blue
        # 173 - 210 Light Blue
        # 76 - 173 Green
        # 55 - 75 Yellow V <= 40 or S <= 40 -> green
        # 18 - 74 Orange
        # 0 - 17 Red excp: 20 <= S <= 30 -> brown

        # S = 50 or V = 50
        # H ~

        # V <= 20 -> Black
        # S <= 10, 20 <= V -> Gray


        # low-saturation == more girly


        for val in RGB_vals:
            H, S, V = self.RGBtoHSV(val)
            print([H, S, V])

            if H >= 350 or S <= 3 and V >= 97:
                dominant_colors.append("white")
            elif H <= 10:
                dominant_colors.append("black")
            elif V <= 20:
                dominant_colors.append("black")
            elif S <= 10 and V >= 20:
                dominant_colors.append("gray")
            elif 0 <= H <= 17:
                if 20 <= S <= 30:
                    dominant_colors.append("brown")
                else:
                    dominant_colors.append("red")
            elif 17 <= H <= 55:
                if S <= 40 and V < 50:
                    dominant_colors.append("green")
                elif V >= 50:
                    dominant_colors.append("brown")
                else:
                    dominant_colors.append("orange")
            elif 55 <= H <= 75:
                if V <= 40 or S <= 40:
                    dominant_colors.append("greenish yellow")
                else:
                    dominant_colors.append("yellow")
            elif 75 <= H <= 173:
                dominant_colors.append("green")
            elif 173 <= H <= 210:
                dominant_colors.append("light blue")
            elif 210 <= H <= 254:
                dominant_colors.append("blue")
            elif 254 <= H <= 301:
                dominant_colors.append("purple")
            elif 301 <= H <= 360:
                if 50 <= S <= 60:
                    dominant_colors.append("pink")
                else:
                    dominant_colors.append("red")

        return dominant_colors

if __name__ == "__main__":

    parse_dominant = KDominantColors()
    print(parse_dominant.dominantColors("./test_images/colortent.png"))