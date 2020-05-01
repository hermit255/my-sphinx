######################
実践的な記述(ビュー)
######################

.. comment

.. _practice_interface:

商品情報画面 - |interface|
#################################

  商品情報画面を表示する

---------
|request|
---------

.. csv-table:: |headers|
   :file: /app/source/_static/csv/api/view1/req_headers.csv
   :header-rows: 1
   :widths: 8, 40, 60

.. csv-table:: |params|
   :file: /app/source/_static/csv/api/view1/req_params.csv
   :header-rows: 1
   :widths: 8, 10, 20, 10, 10, 40

----------
|response|
----------

.. csv-table:: |headers|
   :file: /app/source/_static/csv/api/view1/res_headers.csv
   :header-rows: 1
   :widths: 8, 40, 60

商品情報画面 - |process|
#################################

------------------------
1. API1から情報を取得
------------------------

.. _practice_request_to_api1:

1-1. リクエスト送信
--------------------

    処理フロー
  .. uml::

      skinparam monochrome true

      actor User
      participant "UI" as ui
      participant "wrapperAPI" as wrapper
      participant "API" as api

      User -> ui: request
      activate ui

      ui -> wrapper: call api1
      activate wrapper

      wrapper -> api: call api2
      activate api
      api --> wrapper: response
      deactivate api

      wrapper -> api: call api3
      activate api
      api --> wrapper: response
      deactivate api

      wrapper --> ui: response
      deactivate wrapper

      ui --> ui: set_value
      ui --> User: view
      deactivate ui

.. _practice_remake_view1_response:

1-2. レスポンス調整
--------------------

  :ref:`practice_request_to_view1` のレスポンスを
  キャメル型のカラム名にして再格納する


--------------
2. |view_set| ・ |render|
--------------

.. _practice_view_set:

2-1. |view_set|
----------------------

.. csv-table::
   :file: /app/source/_static/csv/api/view1/res_body_set.csv
   :header-rows: 1
   :widths: 8, 10, 12, 30, 30

.. _practice_view_set:

2-2. |render|
----------------------

  画面を描画する

------------------------
3. |event_listen|
------------------------

3-1. 「購入」ボタンを |click|
----------------------

  ユーザー認証ダイアログを開きPINコードを入力する...

.. _practice_view_event_go_next:

3-2. 「次へ」ボタンを |click|
----------------------

  gotoページへ遷移する

.. csv-table:: |headers|
   :file: /app/source/_static/csv/api/view1/req_headers.csv
   :header-rows: 1
   :widths: 8, 40, 60

.. csv-table:: |params|
   :file: /app/source/_static/csv/api/view1/req_params.csv
   :header-rows: 1
   :widths: 8, 10, 20, 10, 10, 40

.. _practice_view_event_check_auth:

