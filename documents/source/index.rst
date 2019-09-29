.. my-sphinx documentation master file, created by
   sphinx-quickstart on Sun Sep 29 13:41:41 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to my-sphinx's documentation!
=====================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

以下は `ブロック図生成ツール blockdiag <http://blockdiag.com/ja/>`_ の 1 つである nwdiag によるネットワーク図のサンプルです。図のビルドがうまくいくかの確認用に入れています。図のフォントは Noto Sans JP Regular を使用し、 SVG ファイルとして生成しています。

.. nwdiag::

    nwdiag {
      network dmz {
          address = "210.x.x.x/24"

          web01 [address = "210.x.x.1"];
          web02 [address = "210.x.x.2"];
      }
      network internal {
          address = "172.x.x.x/24";

          web01 [address = "172.x.x.1"];
          web02 [address = "172.x.x.2"];
          db01;
          db02;
      }
    }

`sphinx.ext.graphviz – Graphviz のSphinx拡張 <http://www.sphinx-doc.org/ja/stable/ext/graphviz.html>`_ を使った `Graphviz <http://graphviz.org/>`_ のグラフ埋め込みのサンプルです。

.. graphviz::

   digraph foo {
      "bar" -> "baz";
   }


`sphinxcontrib-plantuml <https://pypi.org/project/sphinxcontrib-plantuml/>`_ を使った `PlantUML <http://plantuml.com/>`_　の埋め込みサンプルです。

.. uml::

    skinparam monochrome true
    
    actor User
    participant "First Class" as A
    participant "Second Class" as B
    participant "Last Class" as C
    
    User -> A: DoWork
    activate A
    
    A -> B: Create Request
    activate B
    
    B -> C: DoWork
    activate C
    C --> B: WorkDone
    destroy C
    
    B --> A: Request Created
    deactivate B
    
    A --> User: Done
    deactivate A

コードブロックのサンプルです。使用している Sphinx のテーマが長い行を折り返すか折り返さないかを確認するために入れています。

.. code-block:: console

    echo hello
    echo longlonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglong
    echo goodbye

.. code-block:: console

    echo hello
    echo veryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryverylong
    echo goodbye

:code:`:linenos:` ありの :code:`code-block` のサンプルです。

.. code-block:: console
    :linenos:

    echo hello
    echo longlonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglonglong
    echo goodbye

.. code-block:: console
    :linenos:

    echo hello
    echo veryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryverylong
    echo goodbye



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
