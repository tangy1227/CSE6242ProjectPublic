# CSE6242Project

#### Instructions to run the D3-based tool:
* Download `data.csv` from https://drive.google.com/file/d/15ThtXZSPA49Y-jtjRzYFawzeLRTBwvAs/view?usp=sharing
* Place `data.csv` in the `CODE/visualization/` directory
* Create a conda environment with the required packages listed in `requirements.txt`. Note that an anaconda installation is a prerequisite:
```bash
conda create --name 6242_env python=3.8
conda activate 6242_env
pip install -r requirements.txt
```
* Run:
```bash
cd CODE/visualization/
python create_database.py
```
* Open two terminal windows. Execute `python app.py` in one window, and `python -m http.server 8000` the second window.
* Open a browser, and navigate to http://localhost:8000/chloropleth_map.html

#### Instructions to run the Tableau-based tool:
* Visit the Dropbox link in `link-to-tableau.txt`
* Download the packaged workbook `CSE6242Project_Sastry.twbx` (which includes the datasets it relies on)
* Open in Tableau Desktop Professional Edition (Tested on 2022.4.1)
* Navigate to "Dashboard"
