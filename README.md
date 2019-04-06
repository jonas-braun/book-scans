!["example-page"](cover.jpg?raw=true)

# Beautiful Book-Scans

Many old texts are available in the public domain as high-quality scans, yet the glory of their original type-setting is somewhat lost.

This is a machine learning approach to creating vector-based, beautiful and accurate digital reproductions of old texts.

An example text is included.

Use the `extract_characters.py` script to find characters and ligatures from the pages. The parameters in the script can be tuned to provide basic filtering / thresholds.

`training_select.py` is used to manually annotate / label the ligatures.

From this labelled training set, two machine learning tasks ensue. One is finding the typesetting paramaters, paragraphs, spacing, etc (TODO). The other task is to generate an accurate vector-representation of the font used. Therefore, the average of all occurences of a character is calculated. This average is a reconstruction of the original "sort" or "type" used for the printing and can be vectorized to get the font.


Dependencies:
* python3
* OpenCV3
