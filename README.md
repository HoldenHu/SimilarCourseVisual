# SimilarCourseVisual
##Description
**For WING's task one**. Crawl some courses codes and descriptions from *NUSmodules*.  Take the descriptions and encode them into thought or doc vectors via word embeddings).  Give a visualization on how the courses relate to each other. 

##File Structure
SimilarCourseVisual/   
|-- bin/　 <small>*(Executable files for the project)*</small>  
|　 |-- \__init__  
|　 |-- start.py　 <small>*(Starting program)*</small>     
|-- core/　 <small>*(Store all source code for the project (core code))*</small>   
|　 |-- tests/　 <small>*(Store unit test code)*</small>     
|　 |　 |-- __init__.py   
|　 |　 |-- test.main.py     
|　 |-- __init__.py     
|　 |-- test_main.py　 <small>*(Store core logic)*</small>       
|-- conf/　 <small>*(Configuration file)*</small>     
|　 |-- __init__.py     
|　 |-- setting.py　 <small>*(Write the relevant configuration)*</small>       
|---db/    #Database files     
|　 |--db.json　 <small>*(Store database files)*</small>       
|-- docs/　 <small>*(Store some documents)*</small>       
|-- lib/　 <small>*(Library files, put custom modules and packages)*</small>       
|　 |-- __init__.py     
|　 |-- common.py　 <small>*(Write commonly used functions)*</small>       
|-- log/　 <small>*(Log files)*</small>       
|　 |-- access.log　 <small>*(logs)*</small>       
|-- README　 <small>*(Project description document)*</small>       