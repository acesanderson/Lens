────────────────────────────────────────────────────────────────────────────────────────────────────
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                 Courses Database Search Project                                  ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

This project is a Python-based command line tool for searching through a MongoDB (or potentially    
SQLite) Courses database. It supports both strict and fuzzy searches across course metadata and     
Table of Contents (TOC) to identify relevant courses based on keywords input by the user.           


                                              Features                                              

 • Keyword Search: Find courses based on keywords within the course title, description, or TOC.     
 • Fuzzy Matching: Utilize fuzzy matching to identify courses with similar but not exact keyword    
   matches.                                                                                         
 • Multiple Keyword Search: Search using multiple keywords and identify common courses.             
 • Interactive Mode: Allows for real-time interaction, prompt-based searching, and dynamic settings 
   adjustment for fuzzy matching.                                                                   


                                            Requirements                                            

 • Python 3.7+                                                                                      
 • Packages:                                                                                        
    • rich for enhanced console input/output                                                        
    • rapidfuzz for fuzzy string matching                                                           
    • argparse for command line argument parsing                                                    
    • pymongo for MongoDB access                                                                    
 • MongoDB should be properly set up with a courses database.                                       

Install the required Python packages using pip:                                                     

                                                                                                    
 pip install rich rapidfuzz pymongo                                                                 
                                                                                                    


                                             Setting Up                                             

 1 Clone the Repository                                                                             
                                                                                                    
    git clone <repository-url>                                                                      
    cd <repository-directory>                                                                       
                                                                                                    
 2 Database Configuration                                                                           
   Ensure that your MongoDB instance is running and accessible. The script is designed to connect to
   this database to fetch courses.                                                                  
 3 Running the Script                                                                               
   You can run the script in two primary modes:                                                     
                                         Non-interactive Mode:                                      
                                                                                                    
    python main.py <keyword> [-f]                                                                   
                                                                                                    
    • <keyword>: The keyword to search for.                                                         
    • -f or --fuzzy: Enable fuzzy matching.                                                         
                                           Interactive Mode:                                        
                                                                                                    
    python main.py -i                                                                               
                                                                                                    
   The interactive mode allows you to enter keywords and toggle fuzzy matching dynamically. To exit,
   type exit.                                                                                       
 4 Functionality Breakdown                                                                          
    • Type single or multiple keywords (separated by newline) for searching.                        
    • Utilize the fuzzy command to toggle fuzzy matching on or off.                                 
    • In non-interactive mode, enter keywords directly as command-line arguments.                   


                                           Usage Example                                            

If you want to find courses with the keyword Python and enable fuzzy matching:                      

                                                                                                    
 python main.py "Python" -f                                                                         
                                                                                                    

In interactive mode, after execution:                                                               

                                                                                                    
 python main.py -i                                                                                  
                                                                                                    

 • Type Python and press Enter for results.                                                         
 • Type fuzzy to toggle fuzzy matching.                                                             
 • Type exit to quit the interactive session.                                                       


                                           Contributions                                            

Contributions to the project are welcome! If you have any suggestions or improvements, feel free to 
fork the repository and submit a pull request.                                                      


                                              Support                                               

If you run into any issues or have questions, you can reach out via the issue tracker on the        
repository.                                                                                         

────────────────────────────────────────────────────────────────────────────────────────────────────
