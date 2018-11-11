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



#### Method Chosen

Given a computer cartoon picture and a photograph as follows:
![](https://ws2.sinaimg.cn/large/006tNbRwgy1fwy50ef1h9j30rs0jvacx.jpg)

![](https://ws1.sinaimg.cn/large/006tNbRwgy1fwy50jjc7sj30sg0iywj0.jpg)

[**GIF**](https://en.wikipedia.org/wiki/Gif)s are suitable for **sharp-edged line art** (such as logos) with a limited number of colors. Taking advantage of the format's lossless compression, which favors flat areas of uniform color with well defined edges, **it's intuitive to choose [GIF](https://en.wikipedia.org/wiki/Gif) as a better choice for cartoon picture and [JPEG](https://en.wikipedia.org/wiki/JPEG) for photograph.**



#### JPEG Implementation



In this part, I implement a simple JPEG compression algorithm including `Color Conversion`, `Chroma Subsampling`, `2-D DCT transform`, `DPCM` , `Run Length Encoding` and `Entropy Coding` refered [this column](https://blog.csdn.net/w394221268/article/category/6371090).



**Color Conversion**

"Color space", refers to the mathematical model of the expression of color, such as our common "RGB" model, is decomposed into red, green and blue color into three components, such a picture can be broken down into three grayscale, mathematical expression, the design of each of the 8 by 8, 8 by 8 can be expressed by the three matrix, the range of the average between the [0, 255]. 

Different color models have different application scenarios, such as RGB model suitable for spontaneous light design, such as display in the printing industry, the use of ink printing, the color of the pattern was produced by when the reflected light, often using CMYK model, in the JPEG compression algorithm, the need to transform the pattern become YCbCr model, the Luminance, Luminance Y said here, Cb and Cr, respectively, said green and red "color difference value".

RGB 2 YCC conversion is shown as following,

```cpp
template<class T> static void RGB_to_YCC(image &img, int y, const T *src)
{
   for (int x = 0; x < img.m_x; x++) {
       const int r = src[x].r, g = src[x].g, b = src[x].b;
       img.set_px((ycbcr) {
           0 + (0.299* r) + (0.587* g) + (0.114* b),
           128 - (0.168736*r) - (0.331264*g) + (0.5*b),
           128 + (0.5*r) - (0.418688*g) - (0.081312*b),
       }, x, y);
   }
}
```



**Chroma subsampling** 

Chroma subsampling is the practice of encoding images by implementing less resolution for chroma information than for luma information, taking advantage of the human visual system's lower acuity for color differences than for luminance.

In human vision there are three channels for color detection, and for many color systems, three "channels" is sufficient for representing most colors. But there are other ways to represent the color. In many video systems, the three channels are luminance and two chroma channels. In video. The chroma can influence the luma specifically at the pixels where the subsampling put no chroma. Interpolation may then put chroma values there which are incompatible with the luma value there, and further post-processing of that Y'CbCr into R'G'B' for that pixel is what ultimately produces false luminance upon display

The subsampling processes are shown as follows:

``` cpp
if (m_comp[0].m_h_samp == 2 && m_comp[0].m_v_samp == 1) {
    for(int c=1; c < m_num_components; c++) {
        for(int y=0; y < m_image.m_y_mcu; y++) {
            for(int x=0; x < m_image.m_x_mcu; x+=2) {
                m_image.set_px(blend_dual(x, y, c), x/2, y, c);
            }
        }
    }
}
if (m_comp[0].m_h_samp == 2 && m_comp[0].m_v_samp == 2) {
    for(int c=1; c < m_num_components; c++) {
        for(int y=0; y < m_image.m_y_mcu; y+=2) {
            for(int x=0; x < m_image.m_x_mcu; x+=2) {
                m_image.set_px(blend_quad(x, y, c), x/2, y/2, c);
            }
        }
    }
}
```



**2 - D DCT Transformation**

The discrete cosine transform (DCT) helps separate the image into parts (or spectral sub-bands) of differing importance (with respect to the image's visual quality). The DCT is similar to the discrete Fourier transform: it transforms a signal or image from the spatial domain to the frequency domain.

![](https://ws4.sinaimg.cn/large/006tNbRwly1fx3y0qtjyyj30ly06adgf.jpg)

![](https://ws1.sinaimg.cn/large/006tNbRwly1fx3y02axq8j31kw12kk07.jpg)

[Look here for more infomation of my reference.](https://users.cs.cf.ac.uk/Dave.Marshall/Multimedia/node231.html) 

```cpp
static void dct(dct_t *data)
{
    dct_t z1, z2, z3, z4, z5, tmp0, tmp1, tmp2, tmp3, tmp4, tmp5, tmp6, tmp7, tmp10, tmp11, tmp12, tmp13, *data_ptr;

    data_ptr = data;

    for (int c=0; c < 8; c++) {
        tmp0 = data_ptr[0] + data_ptr[7];
        tmp7 = data_ptr[0] - data_ptr[7];
        tmp1 = data_ptr[1] + data_ptr[6];
        tmp6 = data_ptr[1] - data_ptr[6];
        tmp2 = data_ptr[2] + data_ptr[5];
        tmp5 = data_ptr[2] - data_ptr[5];
        tmp3 = data_ptr[3] + data_ptr[4];
        tmp4 = data_ptr[3] - data_ptr[4];
        tmp10 = tmp0 + tmp3;
        tmp13 = tmp0 - tmp3;
        tmp11 = tmp1 + tmp2;
        tmp12 = tmp1 - tmp2;
        data_ptr[0] = tmp10 + tmp11;
        data_ptr[4] = tmp10 - tmp11;
        z1 = (tmp12 + tmp13) * 0.541196100;
        data_ptr[2] = z1 + tmp13 * 0.765366865;
        data_ptr[6] = z1 + tmp12 * - 1.847759065;
        z1 = tmp4 + tmp7;
        z2 = tmp5 + tmp6;
        z3 = tmp4 + tmp6;
        z4 = tmp5 + tmp7;
        z5 = (z3 + z4) * 1.175875602;
        tmp4 *= 0.298631336;
        tmp5 *= 2.053119869;
        tmp6 *= 3.072711026;
        tmp7 *= 1.501321110;
        z1 *= -0.899976223;
        z2 *= -2.562915447;
        z3 *= -1.961570560;
        z4 *= -0.390180644;
        z3 += z5;
        z4 += z5;
        data_ptr[7] = tmp4 + z1 + z3;
        data_ptr[5] = tmp5 + z2 + z4;
        data_ptr[3] = tmp6 + z2 + z3;
        data_ptr[1] = tmp7 + z1 + z4;
        data_ptr += 8;
    }

    data_ptr = data;

    for (int c=0; c < 8; c++) {
        tmp0 = data_ptr[8*0] + data_ptr[8*7];
        tmp7 = data_ptr[8*0] - data_ptr[8*7];
        tmp1 = data_ptr[8*1] + data_ptr[8*6];
        tmp6 = data_ptr[8*1] - data_ptr[8*6];
        tmp2 = data_ptr[8*2] + data_ptr[8*5];
        tmp5 = data_ptr[8*2] - data_ptr[8*5];
        tmp3 = data_ptr[8*3] + data_ptr[8*4];
        tmp4 = data_ptr[8*3] - data_ptr[8*4];
        tmp10 = tmp0 + tmp3;
        tmp13 = tmp0 - tmp3;
        tmp11 = tmp1 + tmp2;
        tmp12 = tmp1 - tmp2;
        data_ptr[8*0] = (tmp10 + tmp11) / 8.0;
        data_ptr[8*4] = (tmp10 - tmp11) / 8.0;
        z1 = (tmp12 + tmp13) * 0.541196100;
        data_ptr[8*2] = (z1 + tmp13 * 0.765366865) / 8.0;
        data_ptr[8*6] = (z1 + tmp12 * -1.847759065) / 8.0;
        z1 = tmp4 + tmp7;
        z2 = tmp5 + tmp6;
        z3 = tmp4 + tmp6;
        z4 = tmp5 + tmp7;
        z5 = (z3 + z4) * 1.175875602;
        tmp4 *= 0.298631336;
        tmp5 *= 2.053119869;
        tmp6 *= 3.072711026;
        tmp7 *= 1.501321110;
        z1 *= -0.899976223;
        z2 *= -2.562915447;
        z3 *= -1.961570560;
        z4 *= -0.390180644;
        z3 += z5;
        z4 += z5;
        data_ptr[8*7] = (tmp4 + z1 + z3) / 8.0;
        data_ptr[8*5] = (tmp5 + z2 + z4) / 8.0;
        data_ptr[8*3] = (tmp6 + z2 + z3) / 8.0;
        data_ptr[8*1] = (tmp7 + z1 + z4) / 8.0;
        data_ptr++;
    }
}
```



**DPCM**

Differential pulse-code modulation is a signal encoder that uses the baseline of PCM but adds some functionalities based on the prediction of the samples of the signal.

If the input is a continuous-time analog signal, it needs to be sampled first so that a discrete-time signal is the input to the DPCM encoder.

- Option 1: take the values of two consecutive samples; if they are analog samples, quantize them; calculate the difference between the first one and the next; the output is the difference, and it can be further entropy coded.
- Option 2: instead of taking a difference relative to a previous input sample, take the difference relative to the output of a local model of the decoder process; in this option, the difference can be quantized, which allows a good way to incorporate a controlled loss in the encoding.

Applying one of these two processes, short-term redundancy (positive correlation of nearby values) of the signal is eliminated; compression ratios on the order of 2 to 4 can be achieved if differences are subsequently entropy coded, because the entropy of the difference signal is much smaller than that of the original discrete signal treated as independent samples.

``` cpp
// Tables and macro used to fully decode the DPCM differences.
static const int s_extend_test[16] = { 0, 0x0001, 0x0002, 0x0004, 0x0008, 0x0010, 0x0020, 0x0040, 0x0080, 0x0100, 0x0200, 0x0400, 0x0800, 0x1000, 0x2000, 0x4000 };
static const int s_extend_offset[16] = { 0, ((-1)<<1) + 1, ((-1)<<2) + 1, ((-1)<<3) + 1, ((-1)<<4) + 1, ((-1)<<5) + 1, ((-1)<<6) + 1, ((-1)<<7) + 1, ((-1)<<8) + 1, ((-1)<<9) + 1, ((-1)<<10) + 1, ((-1)<<11) + 1, ((-1)<<12) + 1, ((-1)<<13) + 1, ((-1)<<14) + 1, ((-1)<<15) + 1 };
static const int s_extend_mask[] = { 0, (1<<0), (1<<1), (1<<2), (1<<3), (1<<4), (1<<5), (1<<6), (1<<7), (1<<8), (1<<9), (1<<10), (1<<11), (1<<12), (1<<13), (1<<14), (1<<15), (1<<16) };
// The logical AND's in this macro are to shut up static code analysis (aren't really necessary - couldn't find another way to do this)
#define JPGD_HUFF_EXTEND(x, s) (((x) < s_extend_test[s & 15]) ? ((x) + s_extend_offset[s & 15]) : (x))
```



**RLE**

Run-length encoding is a very simple form of lossless data compression in which runs of data are stored as a single data value and count, rather than as the original run. This is most useful on data that contains many such runs. Consider, for example, simple graphic images such as icons, line drawings, and animations. It is not useful with files that don't have many runs as it could greatly increase the file size.

In this experiment, we use *the variable* `pD->m_eob_run` to represent the runs of data.

``` cpp
void jpeg_decoder::decode_block_ac_first(jpeg_decoder *pD, int component_id, int block_x, int block_y)
{
    int k, s, r;

    if (pD->m_eob_run) {
        pD->m_eob_run--;
        return;
    }

    jpgd_block_t *p = pD->coeff_buf_getp(pD->m_ac_coeffs[component_id], block_x, block_y);

    for (k = pD->m_spectral_start; k <= pD->m_spectral_end; k++) {
        s = pD->huff_decode(pD->m_pHuff_tabs[pD->m_comp_ac_tab[component_id]]);

        r = s >> 4;
        s &= 15;

        if (s) {
            if ((k += r) > 63)
                pD->stop_decoding(JPGD_DECODE_ERROR);

            r = pD->get_bits_no_markers(s);
            s = JPGD_HUFF_EXTEND(r, s);

            p[g_ZAG[k]] = static_cast<jpgd_block_t>(s << pD->m_successive_low);
        } else {
            if (r == 15) {
                if ((k += 15) > 63)
                    pD->stop_decoding(JPGD_DECODE_ERROR);
            } else {
                pD->m_eob_run = 1 << r;

                if (r)
                    pD->m_eob_run += pD->get_bits_no_markers(r);

                pD->m_eob_run--;

                break;
            }
        }
    }
}

void jpeg_decoder::decode_block_ac_refine(jpeg_decoder *pD, int component_id, int block_x, int block_y)
{
    int s, k, r;
    int p1 = 1 << pD->m_successive_low;
    int m1 = (-1) << pD->m_successive_low;
    jpgd_block_t *p = pD->coeff_buf_getp(pD->m_ac_coeffs[component_id], block_x, block_y);

    JPGD_ASSERT(pD->m_spectral_end <= 63);

    k = pD->m_spectral_start;

    if (pD->m_eob_run == 0) {
        for ( ; k <= pD->m_spectral_end; k++) {
            s = pD->huff_decode(pD->m_pHuff_tabs[pD->m_comp_ac_tab[component_id]]);

            r = s >> 4;
            s &= 15;

            if (s) {
                if (s != 1)
                    pD->stop_decoding(JPGD_DECODE_ERROR);

                if (pD->get_bits_no_markers(1))
                    s = p1;
                else
                    s = m1;
            } else {
                if (r != 15) {
                    pD->m_eob_run = 1 << r;

                    if (r)
                       pD->m_eob_run += pD->get_bits_no_markers(r);

                    break;
                }
            }

            do {
                jpgd_block_t *this_coef = p + g_ZAG[k & 63];

                if (*this_coef != 0) {
                    if (pD->get_bits_no_markers(1)) {
                        if ((*this_coef & p1) == 0) {
                            if (*this_coef >= 0)
                                *this_coef = static_cast<jpgd_block_t>(*this_coef + p1);
                            else
                                *this_coef = static_cast<jpgd_block_t>(*this_coef + m1);
                        }
                    }
                } else {
                    if (--r < 0)
                        break;
                }

                k++;

            } while (k <= pD->m_spectral_end);

            if ((s) && (k < 64)) {
                p[g_ZAG[k]] = static_cast<jpgd_block_t>(s);
            }
        }
    }

    if (pD->m_eob_run > 0) {
        for ( ; k <= pD->m_spectral_end; k++) {
            jpgd_block_t *this_coef = p + g_ZAG[k & 63];

            if (*this_coef != 0) {
                if (pD->get_bits_no_markers(1)) {
                    if ((*this_coef & p1) == 0) {
                        if (*this_coef >= 0)
                            *this_coef = static_cast<jpgd_block_t>(*this_coef + p1);
                        else
                            *this_coef = static_cast<jpgd_block_t>(*this_coef + m1);
                    }
                }
            }
        }

        pD->m_eob_run--;
    }
}
```



**Entropy Coding**

Entropy encoding is a lossless data compression scheme that is independent of the specific characteristics of the medium. Entropy coding creates and assigns a unique prefix-free code to each unique symbol that occurs in the input. These entropy encoders then compress data by replacing each fixed-length input symbol with the corresponding variable-length prefix-free output codeword. The length of each codeword is approximately proportional to the negative logarithm of the probability. Therefore, the most common symbols use the shortest codes.

Here we use Huffman Coding as our entropy coding instance.

``` cpp
// Limits canonical Huffman code table's max code size to max_code_size.
static void huffman_enforce_max_code_size(int *pNum_codes, int code_list_len, int max_code_size)
{
    if (code_list_len <= 1) return;

    for (int i = max_code_size + 1; i <= MAX_HUFF_CODESIZE; i++) pNum_codes[max_code_size] += pNum_codes[i];

    uint32 total = 0;
    for (int i = max_code_size; i > 0; i--)
        total += (((uint32)pNum_codes[i]) << (max_code_size - i));

    while (total != (1UL << max_code_size)) {
        pNum_codes[max_code_size]--;
        for (int i = max_code_size - 1; i > 0; i--) {
            if (pNum_codes[i]) {
                pNum_codes[i]--;
                pNum_codes[i + 1] += 2;
                break;
            }
        }
        total--;
    }
}

// Generates an optimized offman table.
void huffman_table::optimize(int table_len)
{
    sym_freq syms0[MAX_HUFF_SYMBOLS], syms1[MAX_HUFF_SYMBOLS];
    syms0[0].m_key = 1; syms0[0].m_sym_index = 0;  // dummy symbol, assures that no valid code contains all 1's
    int num_used_syms = 1;
    for (int i = 0; i < table_len; i++)
        if (m_count[i]) {
            syms0[num_used_syms].m_key = m_count[i];
            syms0[num_used_syms++].m_sym_index = i + 1;
        }
    sym_freq *pSyms = radix_sort_syms(num_used_syms, syms0, syms1);
    calculate_minimum_redundancy(pSyms, num_used_syms);

    // Count the # of symbols of each code size.
    int num_codes[1 + MAX_HUFF_CODESIZE]; clear_obj(num_codes);
    for (int i = 0; i < num_used_syms; i++)
        num_codes[pSyms[i].m_key]++;

    const uint JPGE_CODE_SIZE_LIMIT = 16; // the maximum possible size of a JPEG Huffman code (valid range is [9,16] - 9 vs. 8 because of the dummy symbol)
    huffman_enforce_max_code_size(num_codes, num_used_syms, JPGE_CODE_SIZE_LIMIT);

    // Compute m_huff_bits array, which contains the # of symbols per code size.
    clear_obj(m_bits);
    for (int i = 1; i <= (int)JPGE_CODE_SIZE_LIMIT; i++)
        m_bits[i] = static_cast<uint8>(num_codes[i]);

    // Remove the dummy symbol added above, which must be in largest bucket.
    for (int i = JPGE_CODE_SIZE_LIMIT; i >= 1; i--) {
        if (m_bits[i]) {
            m_bits[i]--;
            break;
        }
    }

    // Compute the m_huff_val array, which contains the symbol indices sorted by code size (smallest to largest).
    for (int i = num_used_syms - 1; i >= 1; i--)
        m_val[num_used_syms - 1 - i] = static_cast<uint8>(pSyms[i].m_sym_index - 1);
}
```



Finally, we are able to compress the animal images.



**STEP 1** : Compress JPEG imagines on terminal.

![](https://ws4.sinaimg.cn/large/006tNbRwgy1fx3z2jpk12j31bg0oywm2.jpg)

*Executable file and Outputs are given are archived in res folder.*



**STEP 2** : Using [I❤️IMG](https://www.iloveimg.com/) and [yasuotu](https://www.yasuotu.com/) to compress GIF Images respectively.

![](https://ws2.sinaimg.cn/large/006tNbRwly1fx3ziflumhj31b20nk762.jpg)

![](https://ws1.sinaimg.cn/large/006tNbRwly1fx3zj0wh4uj31is0kmwie.jpg)



**STEP 3** : Compare results.

Size (KB):

- Original: 116 + 177 = 293
- JPEG: 99 + 176 = 275
- GIF:
  - [I❤️IMG](https://www.iloveimg.com/): 111 + 166 = 277
  - [yasuotu](https://www.yasuotu.com/): 115 + 177 = 292

Pic:

Original JPG:

![](https://ws3.sinaimg.cn/large/006tNbRwly1fx3zxbjk4cj31kw0jf4hk.jpg)

Our JPEG:

![](https://ws3.sinaimg.cn/large/006tNbRwgy1fx3ztyeeoyj31kw0jih7l.jpg)

[I❤️IMG](https://www.iloveimg.com/) :

![](https://ws2.sinaimg.cn/large/006tNbRwly1fx3zya1y01j31kw0jbh41.jpg)

[yasuotu](https://www.yasuotu.com/) : 

![](https://ws2.sinaimg.cn/large/006tNbRwgy1fx3zz76s0tj31kw0jfh3z.jpg)



All of this demonstrates the effectiveness of our Ex.