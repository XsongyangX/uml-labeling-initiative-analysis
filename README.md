# Cleaning of the database
Data comes from umllabels.herokuapp.com

## Usage
* `get.sh` will get the data from the cloud and export csv data locally

### NMT
NMT uses the framework at https://github.com/lmthang/nmt.hybrid. 
* `flatten.sh` will change the newlines to `0newline0` tokens. Used to get one line of plantuml.
* `expand.sh` reverses the effect of flattening
* `tokenize.sh` replaces newlines by spaces