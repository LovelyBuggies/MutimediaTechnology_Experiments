# Experiments Report

[TOC]



---

## Adaptive Huffman Coding

As **[Adaptive Huffman Coding](https://en.wikipedia.org/wiki/Adaptive_Huffman_coding)** is generally base on **[Huffman Coding](https://en.wikipedia.org/wiki/Huffman_coding)**,  we are going to first briefly introduce **[Huffman Coding](https://en.wikipedia.org/wiki/Huffman_coding)** in this part.



### Algorithm



#### Huffman Coding

> **[Huffman Coding](https://en.wikipedia.org/wiki/Huffman_coding)** is a lossless data compression algorithm. The idea is to assign variable-length codes to input character, lengths of the assigned codes are based on the frequecies of corresponding characters. The most frequent character gets the small code and the least frequent character gets the largest code.

**[Huffman Coding](https://en.wikipedia.org/wiki/Huffman_coding)** consists of following steps:

- First, we need to sort each characters by their emerge frequencies. 

- Then we are able build Huffman Tree 🌲. A great ***Huffman Tree Construction demo*** is on this website - [YouTube/Huffman Coding - Greedy Algorithm](YouTube/Huffman Coding - Greedy Algorithm) .

- After buliding a Huffman Tree, we can simply put characters together according to the compression Table. ⚠️ *Notice that the above **demo** generated a compression table like the following image ⬇️, and no ambiguity would happen.*
- Finally, we compress the information successfully! ✌️

![](https://ws2.sinaimg.cn/bmiddle/006tNbRwgy1fwx0borxohj30s811ewgq.jpg)



#### Adaptive Huffman Coding 

>  **[Adaptive Huffman Coding](https://en.wikipedia.org/wiki/Adaptive_Huffman_coding)** (also called **Dynamic Huffman coding**) is an [adaptive coding](https://en.wikipedia.org/wiki/Adaptive_coding) technique based on **[Huffman coding](https://en.wikipedia.org/wiki/Huffman_coding)**. In the **[Adaptive Huffman Coding](https://en.wikipedia.org/wiki/Adaptive_Huffman_coding)** , statistics are gathered and updated dynamically **both in encoder and decoder** , who use the same routine. It permits building the code as the symbols are being transmitted, having no initial knowledge of source distribution, that allows one-pass encoding and adaptation to changing conditions in data. 

**The rule of  [Adaptive Huffman Coding](https://en.wikipedia.org/wiki/Adaptive_Huffman_coding) algorithm are sophisticated:**

- Initial code assigns symbols with some initially agreed upon codes, without any prior knowledge of the frequency count.
- Then we start to build **Adaptive Huffman Tree**:
  - Nodes are numbered in order **from left to right, bottom to top**. The numbers in parentheses indicates the count.
  - The tree must always **maintain its sibling property**, i.e., all nodes (internal and leaf) are arranged in the order of increas- ing counts. 
  - If the sibling property is about to be violated, a **swap procedure** is invoked to update the tree by rearranging the nodes. 
  - When a swap is necessary, the **farthest node with count $N$** is swapped with the node whose count has just been increased to $N + 1$.
- A special symbol **NEW** will be sent before any letter if it is to be sent the first time, and encoder compresses the corresponding letter.

Following a fantastic video of **[Adaptive Huffman Coding](https://en.wikipedia.org/wiki/Adaptive_Huffman_coding)** **algorithm demo** on this website - [YouTube/Adaptive Huffman Encoding exercise demo](https://www.youtube.com/watch?v=N5pw_Z-oP-4) , I tried the *courseware example* with initial code: *NEW - 0; A - 00001; B - 00010; C - 00011; D - 00100* .

![](https://ws3.sinaimg.cn/large/006tNbRwgy1fwx6jok0r3j31ic12y77t.jpg)

![](https://ws2.sinaimg.cn/large/006tNbRwgy1fwx6k9nywsj31kw0yr0yp.jpg)

And finally generate *the sequence of symbols* like this:

![](https://ws1.sinaimg.cn/large/006tNbRwgy1fwx6m97nasj31kw042jt4.jpg)



### Exercise



#### Q. 1

What's the major `advantage` of **[Adaptive Huffman Coding](https://en.wikipedia.org/wiki/Adaptive_Huffman_coding)** compared with  **[Huffman coding](https://en.wikipedia.org/wiki/Huffman_coding)** ?

**The benefit of one-pass procedure is that the source can be encoded in real time, though it becomes more sensitive to transmission errors, since just a single loss ruins the whole code.**



#### Q. 2

Assume that **[Adaptive Huffman Coding](https://en.wikipedia.org/wiki/Adaptive_Huffman_coding)** is used to code an information source $S$with a vocabulary of four letters (a, b, c, d) . Before any transmission, the initial coding is *a - 00; b - 01; c - 10; d - 11* . As in the example illustrated in Figure, an **Adaptive Huffman Tree** is built after sending letters "*aabb*" . After that, the additional bitstream received by the decoder for the next few letters is *01010010101*. What's the additional letters received?

![](https://ws2.sinaimg.cn/large/006tNbRwgy1fwx85n8q5hj31as0qgabd.jpg)

**The received letters are *b - a - c - c*, respectively, the routine table is: **

| Code        | 01    | 01    | 00      | 10    | 101   |
| ----------- | ----- | ----- | ------- | ----- | ----- |
| **Symbols** | **b** | **a** | **NEW** | **c** | **c** |

**The Adaptive Huffman Trees after each of the additional letters are listed as following:** 

![](https://ws3.sinaimg.cn/large/006tNbRwgy1fwx99j8zlqj31kw18w10e.jpg)

![](https://ws1.sinaimg.cn/large/006tNbRwgy1fwx99gzo47j31kw1cpthh.jpg)

⚠️ *You can also watch tree changement on [my-Youtube-channel/Adaptive-Huffman-coding](https://www.youtube.com/watch?v=AQsHcZGMFIM).*



---



## Compression Methods

[**Image compression**](https://en.wikipedia.org/wiki/Image_compression) is a type of [data compression](https://en.wikipedia.org/wiki/Data_compression) applied to [digital images](https://en.wikipedia.org/wiki/Digital_image), to reduce their cost for [storage](https://en.wikipedia.org/wiki/Computer_data_storage) or [transmission](https://en.wikipedia.org/wiki/Data_transmission). [Algorithms](https://en.wikipedia.org/wiki/Algorithm) may take advantage of [visual perception](https://en.wikipedia.org/wiki/Visual_perception) and the [statistical](https://en.wikipedia.org/wiki/Statistical) properties of image data to provide superior results compared with generic compression methods.



### Image Formats

**Lossless image representation formats:**

- [**BMP**](https://en.wikipedia.org/wiki/Bmp) (bitmap) is a bitmapped graphics format used internally by the [Microsoft Windows graphics subsystem](https://en.wikipedia.org/wiki/GDI) ([GDI](https://en.wikipedia.org/wiki/GDI)), and used commonly as a simple graphics file format on that platform. It is an uncompressed format.
- [**PNG**](https://en.wikipedia.org/wiki/Png) (Portable Network Graphics) (1996) is a bitmap image format that employs lossless data compression. [**PNG**](https://en.wikipedia.org/wiki/Png) was created to both improve upon and replace the [**GIF**](https://en.wikipedia.org/wiki/Gif) format with an image file format that does not require a patent license to use. It uses the [DEFLATE compression algorithm](https://en.wikipedia.org/wiki/DEFLATE_compression_algorithm), that uses a combination of the **LZ77 algorithm** and Huffman coding.
- [**TIFF**](https://en.wikipedia.org/wiki/Tiff) (Tagged Image File Format) (last review 1992) is a file format for mainly storing images, including photographs and line art. It is one of the most popular and flexible of the current public domain raster file formats. Originally created by the company Aldus, jointly with Microsoft, for use with PostScript printing, **[TIFF](https://en.wikipedia.org/wiki/Tiff)** is a popular format for high color depth images, along with [**JPEG**](https://en.wikipedia.org/wiki/JPEG) and [**PNG**](https://en.wikipedia.org/wiki/Png). [**TIFF**](https://en.wikipedia.org/wiki/Tiff) format is widely supported by image-manipulation applications, and by scanning, faxing, word processing, optical character recognition, and other applications. 
- [**GIF**](https://en.wikipedia.org/wiki/Gif) images are compressed using the [Lempel–Ziv–Welch](https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Welch) (LZW) [lossless data compression](https://en.wikipedia.org/wiki/Lossless_data_compression) technique to reduce the file size without degrading the visual quality. [**GIF**](https://en.wikipedia.org/wiki/Gif) are suitable for sharp-edged line art (such as logos) with a limited number of colors. This takes advantage of the format's lossless compression, which favors flat areas of uniform color with well defined edges.

**Lossy image compression formats:**

- [**JPEG**](https://en.wikipedia.org/wiki/JPEG) (Joint Photographic Experts Group) (1992) is an algorithm designed to compress images with 24 bits depth or greyscale images. It is a lossy compression algorithm. One of the characteristics that make the algorithm very flexible is that the compression rate can be adjusted. If we compress a lot, more information will be lost, but the result image size will be smaller. With a smaller compression rate we obtain a better quality, but the size of the resulting image will be bigger. This compression consists in making the coefficients in the quantization matrix bigger when we want more compression, and smaller when we want less compression. 
- [**JPEG 2000**](https://en.wikipedia.org/wiki/JPEG_2000) (Joint Photographic Experts Group 2000) is a wavelet-based image compression standard. It was created by the Joint Photographic Experts Group committee with the intention of superseding their original discrete cosine transformbased [**JPEG**](https://en.wikipedia.org/wiki/JPEG) standard. 

**Comparason of different image formats:**

- [**JPEG**](https://en.wikipedia.org/wiki/JPEG) has a big compressing ration, reducing the quality of the image, it is ideal for big images and photographs.
- [**PNG**](https://en.wikipedia.org/wiki/Png) is a lossless compression algorithm, very good for images with big areas of one unique color, or with small variations of color.
- [**PNG**](https://en.wikipedia.org/wiki/Png) is a better choice than [**JPEG**](https://en.wikipedia.org/wiki/JPEG) for storing images that contain text, line art, or other images with sharp transitions that do not transform well into the frequency domain. 
- [**TIFF**](https://en.wikipedia.org/wiki/Tiff)  is a complicated format that incorporates an extremely wide range of options. While this makes it useful as a generic format for interchange between professional image editing applications, it makes supporting it in more general applications such as Web browsers difficult.
- The most common general-purpose lossless compression algorithm used with [**TIFF**](https://en.wikipedia.org/wiki/Tiff)  is [LZW](https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Welch), which is inferior to [**PNG**](https://en.wikipedia.org/wiki/Png) and until expiration in 2003 suffered from the same patent issues that [**GIF**](https://en.wikipedia.org/wiki/Gif) did. 



### Image Compression Tech

**Methods for lossless image compression are:**

- **[Run-length encoding](https://en.wikipedia.org/wiki/Run-length_encoding)** – used in default method in [PCX](https://en.wikipedia.org/wiki/PCX) and as one of possible in [BMP](https://en.wikipedia.org/wiki/BMP_file_format), [TGA](https://en.wikipedia.org/wiki/.tga), [TIFF](https://en.wikipedia.org/wiki/TIFF)
- Area image compression
- **[DPCM](https://en.wikipedia.org/wiki/DPCM)** and Predictive Coding
- **[Entropy encoding](https://en.wikipedia.org/wiki/Entropy_encoding)**
- Adaptive dictionary algorithms such as [LZW](https://en.wikipedia.org/wiki/LZW) – used in [GIF](https://en.wikipedia.org/wiki/Graphics_Interchange_Format) and [TIFF](https://en.wikipedia.org/wiki/TIFF)
- **[DEFLATE](https://en.wikipedia.org/wiki/DEFLATE)** – used in [PNG](https://en.wikipedia.org/wiki/Portable_Network_Graphics), [MNG](https://en.wikipedia.org/wiki/Multiple-image_Network_Graphics), and [TIFF](https://en.wikipedia.org/wiki/TIFF)
- **[Chain codes](https://en.wikipedia.org/wiki/Chain_code)**

**Methods for lossy compression:**

- Reducing the **[color space](https://en.wikipedia.org/wiki/Color_space_encoding)** to the most common colors in the image. The selected colors are specified in the colour [palette](https://en.wikipedia.org/wiki/Palette_(computing)) in the header of the compressed image. Each pixel just references the index of a color in the color palette, this method can be combined with [dithering](https://en.wikipedia.org/wiki/Dithering) to avoid [posterization](https://en.wikipedia.org/wiki/Posterization).
- **[Chroma subsampling](https://en.wikipedia.org/wiki/Chroma_subsampling).** This takes advantage of the fact that the human eye perceives spatial changes of brightness more sharply than those of color, by averaging or dropping some of the chrominance information in the image.
- **[Transform coding](https://en.wikipedia.org/wiki/Transform_coding).** This is the most commonly used method. In particular, a [Fourier-related transform](https://en.wikipedia.org/wiki/List_of_Fourier-related_transforms) such as the Discrete Cosine Transform (DCT) is widely used: [N. Ahmed](https://en.wikipedia.org/wiki/N._Ahmed), T. Natarajan and K.R.Rao, "[Discrete Cosine Transform](http://dasan.sejong.ac.kr/~dihan/dip/p5_DCT.pdf)," *IEEE Trans. Computers*, 90–93, Jan. 1974. The DCT is sometimes referred to as "DCT-II" in the context of a family of discrete cosine transforms; e.g., see [discrete cosine transform](https://en.wikipedia.org/wiki/Discrete_cosine_transform). The more recently developed [wavelet transform](https://en.wikipedia.org/wiki/Wavelet_transform) is also used extensively, followed by [quantization](https://en.wikipedia.org/wiki/Quantization_(image_processing)) and [entropy coding](https://en.wikipedia.org/wiki/Entropy_coding).
- **[Fractal compression](https://en.wikipedia.org/wiki/Fractal_compression).**



### JPEG VS GIF

