# Tensorflow

学习过程中的一些总结。

## Basic operation

* Graph

   Tensorflow是按照计算图定义op，每一个op都是计算图中的节点。可以自定义计算图，`graph=tf.Graph()`，再在这个graph中定义op，然后在Session中指定graph，运行定义的op即可。当然，Tensorflow中也有默认计算图，它无需用户定义。
   ```
   graph=tf.Graph()
   with grahp.as_default():
       # 定义op
       
   with tf.Session(graph=graph) as sess:
       # 执行op
   ```
   
* Tensor

   Tensor是Tensorflow的数据模型，它不保存实际的数据，它保存的是如何得到这些数据的过程，即Graph中op。
   `Tensor("add:0", shape(2,), dtype=float32)`
   上述Tensor中，说明了Tensor中包含三种属性，**name, shape, type**，name通过"node:src_output"的形式给出，node为结点的名称，src_output表示当前Tensor来自节点的第几个输出。shape就是数据的维度。dtype就是数据的类型，主要包含实数（tf.float32, tf.float64），整数（tf.int8, tf.int16, tf.int32, tf.int64, tf.unit8）、布尔型（tf.bool）和复数（tf.complex64, tf.complex128）。要注意是的是op中数据类型要一致，否则会报错，因此养成一个设置dtype的好习惯。
   
* Session

   上述定义了graph和tensor，只是定义了整个计算图的计算过程，并没有完成计算，这从Tensor的定义中也知道，它只保存了op，并没有完成计算，因此需要在Session中计算上述定义的op，Session创建有两种方法。`sess=tf.Session()`，这样定义的sess需要在计算完成后，用`sess.close()`以释放资源，防止资源泄漏（这里我不是很懂，什么是资源泄漏？），另一种如Graph处例子所示，这样做的好处是，自动释放内存，而且异常退出是也能关闭会话。op的操作可以通过`sess.run(op)`来执行，也可以设置默认sess，然后通过tf.Tensor.eval来计算op。
   ```
   sess=tf.Session()
   with sess.as_default():
       print(result.eval())
   ```

* Variable

   Variable的作用就是更新和保存神经网络中的参数，它是一个特殊的张量，它里面有两种操作，assign和read，assign是赋值操作，下表给出一些[随机数生成函数](https://tensorflow.google.cn/api_docs/python/tf/random)。
   
   函数名称|随机数分布|主要参数
   -|-|-
   tf.random_normal|正太分布|平均值、标准差、取值类型
   tf.truncated_normal|正太分布，但如果随机数偏离平均值超过两个标准差，那么这个数会被重新随机|平均值、标准差、取值类型
   tf.random_uniform|均匀分布|最小、最大取值、取值类型
   tf.random_gamma|Gamma分布|形状分布alpha、尺度参数beta、取值类型
   
   tensorflow常数生成函数
   
   函数名称|功能
   -|-
   tf.zeros|产生全0的数组
   tf.ones|产生全1的数组
   tf.fill|产生一个全部为给定数字的数组
   tf.constant|产生一个给定值的常量
   
   需要注意的是，所有的Variable在被使用之前都要初始化：
   ```
   init_op=tf.global_variables_initializer()
   sess.run(init_op)
   ```
   
   此外，Tensorfolw中还可以通过集合管理不同的资源，这一块目前认识不足，后续补充。
   
* Placeholder
   占位符，为输入数据做准备。节省计算图中的资源。
