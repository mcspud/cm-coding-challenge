# Overview

We have a list (Array) of 1000 Javascript maps (Objects), that have been pulled down from the internet somewhere.  This data can be found in `data.txt`.  We'd like to give an interface to our users to do the following:

1. Display a list of the data to the end user, in a table-like format
2. Have the user enter a value into a search box, and have the data filter in the list if it partially matches on any of the properties
3. Give the user the ability to sort the data *by one column only* (ie there is no requirement to chain the sorts)

Since there is lots of data in the list, the user is going to need to be able to paginate through the items.  The user should be able to select the page size from a dropdown - the options being 10, 25 and 50; and with the default value being 10.

## Tools  
React  
Redux

**bonus points**  
Reselect  
Immutable  

There is 0 requirement for styling in this challenge.  If you'd like to pretty it up with bootstrap or something then by all means, but you will not be judged on this at all.

A wireframe has been provided for reference if you need it, but you are in no way required to follow that layout.
