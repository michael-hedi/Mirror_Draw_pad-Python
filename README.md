Query Editor API Documentation
==
Error_codes
==

### Errors={                
        'ERR_100' : 'Error in POST json',
        'ERR_101' : 'Invalid RequestID',
        'ERR_102' : 'InternalMysqlDbConnectionRefuse',
        'ERR_202' : 'RedshiftConnectionRefuse',
        'ERR_201' : 'InvalidQueryInput'         
        }
Endpoints
==

## **/download**

> **methods allowed = POST**
>
### ***Request***
~~~JSON
    {
        "query" : "<SQL statments>" 
    }
~~~
### ***Response***
~~~JSON
    {
        "data"    :"<request_id>",
        "status"  :200
    }
 ~~~
### ***Error***
>
* If requset data body is not correct.
~~~JSON
    {
        "status"    : 100,
        "error"     : "Error in POST json",
        "error_msg" : "<error message>"
        
    }
~~~
***
## **/download_status**

> **methods allowed = POST**
>
### ***Request***

~~~JSON
    {
        "request_id" : "<request id>" 
    }
~~~
### ***Response***
~~~JSON
    {
        "data"    : {
                    "RID"           : "<request id>",
                    "query"         : "<SQL satatement>",
                    "status"        : "( Ready' | 'Processing' | 'Completed' | 'Failed )"
                    "url"           : "<S3 bucket url>",
                    "error"         : "if occur in tranction",
                    "public_url"    : "< pres_signed url >"
                 },
        "status"  : 200
    }
 ~~~
### ***Error***
* If request data body is not correct 

~~~JSON
    {
        "status"    : 100,
        "error"     : "Error in POST json"
        "error_msg" : "<error message>"
    }
~~~
* If given request id is invaid

~~~JSON
    {   
        "status"    : 101,
        "error"     : "Invalid RequesId",
        "error_msg" : "<error message>"
    }
~~~
***
## **/query**
> **method allowed = POST**
>
### ***Request***

~~~JSON
    {
        "query" : "<SQL statement>"
        "limit" : "<limit integer to fetch number of rows> *optional"
    }
~~~
### ***Response***
~~~JSON
    {
        "data"  : [
                    {
                        "<column_name>" : "<data>",
                        "<column_name>" : "<data>",
                        "<column_name>" : "<data>"
                    },
                    {
                        "<column_name>" : "<data>",
                        "<column_name>" : "<data>",
                        "<column_name>" : "<data>"
                    }
        ],
        "status"    : 200
    }
~~~
### ***Error*** 
* If request data body is not correct
~~~JSON
    {
        "status"    : 100,
        "error"     : "Error in POST json",
        "error_msg" : "<error message>"
        
    }
~~~
* If error in redshift connection 
~~~JSON
    {
        "status"    : 202,
        "error"     : "RedshiftConnectionRefuse",
        "error_msg" : "<error message>"
        
    }
~~~
* If qurey is incorrect 
~~~JSON
    {
        "status"    : 201,
        "error"     : "InvalidQueryInput",
        "error_msg" : "<error message>"
        
    }
~~~
***
## /get_md
> **method allowed = POST**
>
### ***Request***

~~~python
    None
~~~
### ***Response***
~~~JSON
    {
        "data"  : [
                    {
                        "db" : "<database name>",
                    },
                    {
                        "db" : "<database name>",
                    },
                    {
                        "db" : "<database name>",
                    }
                ],
        "status"    : 200
    }
~~~
### ***Error*** 
* If error in redshift connection 
~~~JSON
    {
        "status"    : 202,
        "error"     : "RedshiftConnectionRefuse",
        "error_msg" : "<error message>"
        
    }
~~~
## /get_md/'database_name'
> **method allowed = POST**
>
### ***Request***

~~~python
    None
~~~
### ***Response***
~~~JSON
    {
        "data"  : [
                    {
                        "schema" : "<schema name>",
                    },
                    {
                        "schema" : "<schema name>",
                    },
                    {
                        "schema" : "<schema name>",
                    }
                ],
        "status"    : 200
    }
~~~
### ***Error*** 
* If error in redshift connection 
~~~JSON
    {
        "status"    : 202,
        "error"     : "RedshiftConnectionRefuse",
        "error_msg" : "<error message>"
        
    }
~~~
## /get_md/'database_name'/'schema_name'
> **method allowed = POST**
>
### ***Request***

~~~python
    None
~~~
### ***Response***
~~~JSON
    {
        "data": [
                  {
                    "table_name": "<tabel name>",
                    "table_type": "<view or table>""
                  },
                  {
                    "table_name": "<tabel name>",
                    "table_type": "<view or table>"
                  },
                  {
                    "table_name": "<tabel name>",
                    "table_type": "<view or table>"
                  }
                ],
        "status"    : 200
    }
~~~
### ***Error*** 
* If error in redshift connection 
~~~
    {
        "status"    : 202,
        "error"     : "RedshiftConnectionRefuse",
        "error_msg" : "<error message>"
        
    }
~~~
## /get_md/'database_name'/'schema_name'/'table_name'
> **method allowed = POST**
>
### ***Request***

~~~python
    None
~~~
### ***Response***
~~~JSON
    {
        "data": [
            {
                "column_name": "venueid",
                "data_type": "smallint"
            },
            {
                "column_name": "venuename",
                "data_type": "character varying"
            },
            {
                "column_name": "venuecity",
                "data_type": "character varying"
            },
            {
                "column_name": "venuestate",
                "data_type": "character"
            },
            {
                "column_name": "venueseats",
                "data_type": "integer"
            }
    ],
    "status": 200
}
~~~
### ***Error*** 
* If error in redshift connection 
~~~JSON
    {
        "status"    : 202,
        "error"     : "RedshiftConnectionRefuse',
        "error_msg" : "<error message>"
        
    }
~~~

    
