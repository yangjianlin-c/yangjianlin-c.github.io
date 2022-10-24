## **安装 TensorFlow Lite 解释器**

python配置为国内源


使用 Python 运行 TensorFlow Lite 模型，只需安装 TensorFlow Lite 解释器，不需要安装所有 TensorFlow 软件包。

下载对应的wheel文件，运行 `pip3 install` 安装。

| Python | 网址                                                                                                                                                                                |
| ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 3.5    | [https://dl.google.com/coral/python/tflite_runtime-2.1.0.post1-cp35-cp35m-linux_armv7l.whl](https://dl.google.com/coral/python/tflite_runtime-2.1.0.post1-cp35-cp35m-linux_armv7l.whl) |
| 3.6    | [https://dl.google.com/coral/python/tflite_runtime-2.1.0.post1-cp36-cp36m-linux_armv7l.whl](https://dl.google.com/coral/python/tflite_runtime-2.1.0.post1-cp36-cp36m-linux_armv7l.whl) |
| 3.7    | [https://dl.google.com/coral/python/tflite_runtime-2.1.0.post1-cp37-cp37m-linux_armv7l.whl](https://dl.google.com/coral/python/tflite_runtime-2.1.0.post1-cp37-cp37m-linux_armv7l.whl) |
| 3.8    | [https://dl.google.com/coral/python/tflite_runtime-2.1.0.post1-cp38-cp38-linux_armv7l.whl](https://dl.google.com/coral/python/tflite_runtime-2.1.0.post1-cp38-cp38-linux_armv7l.whl)   |

不要从 `tensorflow` 模块导入 `Interpreter` 模块，您需要从 `tflite_runtime` 导入。

例如，安装上述软件包后，如果复制并运行 [`label_image.py`](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/examples/python/) 文件，（可能）会失败，因为您没有安装 `tensorflow` 库。要解决此问题，请编辑该文件中的下面一行：

```
import tensorflow as tf
```

将其改成：

```
import tflite_runtime.interpreter as tflite
```

然后更改下面一行：

```
interpreter = tf.lite.Interpreter(model_path=args.model_file)
```

将其改成：

```
interpreter = tflite.Interpreter(model_path=args.model_file)
```

现在，重新运行 `label_image.py`。就是这样！您现在执行的正是 TensorFlow Lite 模型。
