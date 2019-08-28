sphinx简介
================

sphinx是什么？
----------------------

`参考sphinx中文版使用手册 <https://zh-sphinx-doc.readthedocs.io/en/latest/contents.html>`_ ，介绍sphinx。

Sphinx 是一种文档工具，它可以令人轻松的撰写出清晰且优美的文档, 由 Georg Brandl 在BSD 许可证下开发. 
新版的Python文档 就是由Sphinx生成的， 并且它已成为Python项目首选的文档工具,同时它对 C/C++ 项目也有很好的支持; 
并计划对其它开发语言添加特殊支持. 本站当然也是使用 Sphinx 生成的，它采用reStructuredText! Sphinx还在继续开发.
下面列出了其良好特性,这些特性在Python官方文档中均有体现:

- **丰富的输出格式**: 支持 HTML (包括 Windows 帮助文档), LaTeX (可以打印PDF版本), manual pages（man 文档）, 纯文本
- **完备的交叉引用**: 语义化的标签,并可以自动化链接函数,类,引文,术语及相似的片段信息
- **明晰的分层结构**: 可以轻松的定义文档树,并自动化链接同级/父级/下级文章
- **美观的自动索引**: 可自动生成美观的模块索引
- **精确的语法高亮**: 基于 Pygments 自动生成语法高亮
- **开放的扩展**: 支持代码块的自动测试,并包含Python模块的自述文档(API docs)等

Sphinx 使用 reStructuredText 作为标记语言, 可以享有 Docutils 为reStructuredText提供的分析，转换等多种工具.

Sphinx的官网英文版手册地址：`http://www.sphinx-doc.org/en/master/contents.html 
<http://www.sphinx-doc.org/en/master/contents.html>`_ 。

为什么用sphinx写文档？
-------------------------

用Word、PPT、Excel、Pages、Numbers也很棒，但是sphinx用纯文本编辑

    - 方便用Git/Svn等版本管理工具实现协作
    - 通过Web发布，有利于文档的传播，无需安装软件即可查看
    - 有更方便的索引和引用，支持检索查询
    - 支持用脚本画图，排版，高效率低成本提升文档美观度
    - 高度的可扩展性，包括自定义样式、提供自动函数来解决一些常见问题等等


为什么不推荐Markdown作为大型文档协作工具？
-----------------------------------------------

Sphinx缺省使用reStructuredText语法，尽管它也支持Markdown，但为什么不推荐用Markdown，以下是引用别的blog提供的观点。
`http://ericholscher.com/blog/2016/mar/15/dont-use-markdown-for-technical-docs/ 
<http://ericholscher.com/blog/2016/mar/15/dont-use-markdown-for-technical-docs/>`_ 

Markdown是互联网上最普遍使用的轻量级标记语言。对于写博客和评论这类的任务，用Markdown很棒。
不过最近技术社区的人员开始用它来写文档。

下面我列出一些反对使用Markdown的观点，希望能帮助你决定是否适合使用Markdown。
如果你在考虑使用Markdown，我希望你也可以关注下Asciidoctor 和Sphinx，我发现用它们写文档更好。
人们选择Markdown是因为它可以很简单的处理一些基本任务。开发者选择它是因为GitHub支持它，尽管GitHub支持9种不同的标记语言，
包括 Asciidoc和reStructuredText。但是当文档从几页逐渐增长到大的文档集，Markdown很快就崩溃并成为累赘。下面是这种情况发生的原因。

.. rubric:: 缺乏一个标准

最初，Markdown是由John Gruber写的initial implementation来定义，但并未明确规定行为规范。

随着Markdown越来越流行，越来越多的站点开始支持Markdown的实现，这些站点是用其它语言写成的，因此产生了更多的Markdown实现。
所有这些实现有轻微差别，但都达不到令人接受的程度。

比如有些实现要求开头有一个空格，但另外的一些不做要求：

::

    # Heading 1
    #Heading 1

还有一些小问题使得Markdown很难在不同的站点和版本之间移植

在过去的几年里，Commonmark已经发展成标准化的Markdown。这很好，应该解决很多问题，但是却没人采用它。

.. rubric:: 风格

Markdown缺乏采用的主要原因是这些年来其一直在变化。
起初，Markdown功能很有限，每当有流行的工具在Markdown上实现的时候，都会有一个特定的风格。
听起来不错 ，是吧？问题是每一个工具都形成了不同的风格，甚至连实现相似任务的工具都有不同的语法。

举个例子，在Markdown Extra 中代码块是下面这种样式：

