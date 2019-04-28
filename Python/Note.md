# 学习笔记 #
学习过程中一些笔记。

## 编码 ##

### sklearn ####

   * **onehotencode**:fit,transform

	from sklearn.preprocessing import transform	

	fit输入的shape（m,n)，其中m为样本个数，n为样本属性的个数。

	transform的输入为，与fit输入的n相同，m可以不同。并紧接一个.toarray()将稀疏编码转换成list。


## 内置模块 ##

* **join方法**：str.join(list)，以str连接list，转换成一个str。

* **[shutil模块](https://www.cnblogs.com/zhangboblogs/p/7821702.html)**:

    * copy(来源地址，目标地址)

* **glob模块**:glob模块提供了一个函数用于从目录通配符搜索中生成文件列表

```
 import glob  

 glob.glob('*.xml')
```

* **json**:
   
   * loads:加载list成json。
   
   * load:加载文件。
   
   * dumps:将list转换成json格式储存
   
   * dump：接受两个参数，一个是文件名，一个是对象。
   
   
## 列表复制 ##

* 列表中的元素不是列表

```
b = a[:]
c = a.copy()
```

    上述两种做法会产生一个新列表，在b,c上的修改，对a不影响.
    
    `d = a`这样做对d的修改会直接反映到a上，b只是a的一个别名。
    
* 列表中的元素是列表

这种情况下，上述三种方式都是浅复制，即对新列表的修改会修改列表a，这个时候，有两种方法。
	* 创建一个一模一样的列表，其中的元素给全零，然后遍历列表a，一一赋值。
	* import copy，使用b = copy.deepcoy(a)，深度复制。
    
