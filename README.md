# tools
A convenient auto tool for database performance testing, integrate sysbench and tpcc-mysql.
The tool can run database performance tools according to related config files, avoid to 
input a lot of parameters manually.

==================================
A sample sysbench command
==================================
sysbench --test=/usr/share/sysbench/tests/db/oltp.lua 
         --oltp-table-size=[table_size] 
         --oltp-tables-count=[table_counts] 
         --num-threads=[thread_numbers]
         --mysql-db=[database_name] 
         --mysql-host=[database_host_name] 
         --mysql-user=[user_name] 
         --mysql-password=[password] 
         --mysql-port=3306
         --db-driver=mysql
prepare


==================================
A sample tpcc-mysql command
==================================
./tpcc_start -h[database_host_name]
			 -d[database_name]
			 -u[user_name]
			 -p[password]
			 -w[warehouse_numbers]
			 -c[threads_numbers]
			 -r[rampup_time]
			 -l[execution_time]

