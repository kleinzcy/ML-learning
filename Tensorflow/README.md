# Tensorflow

学习过程中的一些总结。

## Basic operation

Tensorflow中的一些基础op。

* Graph

   Tensorflow是按照计算图定义op，每一个op都是计算图中的节点。可以自定义计算图，'graph=tf.Graph()'，再在这个graph中定义op，然后在Session中指定graph，运行定义的op即可。当然，Tensorflow中也有默认计算图，它无需用户定义。
   '''
   graph=tf.Graph()
   with grahp.as_default():
       # 定义op
       
   with tf.Session(graph=graph) as sess:
       # 执行op
   '''
   
* Tensor

   Tensor是Tensorflow的数据模型，它不保存实际的数据，它保存的是如何得到这些数据的过程，即Graph中op。
   'Tensor("add:0", shape(2,), dtype=float32)'
   上述Tensor中，说明了Tensor中包含三种属性，**name, shape, type**，name通过"node:src_output"的形式给出，node为结点的名称，src_output表示当前Tensor来自节点的第几个输出。shape就是数据的维度。dtype就是数据的类型，主要包含实数（tf.float32, tf.float64），整数（tf.int8, tf.int16, tf.int32, tf.int64, tf.unit8）、布尔型（tf.bool）和复数（tf.complex64, tf.complex128）。要注意是的是op中数据类型要一致，否则会报错，因此养成一个设置dtype的好习惯。
   
* Session

   上述定义了graph和tensor，只是定义了整个计算图的计算过程，并没有完成计算，这从Tensor的定义中也知道，它只保存了op，并没有完成计算，因此需要在Session中计算上述定义的op，Session创建有两种方法。'sess=tf.Session()'，这样定义的sess需要在计算完成后，用'sess.close()'以释放资源，防止资源泄漏（这里我不是很懂，什么是资源泄漏？），另一中如Graph处例子所示，这样做的好处是，自动释放内存，而且异常退出是也能关闭会话。op的操作可以通过'sess.run(op)'来执行，也可以设置默认sess，然后通过tf.Tensor.eval来计算op。
   '''
   sess=tf.Session()
   with sess.as_default():
       print(result.eval())
   '''
