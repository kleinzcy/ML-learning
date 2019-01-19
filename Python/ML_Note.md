# 学习笔记 #
学习过程中一些笔记。

## 编码 ##

### sklearn ####

   * **onehotencode**:fit,transform

	from sklearn.preprocessing import transform	

	fit输入的shape（m,n)，其中m为样本个数，n为样本属性的个数。

	transform的输入为，与fit输入的n相同，m可以不同。并紧接一个.toarray()将稀疏编码转换成list。



* join方法：str.join(list)，以str连接list，转换成一个str。

* **shutil模块**:

* **glob模块**:glob模块提供了一个函数用于从目录通配符搜索中生成文件列表

```
import glob  

glob.glob('*.xml')

```