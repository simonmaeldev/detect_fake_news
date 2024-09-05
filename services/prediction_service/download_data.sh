 #!/bin/sh                                                                                                                                                       
                                                                                                                                                                 
 # Check if news.csv exists                                                                                                                                      
 if [ ! -f news.csv ]; then                                                                                                                                 
     echo "news.csv not found. Downloading..."                                                                                                                   
     wget --no-check-certificate 'https://docs.google.com/uc?export=download&id=1er9NJTLUA3qnRuyhfzuN0XUsoIC4a-_q' -O news.csv.zip                               
     unzip news.csv.zip                                                                                                                                          
     rm news.csv.zip                                                                                                                                             
     echo "Download complete."                                                                                                                                   
 else                                                                                                                                                            
     echo "news.csv found. Skipping download."                                                                                                                   
 fi  