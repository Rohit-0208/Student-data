import pandas as pd                             # Import pandas library for data analysis and manipulation
import webbrowser                              # Import webbrowser library to open URLs
import time as tm                               # Import time library (aliased as tm) for delays


def open_urls(filename):
  
  try:
    data = pd.read_excel(filename)                    #reads the excel  file
  except FileNotFoundError:        
    print(f"Error: File '{filename}' not found.")             #this mesage will be printed if there is no file found.
    return
  except pd.errors.ParserError:                     #error is displayed when the file is not format.
    print(f"Error: Unable to parse '{filename}' as Excel.")
    return
  
  car_names = data.iloc[:, 0].tolist()                      # it will append all the elements in 1 column to list.

  urls = data.iloc[:, 1].tolist()                # it will append all the elements in 2 column to list.

 
  for car_name, url in zip(car_names, urls):    #zip is used to iterate two lists symeltaneously i used this because in list1 there are car names and list2 there is url to print car names i used zip function.

    try:
      print(f"Opening car: {car_name}")
      webbrowser.open(url)
      tm.sleep(10)                               # this will pause the code for 10 sec. After 10 sec code will execute.
    except webbrowser.BrowserError:               #error in opening broswer this block will execute.
      print(f"Error: Unable to open URL: {url}")


open_urls("data.xlsx") 
