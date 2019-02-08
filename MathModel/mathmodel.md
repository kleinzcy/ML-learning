## 数学建模 ##

### Problem B ###

	Task：预测语言分布情况，与语言接下来的发展趋势。

* 73410：文章中建立一个转移矩阵，表示语言与语言之间的转移关系，也就是马尔科夫模型，之后运用模拟退火算法优化。这个模型，值得借鉴的是，它由简到繁，先建立两个语言之间的模型，再建立多个语言的。

* 79002：文章与其他思路不同，它建立时序差分模型，也就是ARIMA模型，因为语言的发展趋势是有时序关系，差分后序列是稳定的，才可以用ARMA模型进行预测分析。此外，文中还建立了动态估计模型。

* 74316：自回归模型，马尔科夫链。一是利用时间序列自身的关系，二是利用马尔科夫链建立转移矩阵。这个题，很多都用到了马尔科夫模型，关系是怎样建立转移矩阵，这与文章的假设直接挂钩，文章的假设要有依据。

### Problem C ###

	Task:题目给了四个州能源使用的情况，要求我们根据这些数据，描述这四个周能量使用特点，以及描述他们之间的相同点与不同点，并给可能的原因，预测25年与50年的能量使用情况。

* 73767： 文章的思路值得借鉴，模型不是很复杂，主要是数据的处理与阐述。主要用到了PCA、BP neural network。但是它的sensitivity analysis很随便。这一点我不是很懂。

* 80560：这篇文章主要从经济学的角度解析的，涉及凯恩斯模型和希克斯-汉森模型等等经济模型，就不具体看。

* 72969： 文章方法比较简单，内容比较多。这里面涉及了很多统计学的概念，例如皮尔森系数等等，这方面我们需要后续补充。

### Problem D ###

	Task:充电桩的规划问题。伴随着电动汽车的普及，怎样规划充电桩的建设。

* 82504：文章中设计的方法比较基础。K-means，logsitc，Markov model等等。主要的模型是Markov model，利用该模型建立充电桩与道路网络之间的关系。

* 73156:针对不同问题，提出了不同的模型。而且针对不同地区，分层建模。

### summry ###

数学建模强调模型的可解释性，故而要采用一些基本的方法与理论。马尔科夫模型运用较多，后续我们要着重这个了解模型。文章[布局](http://www.mcmbooks.net/pingshen.html)方面，需要注意的是，问题假设，问题简化（主要是减少考虑的因素），稳定性分析（这一点，不知道怎么做，后续注意）。

**我觉得，我们适合做C题，B题数据是个麻烦，这决定着后续分析。C题偏向于经济，问题不是很难，懂一点经济，画点图，就可以试一试。D题的话，设计动态规划，这一块，我了解比较少，而且考虑因素比较多，不过也可以做。**

### 算法 ###

蚁群算法、模拟退火算法、遗传算法、马尔科夫模型、PCA、ARMA、K-means，logsitc