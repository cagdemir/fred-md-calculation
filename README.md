# fred-md-calculation
Python scripts for calculating FRED-MD: A Monthly Database for Macroeconomic Research


I converted a Matlab library into python which calculates and preprocesses 150 monthly macroeconomics variables. The library was written by Assistant Vice-President of Federal Reserve Bank of St. Louis, Michael W. McCracken (McCracken and Ng, 2015). However, the original work requires users to manually download raw data and then point the module to the related path. Instead, I added a data retrieval module via St. Louis Fed’s python API which is absent in the original implementation. I also added a Python script to transform each variable into a stationary variable.



