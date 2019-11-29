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

