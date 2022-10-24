保持CSV文件时使用"CSV (Comma delimited)(*.csv)" without BOM这种

Import may fail if the created CSV file contains hidden headers such as BOM (byte order mark).  
CSV files created in Excel or text editors should not describe hidden headers.

For example, when saving a table created in Excel, we see two types of CSV formats.  
"CSV UTF-8 (Comma delimited)(*.csv)" and "CSV (Comma delimited)(*.csv)".  

![](https://support.sw.siemens.com/kbassets/external/MG620572/images/11.png)

Although both have the same extension, the former gives a UTF-8 description as a BOM, which may cause problems in importing to Flotherm.  
Therefore, users should save the latter as "CSV (Comma delimited)(*.csv)" without BOM.