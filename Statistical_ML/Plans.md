# 寒假计划 #

寒假的一些安排，记录每天做的事和学到的东西

***

### 2019.1.8 ###

   * 搭建分类网络mobilenet
   * 数模学习两章
   * 数据比赛分析预测结果，找到突破口


### 2019.1.9 ###

   * 换数据集测试网络
   * 数学建模

### 2019.1.11 ###

   * 数学建模

***
   
### summary ###

* **github**

    pycharm commit to github and then merge,push

* **Docker**

    *run*:创建容器并启动

	*start*:启动容器

	*create*：创建容器

	*exec*:打开容器，启动一个伪终端，具体命令 `docker exec -it 容器名 `

***

### keras学习记录 ###

首先是<font color='red'>模型</font>：

sequential：顺序结构的模型。

[model](https://keras.io/models/model/)：非顺序结构，结构任意。能搭建resnet等模型。

model中的方法以及参数含义：

**方法**

* **compile**: *Configures the model for training.*

	compile(optimizer, loss=None, metrics=None, loss_ weights=None,sample_ weight_ mode=None, weighted_ metrics=None, target_ tensors=None)

	optimizer为优化器。loss为损失函数，**metrics**搞不清楚，后面参数的实际意义都不清楚。目前只需要前几个参数弄明白就行。

* **fit**: *Trains the model for a given number of epochs (iterations on a dataset).*

	fit(x=None, y=None, batch_ size=None, epochs=1, verbose=1, callbacks=None, validation_ split=0.0, validation_data=None, shuffle=True, class_ weight=None, sample_ weight=None, initial_ epoch=0, steps_ per_ epoch=None, validation_ steps=None)

	前面几个参数比较简单，不做说明。

	verbose：0为silent，1为progress bar，2为one line per epoch

	callbacks:字面是回调，在训练过程调用的函数。例如学习率下降等等。[detail](https://keras.io/callbacks/)

	validation_ split:确认集划分，在shuffle前完成，因此要提前shuffle。或者直接使用validation_data.

	step_ per_ epoch:每个epoch运行多少step，如果给了batch_ size那么这个参数就缺省。如果没给batch_ size那么这个参数就得自己填。此外，指定这个参数后，shuffle就无效了。

	validation_ steps:运行多少step进行validation，只有在step_ per_ epoch给定后才有用。

* **evaluate**: *Returns the loss value & metrics values for the model in test mode.*

	evaluate(x=None, y=None, batch_ size=None, verbose=1, sample_weight=None, steps=None)

* **predict**: *Generates output predictions for the input samples.*

	predict(x, batch_size=None, verbose=0, steps=None)



其次是<font color='red'>优化</font>：

这里面就包括很多[优化算法](https://keras.io/zh/optimizers/)

当然这里面又有很多技巧，后续总结。

还有一个就是数据增强，后续总结。

优化完了，就compile，之后fit就可以，和scikit-learn中大多数一样。 


### Python ###

#### os ####

* os.mkdir():创建目录
* os.path.exists():路径是否存在，存在则返回True，不存在则返回False
* os.path.join():合并两个路径，后一个路径前面不要加 /.
* os.getcwd():获取当前路径。
* os.listdir():返回当前目录下的目录或者文件。


#### tqdm

 `from tqdm import tqdm`

之后tqdm(iterable)，就可以打印进度条。

### 数学建模 ###

* **算法**：蚁群算法、遗传算法、
* **模型**：
	* **AHP模型**:分层决策的过程。key word:1、建立层次结构模型。2、构造成对比较矩阵。3、计算权向量并做一致性检验。4、计算组合权向量并做组合一致性检验。


<font color='red' size=5>**idea:**</font><font size=5>we focus on problem B(discrete problem) and C(data insight). For me, I will collect some classical algorithm, and you also can recommend the algorithm to me. What's more, I will pay my attention to some library, like scipy,numpy,pandas,matplotlib,seaborn,scikit-learn. Don't worry, I have learned a lot about them before.</font> 

