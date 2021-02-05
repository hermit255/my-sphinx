==============
DB構成
==============
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