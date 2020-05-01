電子チケット案件TOP
=====================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

プロジェクト概要
================
* 東急スポーツオアシスサイトに、新機能として「|projectName|」を組み込む
* うち、本プロジェクトでは管理サイトを構成する

.. csv-table::
   :file: /app/source/_static/csv/pageList.csv
   :header-rows: 1
   :widths: 1, 10

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
