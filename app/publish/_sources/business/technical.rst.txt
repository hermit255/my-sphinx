======================================
技術要件
======================================
.. uml::

  rectangle EC2{
    node nginx
    card php {
      card Laravel
    }
    database db
  }

  db -- Laravel
  nginx -- Laravel



.. list-table::
   :header-rows: 1
   :widths: 15, 10, 30

   * -
     - version
     - その他
   * - Laravel
     - 7.0
     - requires PHP7.2.5
   * - PHP-fpm
     - 7.4.3
     -
   * - PostgreSQL
     - 9.6.17
     -
   * - nginx
     - latest
     -
