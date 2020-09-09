#Text Files

filename = 'textfile.txt'

file = open(filename, mode = 'r') #Read, not write. Open a connection to the file

text = file.read()

...

file.close()


with open('textfile.txt') as file #context manager- file is now equal to open('textfile.txt')

#--------------------------------------------------------------------------------------------------------------------
#IMPORTING USING NUMPY

np.loadtext(filename, delimiter, skiprows, usecols[...], dtpye) #dtype ensures al data is imported as a certain type

np.genfromtext(filename, delimiter, skiprows, usecols[...], dtpye, names=True/False) #names indicates if there's a header, dtype = none lets numpy figure out data type for each value

np.recfromcsv() #default dtype is 'None', delimiter is ',' and names is 'True'

#--------------------------------------------------------------------------------------------------------------------
#IMPORTING USING PANDAS

pd.read_csv('file.csv')

array = dataframe.values #turns dataframe into a numpy array

#--------------------------------------------------------------------------------------------------------------------

#PICKLED FILES

#Native to Python

#Pickled == Serialize == transform into a sequence of bytes (bytestream)

#Open and load pickled file
with open('data.pkl', 'rb') as file:
    d = pickle.load(file)

#--------------------------------------------------------------------------------------------------------------------

#EXCEL FILES

pd.ExcelFile(file)

.parse(sheet_name or index, skiprows = [], names = [], usecols = []) #Loads Excel sheet as DataFrame. 

#--------------------------------------------------------------------------------------------------------------------

#SAS/STATA FILES

#SAS: sas7bdat or sas7bcat

#STATA: .dta

file.to_data_frame()

pd.read_stata('file.dta')

#--------------------------------------------------------------------------------------------------------------------

#HDF5 (Hierarchical Data Format)

#Standard for large numerical data

import h5py

h5py_data = h5py.File(h5py_file, 'r')

#--------------------------------------------------------------------------------------------------------------------

#MatLab

#scipy.io.load/savemat() for reading and writing

#A '.Mat' file is a collection of structures. It's imported a dict, where keys are variables and values are objects assigned to those variables.

import scipy.io

#--------------------------------------------------------------------------------------------------------------------

#Relational Databases

#SQLAlchemy package

#Creating a Database engine to communicate with the database

from sqlalchemy import create_engine

engine = create_engine('sqlite:///database.sqlite')

with engine.connect() as con:
    rs = con.execute("SELECT LastName, Title from Employee" )
    df = pd.DataFrame(rs.fetchmany(3))
    df.columns = rs.keys()

#Querying with pandas

pd.read_sql_query(query, engine) #saves in a DataFrame

df = pd.read_sql_query('SELECT * FROM PlaylistTrack INNER JOIN Track on PlaylistTrack.TrackId = Track.TrackId WHERE Miliseconds < 25000',engine) #example with inner join

#--------------------------------------------------------------------------------------------------------------------

#Importing from Web

from urllib.request import urlretrieve

urlretrieve(url, filename) #to save file locally. Performs GET Request.

df = pd.read_csv(url, sep = ';') #import into DataFrame directly from web

dict = pd.read_excel(url, sheet_name = None) #dict with sheets as keys and DataFrames as values

#GET with urllib

from urllib.request import urlopen, Request

request = Request(url)

response = urlopen(request)

html = response.read()

request.close()

#GET using requests package

r = requests.get(url) #single line and no need to close connection

#using BeautifulSoup for parsing HTML

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc)

prety_soup = soup.prettify()

a_tags = soup.find_all('tagname') #find all objects with 'tagname' tag

element.get('attribute') 

#--------------------------------------------------------------------------------------------------------------------

#API's and JSON's

import json

with open("a_movie.json") as json_file: #json's are imported as dicts
    json_data = json.loads(json_file)

r = requests.get(url)

r.json() #creates a dict from a json file




