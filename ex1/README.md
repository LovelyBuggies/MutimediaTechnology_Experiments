# MultimediaTechnology_Experiments_1


## Video Transaction

### Question Description

In this experiment, we are supposed to complete a video transaction. Specifically, the second video appears to under the first video through an opening circle, like a camera iris opening. Implementation effect acts as figure below.

![](https://i.postimg.cc/SQHkxjXZ/small/Snip20181008_43.png)

*Seriously, this is not a PS problem...*

### Experiment Procedure

In order to achieve the "camera iris" effect, there are three possible methods:

- Circle crop an image and paste it to the second one.
- Try to draw a logo layer on the canvas.
- Change original pixels to mask pixels.

#### Language and Environment

We facilitate [Pycharm IDE](https://www.jetbrains.com/pycharm/) to conduct our experiment.Why pyCharm? The most inviting advantage of [Pycharm IDE](https://www.jetbrains.com/pycharm/) is that it is an integrated IDE for [Python](https://en.wikipedia.org/wiki/Python_(programming_language)). We are able to fluently code in [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) with the help of it.

More over, combined with [anaconda](https://www.anaconda.com/), we can get any package we want. *Actually, I first tried to used openCV API to solve this question, but it's turnout to be a dead end.* [Anaconda](https://www.anaconda.com/) -- Easily install 1,400+ data science packages for Python/R and manage your packages, dependencies, and environments—all with the single click of a button. Free and open source.

Here's my [anaconda](https://www.anaconda.com/) environment. As you can see, many package are listed in my env named "Video".

![](https://i.postimg.cc/gkRdXd8G/Snip20181008_42.png)

And the correspondences in [Pycharm IDE](https://www.jetbrains.com/pycharm/).

![](https://i.postimg.cc/XJD1xGMt/Snip20181009_46.png)

#### I/O Implementation

Considering that we could acquire each frame, the video imagine, and we are given the *videos* in *.jpg format, we prefer to deal with the imagines rather than the true videos for simplicity. It isn't huge work to apply this code to videos, if really neccessary. 

As for output, the pictures are saved using *.png formatted. Because we can open *.png image without difficulties in [Pycharm IDE](https://www.jetbrains.com/pycharm/).

Input images were interpreted as [numpy](http://www.numpy.org/) arrays. Each image is a [Height, Width, [R, G, B]] matrix or simply as [Height, Width, Grayscale].

``` python
img1 = Image.open("pics/lena.jpg").convert("L")
npImage1 = np.array(img1)
img2 = Image.open("pics/nobel.jpg").convert("L")
npImage2 = np.array(img2)
height2, width2 = img2.size
centerX = int(width2/2)
centerY = int(height2/2)
radius = int(height2/4);
```

#### Algorithm Design

In this experiment, we have tried many state-of-art ways, such as openCV. But unfortunately, as far as we are concerned, none of them show great performance in this context. 

By trials and errors, we finally selected [PIL(Python Imaging Library)](https://en.wikipedia.org/wiki/Python_Imaging_Library) as our tool and used naive methods to change pixels' RGB.

**Picture in Picture**

![](https://i.postimg.cc/q7w5hD1J/Snip20181009_44.png)

The figure above gives a brief description about the alogithm.

1. For layer image, find the rectangle interest region.
2. For each pixel in interest region, compute the distance to the center.
3. If the distance is smaller than radius, then the pixel change its pixel value to the corresponding mask image.

Core code is listed as following:

``` python
for y in range(centerY-radius, centerY+radius):
    for x in range(centerX-radius, centerX+radius):
        if np.power((x-centerX),2)+np.power((y-centerY),2) < np.power(radius,2):
            npImage2[y][x] = npImage1[y][x]
Image.fromarray(npImage2).save('pics/circleinsertion.png')
```

**Picture Extension**

We found the insertion's size was not the same as the original one when observed in detail. As a result, we need to conduct an imagine extension.

Considering the easiest method with some pixel loss, we used the following formula to illustrate the pixel change:

``` python
newSize/originalSize = newX/originalX
```

According to this formula, we finally got the extension of the mask image. Extension is 4/3 larger than the original.

``` python
img3 = Image.new("L", img1.size)
npImage3 = np.array(img3)
height3, width3 = img3.size
for y in range(0, height3-1):
    for x in range(0, width3-1):
            npImage3[y][x] = npImage1[int(3*y/4), int(3*x/4)]
Image.fromarray(npImage3).save('pics/larger.png')
```

**Extension Insertion**

This step is crystal clear when finishing steps above. It's not very laborious!

``` python
npImage2 = np.array(img2)
radius = int(3*radius/2)
for y in range(centerY-radius, centerY+radius):
    for x in range(centerX-radius, centerX+radius):
        if np.power((x-centerX),2)+np.power((y-centerY),2) < np.power(radius,2):
            npImage2[y][x] = npImage3[y][x]
Image.fromarray(npImage2).save('pics/circleExinsertion.png')
```

### Difficulties

#### OpenCV Defects

When referring to image process, [openCV](https://opencv.org/) is always recommended as the first choice. However, we think it's unable to fit into this context. 

Although cv is useful in image and video process, meanwhile, cv almost contains many sophisticated and advanced API, it's astonishing that, *to our best knowledge*, it doesn't include a simple circular image crop function!!! Cv can only crop images in a rectangle size or more complexed way (courier crop). Neither can it drop a circular image on a canvas.

Some classical Q&As in [Stack Overflow](https://stackoverflow.com/questions/31519197/python-opencv-how-to-crop-circle) actually explore this question. But we are not able to find any useful information as far, leaving this method abandon.

That's why we negate the first plan:

**Because I could never successfully crop images in circle, so any efforts to paste were useless.**

#### PIL ImageDraw Defects

Actually, when I try to google using keyword "python", "circle", "crop", some methods turn out to be good.

Following code is a sample:

``` python
import numpy as np
from PIL import Image, ImageDraw

// Open the input image as numpy array, convert to RGB
img1 = Image.open("pics/lena.jpg").convert("RGB")
npImage1 = np.array(img1)
height1, width1 = img1.size
img2 = Image.open("pics/nobel.jpg").convert("RGB")
npImage2 = np.array(img2)
height2, width2 = img2.size

// Create same size alpha layer with circle
alpha1 = Image.new('L', img1.size, 0)
draw1 = ImageDraw.Draw(alpha1)
draw1.pieslice([height1/4, width1/4, 3*height1/4, 3*width1/4], 0, 360, fill = 255)
alpha2 = Image.new('L', img2.size, 0)
draw2 = ImageDraw.Draw(alpha2)
draw2.pieslice([0, 0, height2, width2], 0, 360, fill = 255)

// Convert alpha Image to numpy array
npAlpha1 = np.array(alpha1)
npAlpha2 = np.array(alpha2)

// Add alpha layer to RGB
npImage1 = np.dstack((npImage1, npAlpha1))
npImage2 = np.dstack((npImage2, npAlpha2))

// Save with alpha
Image.fromarray(npImage1).save('pics/croppedLena.png')
Image.fromarray(npImage2).save('pics/croppedNobel.png')
``` 

The image was covered by circle, alluding the dawn of the success, seemingly. No bad, right?

![](https://i.postimg.cc/V6NHj9hj/Snip20181009_48.png)

But frustratingly, there exists some difficulties when trying to paste mask. In fact, the layer part **is not transparent** but some interesting RGB scales, so you can not simply paste it to the layer.

That's why we negate the second plan:

**Because I could not paste an ImageDraw to another image.**

### Implementation

View code on my [repo](https://github.com/LovelyBuggies/MultimediaTechnology_Experiments/tree/master/ex1/VideoTransition).

### Successful Results

* **Picture in picture:**

![](https://i.postimg.cc/ZYWJm6qB/Snip20181009_50.png)

* **Extended picture:**

![](https://i.postimg.cc/kG0130gc/Snip20181009_51.png)

* **Extension insertion:**

![](https://i.postimg.cc/FzdW6rNz/Snip20181009_49.png)

These pictures indicate the success of camera iris experiment!

## LUT Problem

### Question Description

For the [Color LUT(Lookup Table) problem](https://en.wikipedia.org/wiki/Lookup_table), try out the [median cut algorithm](https://www.cs.tau.ac.il/~dcor/Graphics/cg-slides/color_q.pdf) on a sample image.

### Background Knowledge

[Color quantization](https://en.wikipedia.org/wiki/Color_quantization) reduces the number of colors used in an image; this is important for displaying images on devices that support a limited number of colors and for efficiently compressing certain kinds of images. Most bitmap editors and many operating systems have built-in support for color quantization. Popular modern color quantization algorithms include the nearest color algorithm (for fixed palettes), the [median cut algorithm](https://en.wikipedia.org/wiki/Median_cut), and an algorithm based on [OcTrees](https://en.wikipedia.org/wiki/Octree).

**[A great video on Youtube](https://www.youtube.com/watch?v=LQST9MITKrw) helps me a lot when starting Mid-cut.**

### Experiment Procedure

There are two possible way to make images fuzzy:

- Use [OcTree](https://en.wikipedia.org/wiki/Octree) technique.
- Cut color scales into pieces.

#### Language and Environment

We also used [Pycharm IDE](https://www.jetbrains.com/pycharm/) as our tool and [Anaconda](https://www.anaconda.com/) *video-env* in the VideoTransion problem as our environment.

#### Algorithm Design 

This part contains screen-shot of [video on Youtube](https://www.youtube.com/watch?v=LQST9MITKrw).

We can convert an image to a numpy array. The the image can be represented by points in RGB 3-D space. So we can geographically spilt the points into many groups and put the points into buckets. 

![](https://i.postimg.cc/SsydHjXQ/colorquantization.gif)

Each bucket has a fixed RGB. The image will become less clear for pixels' RGBs are less more accurate. 


**Fuzzy Procedure**

It's intuitive to use ```np.floor()``` methods to approximate the float digits generated by pixel division.

The core code:

``` python
// Fuzzy Image
for x in range(0, int(width-1)):
  for y in range(0, int(height-1)):
    npImage1[y][x] = np.floor(npImage1[y][x] / np.power(2,n)) * np.power(2,n)
```

Moreover, we try to illustrate how the image becoming fuzzier:

``` python
// Fuzzier Image
for n in range(2, 8):
    // fuzzy process
    Image.fromarray(npImage1).show()
```

### Difficulties

#### Complex OcTree

Actually, I used [OcTree](https://en.wikipedia.org/wiki/Octree) at first. Gradually, after searching for some codes on [Github repo](https://github.com/jcummings2/pyoctree), I considered its a painstaking job. Why not just split pixels' RGB scales? 

**Fantastic as OcTree is, I think setting RGB intervals seems to be a better way.**

### Implementation

See my code [here](https://github.com/LovelyBuggies/MultimediaTechnology_Experiments/tree/master/ex1/LUT).

### Successful Result

* **Vague Apple:**

![](https://i.postimg.cc/0NNdCFhr/vagueapple.png)

* **Fuzzier Procedure:**

![](https://i.postimg.cc/44wfD00X/fuzzyprogress.gif)


