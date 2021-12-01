---
title: FaceNet 使用实例介绍
date: 2018/3/12
tags: 人脸识别, AI
---

FaceNet将人脸图像映射到欧几里得空间，空间的距离代表了人脸图像的相似性。基于该映射空间可以实现人脸识别，验证和聚类等任务。

## 1. 安装依赖程序

a) 安装 [Tensorflow](https://github.com/davidsandberg/facenet/wiki/Running-training#1-install-tensorflow) 
b) 下载克隆 [FaceNet repo](https://github.com/davidsandberg/facenet.git) 到本地
c) 安装 [需要的Python模块](https://github.com/davidsandberg/facenet/blob/master/requirements.txt) 

## 2. 下载已训练模型

facenet提供了两个预训练模型，分别是基于CASIA-WebFace和MS-Celeb-1M人脸库训练的，链接为：

| Model name                               | LFW accuracy | Training dataset | Architecture                             |
| ---------------------------------------- | ------------ | ---------------- | ---------------------------------------- |
| [20170511-185253](https://drive.google.com/file/d/0B5MzpY9kBtDVOTVnU3NIaUdySFE) | 0.987        | CASIA-WebFace    | [Inception ResNet v1](https://github.com/davidsandberg/facenet/blob/master/src/models/inception_resnet_v1.py) |
| [20170512-110547](https://drive.google.com/file/d/0B5MzpY9kBtDVZ2RpVDYwWmxoSUk) | 0.992        | MS-Celeb-1M      | [Inception ResNet v1](https://github.com/davidsandberg/facenet/blob/master/src/models/inception_resnet_v1.py) |

将下载的文件夹解压到src\models\目录下面，目录 `20170512-110547` 将包含以下内容：

```
20170512-110547.pb
model-20170512-110547.ckpt-250000.data-00000-of-00001
model-20170512-110547.ckpt-250000.index
model-20170512-110547.meta
```

## 3. 对齐图片

文件`src/align/align_dataset_mtcnn.py`给我们提供了一个对齐图片中面部的实例。主要过程是：

- 读取指定目录中的图片
- 进行面部检测
- 然后对齐裁剪面部
- 另存到指定目录


这段代码：

```python
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from scipy import misc
import sys
import os
import argparse
import tensorflow as tf
import numpy as np
import facenet
import align.detect_face
import random
from time import sleep


output_dir = 'ad/'
input_dir = 'presidents/'

gpu_memory_fraction=0.25 #每个会话允许使用最大25％的GPU总内存
margin = 32
image_size = 160
random_order = False
detect_multiple_faces = True

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Store some git revision info in a text file in the log directory
src_path,_ = os.path.split(os.path.realpath(__file__))
facenet.store_revision_info(src_path, output_dir, ' '.join(sys.argv))
dataset = facenet.get_dataset(input_dir)

print('Creating networks and loading parameters')

with tf.Graph().as_default():
    gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=gpu_memory_fraction)
    sess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options, log_device_placement=False))
    with sess.as_default():
        pnet, rnet, onet = align.detect_face.create_mtcnn(sess, None)

minsize = 80 # minimum size of face
threshold = [ 0.6, 0.8, 0.95 ]  # three steps's threshold
factor = 0.709 # scale factor

# Add a random key to the filename to allow alignment using multiple processes
random_key = np.random.randint(0, high=99999)
bounding_boxes_filename = os.path.join(output_dir, 'bounding_boxes_%05d.txt' % random_key)

with open(bounding_boxes_filename, "w") as text_file:
    nrof_images_total = 0
    nrof_successfully_aligned = 0
    if random_order:
        random.shuffle(dataset)
    for cls in dataset:
        output_class_dir = os.path.join(output_dir, cls.name)
        if not os.path.exists(output_class_dir):
            os.makedirs(output_class_dir)
            if random_order:
                random.shuffle(cls.image_paths)
        for image_path in cls.image_paths:
            nrof_images_total += 1
            filename = os.path.splitext(os.path.split(image_path)[1])[0]
            output_filename = os.path.join(output_class_dir, filename+'.png')
            print(image_path)
            if not os.path.exists(output_filename):
                try:
                    img = misc.imread(image_path)
                except (IOError, ValueError, IndexError) as e:
                    errorMessage = '{}: {}'.format(image_path, e)
                    print(errorMessage)
                else:
                    if img.ndim<2:
                        print('Unable to align "%s"' % image_path)
                        text_file.write('%s\n' % (output_filename))
                        continue
                    if img.ndim == 2:
                        img = facenet.to_rgb(img)
                    img = img[:,:,0:3]

                    bounding_boxes, _ = align.detect_face.detect_face(img, minsize, pnet, rnet, onet, threshold, factor)
                    nrof_faces = bounding_boxes.shape[0]
                    if nrof_faces>0:
                        det = bounding_boxes[:,0:4]
                        det_arr = []
                        img_size = np.asarray(img.shape)[0:2]
                        if nrof_faces>1:
                            if detect_multiple_faces:
                                for i in range(nrof_faces):
                                    det_arr.append(np.squeeze(det[i]))
                            else:
                                bounding_box_size = (det[:,2]-det[:,0])*(det[:,3]-det[:,1])
                                img_center = img_size / 2
                                offsets = np.vstack([ (det[:,0]+det[:,2])/2-img_center[1], (det[:,1]+det[:,3])/2-img_center[0] ])
                                offset_dist_squared = np.sum(np.power(offsets,2.0),0)
                                index = np.argmax(bounding_box_size-offset_dist_squared*2.0) # some extra weight on the centering
                                det_arr.append(det[index,:])
                        else:
                            det_arr.append(np.squeeze(det))

                        for i, det in enumerate(det_arr):
                            det = np.squeeze(det)
                            bb = np.zeros(4, dtype=np.int32)
                            bb[0] = np.maximum(det[0]-margin/2, 0)
                            bb[1] = np.maximum(det[1]-margin/2, 0)
                            bb[2] = np.minimum(det[2]+margin/2, img_size[1])
                            bb[3] = np.minimum(det[3]+margin/2, img_size[0])
                            cropped = img[bb[1]:bb[3],bb[0]:bb[2],:]
                            scaled = misc.imresize(cropped, (image_size, image_size), interp='bilinear')
                            nrof_successfully_aligned += 1
                            filename_base, file_extension = os.path.splitext(output_filename)
                            if detect_multiple_faces:
                                output_filename_n = "{}_{}{}".format(filename_base, i, file_extension)
                            else:
                                output_filename_n = "{}{}".format(filename_base, file_extension)
                            misc.imsave(output_filename_n, scaled)
                            text_file.write('%s %d %d %d %d\n' % (output_filename_n, bb[0], bb[1], bb[2], bb[3]))
                    else:
                        print('Unable to align "%s"' % image_path)
                        text_file.write('%s\n' % (output_filename))
                        
print('Total number of images: %d' % nrof_images_total)
print('Number of successfully aligned images: %d' % nrof_successfully_aligned)
```



## 4. 人脸比对例子

facenet可以直接比对两个人脸经过它的网络映射之后的欧氏距离，运行程序为facenet-master\src\compare.py。 

CMD下运行：

```
python compare.py models\20170511-185253 1.jpg 2.jpg
```