.. code-block:: python

    ~~~ .python
    import antigravity
    ~~~

这将python类应用于输出的HTML块

然而，同样的情况在GitHub Flavored Markdown 中是这样的：

::

    ```python
    import antigravity
    ```

这会将语法高亮显示应用于实际呈现的HTML输出。

相似的概念，不同的语法，但都是Markdown。

.. rubric:: 缺乏扩展

其它的标记语言，可以对其进行扩展以提供需要的功能。它们在语法上有增添新功能同时又不会违反初始规范的机制。

比如reStructuredText，具有内嵌和块级别的标记：

.. code-block:: reStructuredText

    .. contents:: All the stuff I'm going to talk about
    :depth: 2

    Please look at :rfc:`1984` for more information.
    This is implemented in our codebase at :class:`Example.Encryption`.

可以了解更多关于 rfc， class和 contents的概念。

作为一个使用rST或Asciidoctor的开发者，我可以以一种简单，可插入的方式增添新的标记。
我不必改变语言的解析方式，而且我还可以通过标准扩展机制向其它用户分享那些新功能。

在不同的版本间进行移植这些功能，用Markdown可办不到。

.. note::

    注意：CommonMark正在开发可扩展性的语法，但还没有实现。

.. rubric:: 缺乏语义化

尽管很多人添加了很多扩展，但都不够语义化。这意味着不能写Class或Warning，只能写文本。因此很多人直接将HTML嵌入到Markdown中：

而在reStructuredText中，你可以写成：

.. code-block:: html

    <div class="warning">
    This is a Warning!
    </div>

这在HTML,PDF，甚至任何创建的输出格式中都可以合适的显示为一个Warning.

.. code-block:: reStructuredText

    .. warning:: This is a Warning!

语义化标记可以将所写的文字与它们的显示方式完全分开。

缺乏语义化将导致问题，原因如下：

- 现在Markdown依赖于显示中的特定CSS类，这意味着编写者必须考虑如何设计页面。
- 内容不可再移植到其他输出格式（PDF等）。
- 转换到其他标记工具和页面设计变得更加困难。

.. note::

    注意：在我的博文Semantic Meaning in Authoring Documentation中有关于语义化更详细的介绍。

.. rubric:: 锁定和缺乏可移植性

风格的多种多样及缺乏语义化导致锁定。一旦创建了大的Markdown文档集，就很难将它们迁移到另一个工具上，即使该工具宣称支持Markdown！
自定义的HTML类和奇怪风格的扩展组成的文档集，除了在当前的工具和设计外，在其它地方都行不通。

同时也无法轻易将Markdown迁移到其他标记语言（Asciidoc或RST），因为Pandoc和其他转换工具不支持您风格的扩展。
很多人选择Markdown是因为他们认为他们可以在稍后迁移到其他工具或其它标记语言。

Markdown绝对是最低的共同标准，除非文档集足够小，否则你所需要的东西都不在基本语法中。
任何有意义的文档都需要扩展，而一旦使用Markdown各种各样风格的扩展，你将失去所有可移植性的优势。



.. rubric:: 结论

我认为CommonMark是向前迈出的一大步，如果它被更广泛地使用，并且增加对扩展的支持，我会全心全意地推荐它作为解决这个问题的方法。
我不能拥护Markdown目前的生态系统，并且我认为它很大程度上阻止了人们使文档变得更好。

我希望我们可以开始推进更加标准化的语言集合，包括CommonMark，reStructuredText和Asciidoc，在我们使用的工具套件中全面支持他们。
目前，Sphinx和Asciidoctor是很好的替代品。它们语音内部内置了更多的扩展，并且含有用于构建当今文档更完整的工具。

Markdown更像是一个概念，而不是实现。 它通常意味着“在看起来与Markdown类似的语言上的一组互不兼容的扩展”。 当创建大的文档集时，它显然不是正确的工具。

为什么用脚本画图？
------------------------

.. rubric:: 效率

用脚本画图，一开始需要有熟悉的过程，可能比你用现有工具要慢，但一旦你掌握了这些工具，特别是uml等标准图，你的画图的速度会大大加快，
因为你只需要关注图的内容和逻辑，排版和美化等问题由工具自动解决了。当然为了布局合理，画图的逻辑结构也是会有影响的，这可以迫使你
对于图的内容逻辑更多的思考。

.. rubric:: 协作

如果用画图工具，并采用图片标记插入，可能比较符合你原来的创作习惯，但这种方式将导致协作和版本管理的困难，因为别人无法通过
修改文本文件来生成新的图片。

