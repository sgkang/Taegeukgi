import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge
import scipy


class Taegeukgi(object):
    """
        Generating Figure for taegeukgi
    """
    def __init__(self, width, **kwargs):
        self.width = width
        self.height = 2./3.*self.width


    def run(self):

        radius = self.height*0.25
        radiusS = self.height*0.125
        costheta = 3./np.sqrt(13)
        sintheta = 2./np.sqrt(13)

        width = self.width
        height = self.height

        points_bar = np.array([[-radius/24, -radius/2], [radius/24, -radius/2], [radius/24, radius/2], [-radius/24, radius/2]])
        points_bar_tr1 = genbar(180/np.pi*np.arctan(2./3), \
                                points_bar, np.r_[(radius*1.5+1./12*radius)*costheta, (radius*1.5+1./12*radius)*sintheta])
        points_bar_tr2 = genbar(180/np.pi*np.arctan(2./3), \
                                points_bar, np.r_[(radius*1.5+3./12*radius)*costheta, (radius*1.5+3./12*radius)*sintheta])
        points_bar_tr3 = genbar(180/np.pi*np.arctan(2./3), \
                                points_bar, np.r_[(radius*1.5+5./12*radius)*costheta, (radius*1.5+5./12*radius)*sintheta])

        points_sbar = np.array([[-radius/20, -radius/24], [radius/20, -radius/24], [radius/20, radius/24], [-radius/20, radius/24]])
        points_sbar_tr1 = genbar(180/np.pi*np.arctan(2./3), \
                                points_sbar, np.r_[(radius*1.5+1./12*radius)*costheta, (radius*1.5+1./12*radius)*sintheta])
        points_sbar_tr2 = genbar(180/np.pi*np.arctan(2./3), \
                                points_sbar, np.r_[(radius*1.5+3./12*radius)*costheta, (radius*1.5+3./12*radius)*sintheta])
        points_sbar_tr3 = genbar(180/np.pi*np.arctan(2./3), \
                                points_sbar, np.r_[(radius*1.5+5./12*radius)*costheta, (radius*1.5+5./12*radius)*sintheta])


        fig = plt.figure(figsize = (4*3/2, 4))
        ax = fig.add_subplot(111)

        circle = dual_half_circle((0, 0), radius)
        circleL = plt.Circle((-0.5*radius*costheta, 0.5*radius*sintheta), radiusS, color='red')
        circleR = plt.Circle((0.5*radius*costheta, -0.5*radius*sintheta), radiusS, color='blue')
        bar1_1 = plt.Polygon(points_bar_tr1, color="black")
        bar1_2 = plt.Polygon(points_bar_tr2, color="black")
        bar1_3 = plt.Polygon(points_bar_tr3, color="black")

        bar2_1 = plt.Polygon(symmove(points_bar_tr1,'x'), color="black")
        bar2_2 = plt.Polygon(symmove(points_bar_tr2,'x'), color="black")
        bar2_3 = plt.Polygon(symmove(points_bar_tr3,'x'), color="black")

        bar3_1 = plt.Polygon(symmove(points_bar_tr1,'y'), color="black")
        bar3_2 = plt.Polygon(symmove(points_bar_tr2,'y'), color="black")
        bar3_3 = plt.Polygon(symmove(points_bar_tr3,'y'), color="black")

        bar4_1 = plt.Polygon(symmove(points_bar_tr1,'xy'), color="black")
        bar4_2 = plt.Polygon(symmove(points_bar_tr2,'xy'), color="black")
        bar4_3 = plt.Polygon(symmove(points_bar_tr3,'xy'), color="black")

        sbar1_1 = plt.Polygon(points_sbar_tr1, color="white")
        sbar1_3 = plt.Polygon(points_sbar_tr3, color="white")
        sbar3_1 = plt.Polygon(symmove(points_sbar_tr1,'y'), color="white")
        sbar3_2 = plt.Polygon(symmove(points_sbar_tr2,'y'), color="white")
        sbar3_3 = plt.Polygon(symmove(points_sbar_tr3,'y'), color="white")
        sbar4_2 = plt.Polygon(symmove(points_sbar_tr2,'xy'), color="white")

        ax.set_xlim(-0.5*width, 0.5*width)
        ax.set_ylim(-0.5*height,0.5*height)

        line = plt.Polygon([[-width*0.5, -height*0.5], [width*0.5, -height*0.5], [width*0.5, height*0.5], [-width*0.5, height*0.5]] \
                           ,fill=None, edgecolor = 'black')

        polygons = [line, circle[0],circle[1], circleL, circleR, bar1_1, bar1_2, bar1_3,\
                    bar2_1, bar2_2, bar2_3, bar3_1, bar3_2, bar3_3, bar4_1, bar4_2, bar4_3,\
                    sbar1_1, sbar1_3, sbar3_1, sbar3_2, sbar3_3, sbar4_2]

        for poly_temp in polygons:
            ax.add_patch(poly_temp)
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        fig.savefig('Taegeukgi.png', dpi = 200)
        print "Congratuation for 2014 Korean Independence day, Gwangbokjeol Taegeukgi.png is generated with 200 dpi resolution."


def dual_half_circle(center, radius, angle=180/np.pi*np.arctan(-2./3), colors=('red','blue'), **kwargs):
    """
        Add two half circles to the axes *ax* (or the current axes) with the
        specified facecolors *colors* rotated at *angle* (in degrees).
    """
    theta1, theta2 = angle, angle + 180
    w1 = Wedge(center, radius, theta1, theta2, fc=colors[0], ec=colors[0], **kwargs)
    w2 = Wedge(center, radius, theta2, theta1, fc=colors[1], ec=colors[1], **kwargs)
    return [w1, w2]

def genbar(theta, xy, movement):
    """
        First, rotate the bar, then move.
    """
    R = np.array([[np.cos(np.pi/180.*theta), -np.sin(np.pi/180*theta)], [np.sin(np.pi/180.*theta), np.cos(np.pi/180.*theta)]])
    npts = xy.shape[0]
    out = np.zeros((4,2))
    for i in range(4):
        out[i,:] = R.dot(xy[i,:])

    out[:,0] = out[:,0] + movement[0]
    out[:,1] = out[:,1] + movement[1]

    return out


def symmove(xin, flag='x'):
    """
        Symmetric movement function
    """
    x = xin.copy()
    if flag =='x':
        x[:,0] = -x[:,0]
    elif flag =='y':
        x[:,1] = -x[:,1]
    elif flag =='xy':
        x = -x
    else:
        raise Exception("Not implemented !!")
    return x

if __name__ == '__main__':
    taegeukgi = Taegeukgi(100.)
    taegeukgi.run()
