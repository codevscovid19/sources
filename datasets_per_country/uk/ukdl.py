
# this is basically a bash script written in python

import subprocess

data_url_head = "https://raw.githubusercontent.com/tomwhite/covid-19-uk-data/master/data/"


def download_the_data (data_file_name) :
  data_url = data_url_head + data_file_name
  try :
    subprocess . check_call ([ "wget", "--no-check-certificate", "--content-disposition", data_url ])
  except (FileNotFoundError) :
    subprocess . check_call ([ "curl", "-LJ0", data_url, "-o", data_file_name ])

download_the_data ("covid-19-indicators-uk.csv")
download_the_data ("covid-19-cases-uk.csv")



