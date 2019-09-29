#############################
記述サンプル
#############################

.. toctree::
   :maxdepth: 1
   :hidden:

   practical
   practical_view

.. comment

* ここでは\|Z\|という記述を|Z|に置き換えている

* | 改行を含む文章は行頭に `| ` をつける
  | こんなふうに

整形文章タイトル::

  文章1
  文章2

**syntax color: pythonの場合**

.. sourcecode:: python

   import DogIsCute

.. csv-table:: 外部csvデータを素材とした表組み
   :file: ../resources/csv/test.csv
   :header: a, b, c, d


.. list-table:: リスト表記を素材とした表組み
   :header-rows: 1
   :widths: 15, 10, 30

   * - Treat
     - Quantity
     - Description
   * - Albatross
     - 2.99
     - On a stick!
   * - Crunchy Frog
     - 1.49
     - If we took the bones out, it wouldn't be
       crunchy, now would it?
   * - Gannet Ripple
     - 1.99
     - On a stick!

.. list-table:: ヘッダを縦に配置した表組み
   :stub-columns: 1
   :widths: 15, 40

   * - title
     - Dragon Ball
   * - Author
     - Akira Toriyama
   * - Genre
     - Action

.. list-table:: ヘッダがクロスした表組み
   :header-rows: 1
   :stub-columns: 1
   :widths: 15, 10, 10, 10
   :class: center

   * -
     - case A
     - case B
     - case C
   * - target X
     - o
     - x
     - o
   * - target Y
     - o
     - x
     - x
   * - target Z
     - x
     - x
     - x
