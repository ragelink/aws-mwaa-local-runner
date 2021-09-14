#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
"""
Example use of MySql related operators.
"""

from airflow import DAG
from airflow.providers.mysql.operators.mysql import MySqlOperator
from airflow.utils.dates import days_ago

dag = DAG(
    'example_mysql',
    start_date=days_ago(2),
    tags=['example'],
)

# [START howto_operator_mysql]

#create_table_mysql_task = MySqlOperator (
#    task_id='create_table_mysql' mysql_conn_id='mysql_leo', sql=r"""CREATE TABLE IF NOT EXISTS tasks (
#    task_id INT AUTO_INCREMENT,
#    title VARCHAR(255) NOT NULL,
#    start_date DATE,
#    due_date DATE,
#    priority TINYINT NOT NULL DEFAULT 3,
#    description TEXT,
#    PRIMARY KEY (task_id));""", dag=dag
#)

drop_table_mysql_task = MySqlOperator(
    task_id='drop_table_mysql', mysql_conn_id='mysql_leo', sql=r"""INSERT INTO tasks(title,priority) 
    VALUES('Understanding DEFAULT keyword in INSERT statement',DEFAULT);""", dag=dag
)


# [END howto_operator_mysql]

# [START howto_operator_mysql_external_file]

mysql_task = MySqlOperator(
    task_id='create_table_mysql_external_file',
    mysql_conn_id='mysql_conn_id',
    sql='/scripts/drop_table.sql',
    dag=dag,
)

# [END howto_operator_mysql_external_file]
#create_table_mysql_task >> mysql_task

drop_table_mysql_task >> mysql_task
