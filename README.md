# Cleaning of the database
Data comes from umllabels.herokuapp.com

## Usage
* `get.sh` will get the data from the cloud and export csv data locally
* `download_zoo.sh` gets the image data from github

### NMT
NMT uses the framework at https://github.com/lmthang/nmt.hybrid. 
* `flatten.sh` will change the newlines to `0newline0` tokens. Used to get one line of plantuml.
* `expand.sh` reverses the effect of flattening
* `tokenize.sh` replaces newlines by spaces
* `group.py` groups the data for training
* `install.sh` prepares the code for the training model
* `train.sh` trains a model given a previously processed data by `group.py`
* `test.sh` tests the model by decoding and using BLEU

### CONCODE
Completely broken

### 3step
```bash
git submodule init
git submodule update
```
