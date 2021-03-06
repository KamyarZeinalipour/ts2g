# ts2g (time series to graph)
This a package for converting timeseries to graph using three different method which are natural visibility graph, horizontal visibility graph and quantile graph
this three methods are come from the following articels:

Lacasa, Lucas, Bartolo Luque, Fernando Ballesteros, Jordi Luque, and Juan Carlos Nuño. 2008. “From Time Series to Complex Networks: The Visibility Graph.” Proceedings of the National Academy of Sciences of the United States of America 105 (13): 4972–75.

Luque, B., Lacasa, L., Ballesteros, F. and Luque, J., 2009. Horizontal visibility graphs: Exact results for random time series. Physical Review E, 80(4).

Campanharo, A., Sirer, M., Malmgren, R., Ramos, F. and Amaral, L., 2011. Duality between Time Series and Networks. PLoS ONE, 6(8), p.e23378.

# Dependencies:

openpyxl

# How to install package:

1. install python > 3.6 [how to install?](https://www.python.org/downloads/)
2. install pip [how to install?](https://pip.pypa.io/en/stable/installation/)
3. open terminal (linux or mac) or command prompt (windows):

to open terminal if you are using mac:
    1. Press Command + Space Bar on your Mac Keyboard.
    2. Type in “Terminal”
    3. When you see Terminal in the Spotlight search list, click it to open the app.

to open command prompt if you are using windows:
    1. right-click the Windows icon in the bottom-left corner of your screen.
    2. click on powershell(admin) or command prompt(admin)

4. and then enter this command
```sh
pip install openpyxl && pip install ts2g
```

and hit enter!
done.

# How to import:

```sh
import ts2g
```


# How to use:

```python
#import your data! data should be .csv or .xlsx file 
#for example:
data = ts2g.importData("data.csv") # this function will return a matrix of data
#replace you data file with data.csv

#then calculate the data:

#for vertical visibility graph, example:
result = ts2g.vg(data) # this function will return a matrix of results

#for horisantal visibility graph, example:
result = ts2g.hg(data) # this function will return a matrix of results

#for quantile graph, example:
q = 10
result = ts2g.qg(data, q) # this function will return a matrix of results


#then save result!

ts2g.save(result, "name") #this funtion will save results in .txt files!
```


# How saved files are look like:

### if result is for vg, saved files will be:
1. name_A_vg.txt
2. name_graph_indicator_vg.txt
3. name_node_labels_vg.txt

### if result is for hg, saved files will be:
1. name_A_hg.txt
2. name_graph_indicator_hg.txt
3. name_node_labels_hg.txt

### if result is for qg, saved files will be:
1. name_A_qg_q=10.txt
2. name_graph_indicator_qg_q=10.txt
3. name_node_labels_qg_q=10.txt
4. name_edge_labels_qg_q=10.txt

# note:
We strongly suggest using .csv, don't use .xlsx for big files!