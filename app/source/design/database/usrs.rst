======================
|usrs.label|
======================
テーブル定義
----------------------------------
.. csv-table:: |usrs.table|
   :file: /docs/source/_static/csv/database/users.csv
   :header-rows: 1
   :widths: 10, 30, 20, 10, 10, 10, 20, 30


フラグ・ステータス定義
----------------------------------
.. list-table:: ユーザー種別
    :widths: 10 30
    :stub-columns: 1

    * - 1
      - 一般ユーザー
    * - 2
      - 特権ユーザー
    * - 3
      - 管理ユーザー

.. list-table:: ステータス
    :widths: 10 30
    :stub-columns: 1

    * - 200
      - 正常
    * - 400
      - BadRequest
    * - 500
      - 内部エラー