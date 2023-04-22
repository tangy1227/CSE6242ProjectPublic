# CSE6242Project

## Instructions to run the D3-based tool:
* Download `data.csv` from https://drive.google.com/file/d/15ThtXZSPA49Y-jtjRzYFawzeLRTBwvAs/view?usp=sharing
* Place `data.csv` in the `CODE/visualization/` directory
* Open a terminal window, and navigate to the top-level project directory.
* Create a conda environment with all required packages by running: 
```bash
conda create --name 6242_env python=3.8
conda activate 6242_env
pip install -r requirements.txt
```
(note that an anaconda installation is a prerequisite here)
* Then, to get started, run:
```bash
cd CODE/visualization/
python create_database.py
python app.py
```
* Open a second terminal window, navigate to the top-level project directory, and run
```bash
cd CODE/visualization/
python -m http.server 8000
```
* Finally, open a browser, and navigate to http://localhost:8000/chloropleth_map.html

## Instructions to run the Tableau-based tool:
* Visit the Dropbox link in `link-to-tableau.txt`
* Download the packaged workbook `CSE6242Project_Sastry.twbx` (which includes the datasets it relies on)
* Open in Tableau Desktop Professional Edition (Tested on 2022.4.1)
* Navigate to "Dashboard"
