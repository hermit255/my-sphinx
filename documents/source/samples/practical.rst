############
実践的な記述
############

.. comment

.. _practice_interface:

カート内商品取得API - |interface|
#################################

  サイト外APIのラッパーとして
  会員サイトUIから要求されるデータの取得に関して責任を負う

---------
|request|
---------

.. csv-table:: |headers|
   :file: ../resources/csv/api/api1/req_headers.csv
   :header-rows: 1
   :widths: 8, 40, 60

.. csv-table:: |params|
   :file: ../resources/csv/api/api1/req_params.csv
   :header-rows: 1
   :widths: 8, 10, 20, 10, 10, 40

----------
|response|
----------

.. csv-table:: |headers|
   :file: ../resources/csv/api/api1/res_headers.csv
   :header-rows: 1
   :widths: 8, 40, 60

.. csv-table:: |body|
   :file: ../resources/csv/api/api1/res_body.csv
   :header-rows: 1
   :widths: 8, 10, 12, 10, 10, 40

カート内商品取得API - |process|
#################################

------------------------
1. API1から情報を取得
------------------------

.. _practice_request_to_api1:

1-1. リクエスト送信
--------------------

    本文 本文 本文 本文 本文 本文 本文 本文 本文 本文

.. _practice_remake_api1_response:

1-2. レスポンス調整
--------------------

  :ref:`practice_request_to_api1` のレスポンスを
  キャメル型のカラム名にして再格納する

----------
2. |response_set|
----------

.. csv-table:: |headers|
   :file: ../resources/csv/api/api1/res_headers_set.csv
   :header-rows: 1
   :widths: 8, 40, 60

.. csv-table:: |body|
   :file: ../resources/csv/api/api1/res_body_set.csv
   :header-rows: 1
   :widths: 8, 10, 12, 30, 30
