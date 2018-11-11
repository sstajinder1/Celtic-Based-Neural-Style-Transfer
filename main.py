import numpy as np
import matplotlib.pyplot as plt
from CelticDruid import CelticDruid
from wordcloud import WordCloud
from dateutil.parser import parse
import face_recognition
import cv2



def imchange(image_pos):
    frame = cv2.imread(image_pos)
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(small_frame, model="cnn")
    # Display the results
    for top, right, bottom, left in face_locations:
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Extract the region of the image that contains the face
        face_image = frame[top-50:bottom+30, left-10:right+10]
        edges = cv2.Canny(face_image, 100, 100)

        cv2.imwrite('0.png',edges)




def emboss1():

    # Embossing
    from PIL import Image
    import numpy
    global widt,heig

    image_read = input('please input the location of the file with youre face: ')
    # defining azimuth, elevation, and depth
    ele = numpy.pi / 2.2  # radians
    azi = numpy.pi / 4.  # radians
    dep = 10.  # (0-100)

    # get a B&W version of the image
    img = Image.open(image_read).convert('L')
    # img1 = Image.open(image_read)
    widt,heig = img.size
    # get an array
    a = numpy.asarray(img).astype('float')
    # find the gradient
    grad = numpy.gradient(a)
    # (it is two arrays: grad_x and grad_y)
    grad_x, grad_y = grad
    # getting the unit incident ray
    gd = numpy.cos(ele)  # length of projection of ray on ground plane
    dx = gd * numpy.cos(azi)
    dy = gd * numpy.sin(azi)
    dz = numpy.sin(ele)
    # adjusting the gradient by the "depth" factor
    # (I think this is how GIMP defines it)
    grad_x = grad_x * dep / 100.
    grad_y = grad_y * dep / 100.
    # finding the unit normal vectors for the image
    leng = numpy.sqrt(grad_x ** 2 + grad_y ** 2 + 1.)
    uni_x = grad_x / leng
    uni_y = grad_y / leng
    uni_z = 1. / leng
    # take the dot product
    a2 = 255 * (dx * uni_x + dy * uni_y + dz * uni_z)
    # avoid overflow
    a2 = a2.clip(0, 255)
    # you must convert back to uint8 /before/ converting to an image
    img2 = Image.fromarray(a2.astype('uint8'))
    img2.save('0.png')



def fname(strn, ki, form):
    ret = ""
    d1 = (parse(strn,dayfirst=True).date())
    ret = ret + str(d1.year) + str(d1.month) + str(d1.day)
    ret = ret + "_" + ki + "." + form
    return ret



def finalart():
    from skimage import data, color, io, img_as_float
    import numpy as np
    import matplotlib.pyplot as plt
    from PIL import Image
    # import cv2

    alpha = 0.8

    img = cv2.imread('1.png')
    gray1 = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB)
    cv2.imwrite('1.png',gray1)

    img1 = cv2.imread('0.png')
    gray2 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('0.png', gray2)

    color_mask = Image.open('1.png')
    color_mask = color_mask.resize((widt, heig), Image.ANTIALIAS)

    img = img_as_float(Image.open('0.png'))

    img_color = np.dstack((img, img, img))

    img_hsv = color.rgb2hsv(img_color)
    color_mask_hsv = color.rgb2hsv(color_mask)

    img_hsv[..., 0] = color_mask_hsv[..., 0]
    img_hsv[..., 1] = color_mask_hsv[..., 1] * alpha

    img_masked = color.hsv2rgb(img_hsv)

    plt.imshow(img_masked)
    plt.savefig('fig.png')
    plt.show()



def finalarts():
    from PIL import Image
    import matplotlib.pyplot as plt
    import cv2
    # global widt, heig
    alpha = 0.9

    color_mask = Image.open('1.png', 'r')
    print(color_mask)
    img = cv2.imread('0.png')
    gray1 = cv2.cvtColor(img,cv2.COLOR_BGR2RGBA)
    # gray1[0,0] = [255,0,0]
    # gray1[20,20] = [0,255,0]
    cv2.imwrite('0.png',gray1)
    gray = Image.open('0.png', 'r')
    color_mask = color_mask.resize((widt, heig), Image.ANTIALIAS)
    print(gray)
    # fine2 = Image.alpha_composite(color_mask,gray)
    fine1 = Image.blend(color_mask,gray,alpha)
    plt.imshow(fine1)
    # plt.imshow(fine2)
    plt.show()


#
def jollycheck():
    import numpy as np
    from PIL import Image
    from os import path
    import matplotlib.pyplot as plt
    import os
    import random

    from wordcloud import WordCloud, STOPWORDS

    inp = str(input("\n Enter DOB in DD/MM/YYYY format :- "))
    ki, val = CelticDruid(inp)

    np.random.seed(np.random.randint(low=1, high=100, size=4)[1])
    np.random.shuffle(val)

    qual = ' '
    for v in val:
        qual = qual + v + ' '

    def grey_color_func(word, font_size, position, orientation, random_state=None,
                        **kwargs):
        return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)

    mask = np.array(Image.open('0.png'))

    wc = WordCloud(max_words=1000, mask=mask, margin=10,
                   random_state=1).generate(qual)
    # store default colored image
    default_colors = wc.to_array()
    plt.title("Custom colors")
    plt.imshow(wc.recolor(color_func=grey_color_func, random_state=3),
               interpolation="bilinear")
    wc.to_file("a_new_hope.png")
    plt.axis("off")
    plt.figure()
    plt.title("Default colors")
    plt.imshow(default_colors, interpolation="bilinear")
    plt.axis("off")
    plt.show()

if __name__ == '__main__':

    emboss1()
    #
    inp = str(input("\n Enter DOB in DD/MM/YYYY format :- "))
    ki, val = CelticDruid(inp)

    np.random.seed(np.random.randint(low=1, high=100, size=4)[1])
    np.random.shuffle(val)

    qual = ' '
    for v in val:
        qual = qual + v + ' '

    wordcloud = WordCloud(width=widt, height=heig,
                          background_color='black',
                          min_font_size=10).generate(qual)

    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.savefig('1.png', bbox_inches='tight')
    # plt.show()

    finalart()
