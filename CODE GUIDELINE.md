# CODE GUIDELINE FOR PROJECT AIS-3USON

## Client side
### View Widgets
The names of QTableView, QComboBox is defined by used model and filters:
 * Used prefixes:
    * table_
    * t_sql_
    * cbx_0_ - where zero is 0-9 – number of displayed column
    * clndr_
        
 * Used postfixes(in that order):
    * _\_where\_<field> - only select where field = value (by default select None)
    * _raw            - don't use relations in model
    * _\_by\_<field>    - add filter by field

### Models
Model names usually is a substring from view name:
 * = sql table/view names +- "_raw"
 * but if there are "__where__" used - then used full name, except widget prefix ???
 
> (because while all model loaded fully and can be reused, models with __where__ only have partial(volatile) data and thus not eligible for reuse )

- [ ] TODO: maybe mark for reuse for widgets on one tab?...

### Shared data
#### SD 
 * app settings
 * app global state
 * support data for:
    * models
    * connections
    * threads
    * etc...
#### WD 
 * data work logic
 * model managment
 * sql queries
 #### UI 
 * global ui data
 
 
## SQL side
Table names start from letters, view names start from "_".

SQL table used as source for relational data should have:
 * id (int/bigint >0)
 * table_name - unique varchar
 * all other fields


SQL schema have views with prefix __updatable___ used for update tables. All other view for selection only.
updatable_ tables only have columns from one table.

_table1_has_table2  - all record of table2 for record in table1(0 or one or two columns from table1)
first column from table1

Security settings stored in file sql/security.sql
