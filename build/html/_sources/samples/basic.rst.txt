.. include:: /docs/_replace.txt
==================
基本表現
==================
公式ページ解説: https://planset-study-sphinx.readthedocs.io/ja/latest/04.html

index(目次リンク)
==================================
::

  .. toctree::
     :maxdepth: 1
     :caption: 文書管理
     :numbered:

     basic

各見出しに添える点線は、文字部分よりも長くなければなりません

見出し1
==================================
::

  ================================
  基本表現
  ================================

見出し2(章タイトルに相当)
==================================
::

  見出し2
  ================================

見出し3(章内セクションに相当)
==================================
::

  見出し3
  --------------------------------

箇条書き
==================================
- 箇条書き
- 箇条書き
* *でも-でも可能

::

  - 箇条書き
  - 箇条書き
  * *でも-でも可能

箇条書き(ナンバリング)
==================================

#. 箇条書き
#. 箇条書き

::

  #. 箇条書き
  #. 箇条書き


表組み
==================================
csv読込
----------------------------------
.. csv-table:: |usrs.table|
   :file: /docs/source/_static/csv/database/users.csv
   :header-rows: 1
   :widths: 10, 30, 20, 10, 10, 10, 20, 30

↑の表は↓のコードによって書かれています
::

  .. csv-table:: |usrs.table|
     :file: /docs/source/_static/csv/database/users.csv
     :header-rows: 1
     :widths: 10, 30, 20, 10, 10, 10, 20, 30


markdown風
----------------------------------
======= ====== ======
col1    col2   col3
======= ====== ======
row1    a      b
row2    a      b
row3    a      b
======= ====== ======

↑の表は↓のコードによって書かれています
::

  ======= ====== ======
  col1    col2   col3
  ======= ====== ======
  row1    a      b
  row2    a      b
  row3    a      b
  ======= ====== ======


その場でCSV風に書く
----------------------------------
.. csv-table:: Frozen Delights!
    :header: "Treat", "Quantity", "Description"
    :widths: 15, 10, 30

    "Albatross", 2.99, "On a stick!"
    "Crunchy Frog", 1.49, "If we took the bones out, it wouldn't be
    crunchy, now would it?"
    "Gannet Ripple", 1.99, "On a stick!"

↑の表は↓のコードによって書かれています
::
  .. csv-table:: Frozen Delights!
      :header: "Treat", "Quantity", "Description"
      :widths: 15, 10, 30

      "Albatross", 2.99, "On a stick!"
      "Crunchy Frog", 1.49, "If we took the bones out, it wouldn't be
      crunchy, now would it?"
      "Gannet Ripple", 1.99, "On a stick!"

リストテーブル
----------------------------------
.. list-table::
    :widths: 15 10 30
    :header-rows: 1

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

↑の表は↓のコードによって書かれています
::
  .. list-table::
      :widths: 15 10 30
      :header-rows: 1

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

PlantUml
==================================
公式ページ解説: https://plantuml.com/ja/sequence-diagram

.. uml::

  !define MAIN_ENTITY #E2EFDA-C6E0B4
  !define MAIN_ENTITY_2 #FCE4D6-F8CBAD

  !define METAL #F2F2F2-D9D9D9
  !define MASTER_MARK_COLOR AAFFAA
  !define TRANSACTION_MARK_COLOR FFAA00

  skinparam class {
    BackgroundColor METAL
    BorderColor Black
    ArrowColor Black
  }

  package "データベース" as DB <<Database>> {
      entity "テーブルA" as table_A <<M,MASTER_MARK_COLOR>> {
        外部キー
        --
        ID
        名前
      }

      entity "テーブルB" as table_B <<M,MASTER_MARK_COLOR>> {
        外部キー
        --
        ID
        名前
      }

      table_A ---o{  table_B
  }

↑の図は↓のコードによって書かれています
::

  .. uml::

    !define MAIN_ENTITY #E2EFDA-C6E0B4
    !define MAIN_ENTITY_2 #FCE4D6-F8CBAD

    !define METAL #F2F2F2-D9D9D9
    !define MASTER_MARK_COLOR AAFFAA
    !define TRANSACTION_MARK_COLOR FFAA00

    skinparam class {
      BackgroundColor METAL
      BorderColor Black
      ArrowColor Black
    }

    package "データベース" as DB <<Database>> {
        entity "テーブルA" as table_A <<M,MASTER_MARK_COLOR>> {
          外部キー
          --
          ID
          名前
        }

        entity "テーブルB" as table_B <<M,MASTER_MARK_COLOR>> {
          外部キー
          --
          ID
          名前
        }

        table_A ---o{  table_B
    }