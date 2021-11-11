# Groups the data together in preparation for learning

# Format:
# Each line corresponds to its translation counterpart

# english.txt: One English description per line
# fragments.txt: One fragment of UML in flattened plantuml per line

# Divide each language in 3 parts: training, validation, test

# ------
import sys
if len(sys.argv) != 2:
    print("Usage: py group.py source-folder", file=sys.stderr)
    sys.exit(1)

# Read source
import pandas as pd
import os
import subprocess

from sklearn.model_selection import train_test_split

def read_source(location):
    
    labels = pd.read_csv(os.path.join(location, "labels.csv"))
    fragments = pd.read_csv(os.path.join(location, "fragments.csv"))

    paired_labels = []
    paired_fragments = []
    
    # sort fragments according to id
    # id starts at 1
    fragments.sort_values(by=['unique_id'], inplace=True)

    # iterate through labels
    for index, label in labels.iterrows():
        echo = subprocess.Popen(["echo", label["label"]], stdout=subprocess.PIPE)
        tokenize = subprocess.check_output(["bash",
            "nmt/tokenize.sh"
            ], stdin=echo.stdout).decode("utf-8") 

        paired_labels.append(tokenize)

        fragment = fragments.iloc[label["fragment_id"] - 1]

        # open fragment plantuml code
        fragment_file = "{model}_{kind}{number}.plantuml".format(model=fragment["model"], kind=fragment["kind"], number=fragment["number"])
        flatten = subprocess.check_output(["bash", 
            "nmt/flatten.sh",
            os.path.join("zoo", fragment_file)]).decode("utf-8") 

        paired_fragments.append(flatten)
        
    # output to files

    # split
    train_english, test_english = train_test_split(paired_labels, test_size = 0.1)
    train_fragments, test_fragments = train_test_split(paired_fragments, test_size = 0.1)

    train_english, valid_english = train_test_split(train_english, test_size=0.25)
    train_fragments, valid_fragments = train_test_split(train_fragments, test_size=0.25)

    os.makedirs("nmt/data", exist_ok=True)
    for section, eng, frag in [("train", train_english, train_fragments),
        ("valid", valid_english, valid_fragments),
        ("test", test_english, test_fragments)]:
        
        with open(f"nmt/data/{section}.en", 'w') as english:
            for line in eng:
                english.write(line + "\n")
        with open(f"nmt/data/{section}.uml", 'w') as target:
            for line in frag:
                target.write(line + "\n")

read_source(sys.argv[1])
