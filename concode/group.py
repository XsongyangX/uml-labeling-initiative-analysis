# Groups the data together in preparation for learning

# Format:
# Each line corresponds to its translation counterpart

# english.txt: One English description per line
# fragments.txt: One fragment of UML in flattened plantuml per line

# Divide each language in 3 parts: training, validation, test

# ------
import sys
if len(sys.argv) != 3:
    print("Usage: py group.py fragment-folder plantuml-folder", file=sys.stderr)
    sys.exit(1)

# Read source
import pandas as pd
import os

from sklearn.model_selection import train_test_split

def read_source(fragment_folder, plantuml_folder):
    
    labels = pd.read_csv(os.path.join(fragment_folder, "labels.csv"))
    fragments = pd.read_csv(os.path.join(fragment_folder, "fragments.csv"))

    paired_labels = []
    paired_fragments = []
    
    # sort fragments according to id
    # id starts at 1
    fragments.sort_values(by=['unique_id'], inplace=True)

    # iterate through labels
    for index, label in labels.iterrows():
        tokenize = " ".join(label["label"].split())

        paired_labels.append(tokenize)

        fragment = fragments.iloc[label["fragment_id"] - 1]

        # open fragment plantuml code
        fragment_file = "{model}_{kind}{number}.plantuml".format(model=fragment["model"], kind=fragment["kind"], number=fragment["number"])
        flatten = open(os.path.join(plantuml_folder, fragment_file), "r").read().replace("\n", " 0newline0 ")

        paired_fragments.append(flatten)
        
    # output to files
    import json

    # split
    train_english, test_english, train_fragments, test_fragments = train_test_split(paired_labels, paired_fragments, test_size = 0.02)

    train_english, valid_english, train_fragments, valid_fragments = train_test_split(train_english, train_fragments, test_size=0.5)

    os.makedirs("data", exist_ok=True)

    for section, eng, frag in [("train", train_english, train_fragments),
        ("valid", valid_english, valid_fragments),
        ("test", test_english, test_fragments)]:
        
        with open(f"data/{section}.json", "w") as dataset:
            for one_eng, one_frag in zip(eng, frag):
                dataset.write(json.dumps(
                    {
                        "nl": one_eng,
                        "code": one_frag
                    }
                ) + "\n")
            

read_source(sys.argv[1], sys.argv[2])
