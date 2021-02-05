=========================
|page.admin.template|
=========================

.. list-table::
   :stub-columns: 1
   :widths: 30, 120

   * - 画面ID
     - 9999
   * - 画面概要
     - この画面はテンプレートです
   * - 公開範囲
     - 認証必須 or オープンなど

|design.req|
=================================

|design.req.header|
-----------------------
.. list-table::
   :stub-columns: 1
   :widths: 30, 120

   * - |design.req.method|
     - |design.req.method.post|
   * - |design.req.route|
     - |page.admin.template.url|
   * - token
     - ${token}
   * - |design.ctype|
     - |design.ctype.form|

|design.req.params|
------------------------
.. list-table:: |design.req.params.route|
   :stub-columns: 1
   :widths: 30, 120

   * - id
     - ユーザーID

.. list-table:: |design.req.params.query|
   :stub-columns: 1
   :widths: 30, 120

   * - search
     - 検索ワード
   * - page
     - ページ数

.. list-table:: |design.req.params.payload|
   :stub-columns: 1
   :widths: 30, 120

   * - answer
     - 1/2/3/4

.. list-table:: |design.req.params.header|
   :stub-columns: 1
   :widths: 30, 150

   * - token
     - cookeに保存されたログイントークン

メタ情報
------------------------
.. list-table::
   :stub-columns: 1
   :widths: 30, 120

   * - タイトル
     - テンプレート画面タイトル
   * - キーワード
     - sphinx, document, template
   * - ディスクリプション
     - sphinxを使ったドキュメントテンプレートです。

GA設定タグ
------------------------
<script> (function(i,s,o,g,r,a,m){-- 中略; </script></head>

|design.view|
=================================
.. list-table::
   :widths: 120

   * - .. image:: /_static/img/pages/admin/template/view_google.png

.. list-table::

   * - caseA_before

       .. image:: /_static/img/pages/admin/template/view_google_partial_1.png
     - caseA_after

       .. image:: /_static/img/pages/admin/template/view_google_partial_1.png
     - caseB_before

       .. image:: /_static/img/pages/admin/template/view_google_partial_1.png
     - caseB_After

       .. image:: /_static/img/pages/admin/template/view_google_partial_1.png

.. list-table:: アイテム
   :header-rows: 1
   :widths: 1, 20, 10, 20, 20

   * - |label.num|
     - 名前
     - 種類
     - イベント
     - 動的要素
   * - 1
     - ログインボタン
     - button
     - 画面表示 / クリック
     - 非ログイン時のみ出現
   * - 2
     - ユーザー名
     - text
     - 画面表示 / クリック
     - | ログイン時のみ出現
       | ユーザー名を表示
   * - 3
     - Googleについて
     - text
     - クリック
     - \-
   * - 4
     - 検索
     - form
     - \-
     - \-
   * - 5
     - Google検索
     - button
     - クリック
     - \-
   * - 6
     - セレクト
     - form
     - \-
     - 検索に文字入力をすると表示
   * - 7
     - セレクト2
     - form
     - \-
     - セレクト1を選択している間のみ追加

.. note::

  * 種類は area / text / image / button(submitも含める) / form のいずれかとする
  * hrefによる遷移もクリックイベントとして扱う

|design.proc|
=================================

バリデーションチェック
---------------------------------
  以下基準でPOSTパラメータの判定を行う

  .. list-table:: 判定基準
     :header-rows: 1

     * - 対象
       - 判定
     * - value
       - is_valie を含む
     * - ammount
       - 0 - 15 または 100 以上

  .. list-table:: 成果
     :stub-columns: 1

     * - バリデーション結果
       - 適合または不適合


${バリデーションチェック.バリデーション結果}が不適合の場合
--------------------------------------------------------------------------
  リダイレクトし、以降の処理を継続しない

  .. list-table:: リダイレクト先
     :stub-columns: 1

     * - 前画面名
       - /previous/input

DBデータ取得
---------------------------------
  以下条件でデータ取得

  .. list-table:: DBデータ取得
     :stub-columns: 1

     * - database.sale
       - * `modified_at`が当日08:00以降
         * `flg`が true または false

  .. list-table:: 成果
     :stub-columns: 1

     * - 当日度の売上データ
       - array<売上データオブジェクト>

DBデータ整形
---------------------------------
  ${DBデータ取得.当日度の売上データ}から二分割したデータを作成する

  グループABどちらにも属さないデータがある場合、処理を中断

  .. list-table:: 中断時の例外
     :header-rows: 1

     * - 例外クラス
       - メッセージ
     * - MyException
       - unexpected data structure: ${データのID}.

  .. list-table:: 成果
     :stub-columns: 1

     * - グループAデータ
       - array<タイトルにAを含む売上データオブジェクト>
     * - グループBデータ
       - array<タイトルにBを含む売上データオブジェクト>

|design.proc.render|
---------------------------------

  ビューに以下の変数を渡し、 |design.proc.render| する

  .. list-table:: |design.proc.set_view_vars|
     :header-rows: 1
     :widths: 8, 10, 12, 30, 30

     * - |label.num|
       - |label.name_phy|
       - |label.name_loc|
       - |label.src|
       - |label.remarks|
     * - 1
       - groupA
       - グループA
       - ${DBデータ整形.グループAデータ}
       - \-
     * - 2
       - groupB
       - グループB
       - ${DBデータ整形.グループBデータ}
       - \-

|design.event|
=================================
リンク「TOPへ」をクリックしたとき
-----------------------------------
  .. list-table:: |design.event.link_to|
     :stub-columns: 1

     * - 遷移先画面名
       - /previous/input

リンク「検索」をクリックしたとき
-----------------------------------
.. list-table:: |design.event.link_to| (action)
   :stub-columns: 1

   * - 遷移先画面名
     - /next_page

.. csv-table:: |design.form.params.get|
   :file: /docs/source/_static/csv/form/test.csv
   :header-rows: 1
   :widths: 1, 15, 10, 10, 20, 20, 5, 5


連携機能
=================================
.. list-table::
   :widths: 30, 120

   * - XXX レコメンドエンジン
     - 連携内容の説明
   * - YYY API
     - 連携内容の説明