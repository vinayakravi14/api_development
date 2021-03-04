import cv2
import numpy as np
import os
from sklearn.cluster import KMeans, MiniBatchKMeans
from sklearn.feature_extraction import image

from helpers.utility import import_data
import matplotlib.pyplot as plt
from scipy import ndimage
from sklearn.mixture import GaussianMixture


class ImageManipulation:

    def __init__(self):

        self.resize_windows = 0.2

        self.frame_num = 1
        self.border = 25
        self.erosion_size = 0
        self.max_elem = 2
        self.max_kernel_size = 21
        self.size = 8
        self.no_of_clusters = 1
        self.feature_list = []

    def detect_corners(self, img_input, thr: int):

        gray = cv2.cvtColor(img_input, cv2.COLOR_BGR2GRAY)

        ret, thresh = cv2.threshold(
            gray, thr, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

        # removing noise by image morphological operations
        kernel = np.ones((3, 3), np.uint8)
        opening = cv2.morphologyEx(
            thresh, cv2.MORPH_OPEN, kernel, iterations=2)

        # Finding bg area
        sure_bg = cv2.dilate(opening, kernel, iterations=3)

        # Finding fg area
        dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
        ret, sure_fg = cv2.threshold(
            dist_transform, 0.7*dist_transform.max(), 255, 0)

        # Finding unknown region
        sure_fg = np.uint8(sure_fg)
        unknown = cv2.subtract(sure_bg, sure_fg)

        # Marker labelling
        ret, markers = cv2.connectedComponents(sure_fg)

        # Add one to all labels so that sure background is not 0, but 1
        markers = markers+1

        # Now, mark the region of unknown with zero
        markers[unknown == 255] = 0
        markers = cv2.watershed(img_input, markers)

        img_input[markers == -1] = [255, 0, 0]
        return img_input

    def kmeans_clustering(self, img_input: str, num_of_clusters: int, thresh: int):

        rz = img_input.reshape((img_input.shape[1]*img_input.shape[0], 3))
        z = img_input.reshape((-1, 3))
        z = np.float32(z)
        n_clusters = num_of_clusters
        kmeans = KMeans(n_clusters=num_of_clusters)
        s = kmeans.fit(rz)

        labels = kmeans.labels_
        labels = list(labels)

        centroid = kmeans.cluster_centers_

        percent = []
        for i in range(len(centroid)):
            j = labels.count(i)
            j = j/(len(labels))
            percent.append(j)

        # 100 is the no.of iterations in which it will stop, 0.2 is to adjust the clusters moving
        criteria = (cv2.TERM_CRITERIA_EPS +
                    cv2.TermCriteria_MAX_ITER, 100, 0.5)

        ret, label, center = cv2.kmeans(
            z, num_of_clusters, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

        # convert back to uint8 and make org image
        center = np.uint8(center)
        res = center[label.flatten()]
        res2 = res.reshape((img_input.shape))

        norm_img = cv2.normalize(
            res2, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
        # colorIR = cv2.applyColorMap(norm_img, cv2.COLORMAP_JET)
        kernel = np.ones((5, 5), np.uint8)
        norm_img = cv2.filter2D(norm_img, -1, kernel)
        brightBlurIR = cv2.bilateralFilter(norm_img, 9, 150, 150)

        # brightBlurIR = brightBlurIR[20:620, 0:480]
        retval, threshIR = cv2.threshold(
            brightBlurIR, thresh, 255, cv2.THRESH_BINARY)

        stacked = np.hstack([img_input, res2])

        return res2

    def auto_canny(self, img_input: str, sigma: float):
        # framename = self.frames_path + self.all_frames[self.frame_num]
        # im = cv2.imread(img_input)
        im = cv2.cvtColor(img_input, cv2.COLOR_RGB2GRAY)
        blurred = cv2.GaussianBlur(im, (3, 3), 0)

        # compute the median of the single channel pixel intensities
        v = np.median(img_input)

        # auto apply Canny edge detectiom using the computed median
        lower = int(max(0, (1.0 - sigma) * v))
        upper = int(min(255, (1.0 + sigma) * v))
        # edged = cv2.Canny(img_input, lower, upper)

        wide = cv2.Canny(blurred, 10, 200)
        tight = cv2.Canny(blurred, 225, 250)
        auto = cv2.Canny(img_input, lower, upper)

        return auto
