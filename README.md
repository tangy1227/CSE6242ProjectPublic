# CSE6242Project

#### Instructions to run the D3-based tool:
* Install environment and required packages (note that anaconda is a prerequisite):
```bash
conda create --name 6242_env python=3.8
pip install -r requirements.txt
```
* Activate environment and run:
```bash
conda activate 6242_env
cd CODE/visualization/
python create_database.py
```
* Open two terminal windows. Execute `python app.py` in one window, and `python -m http.server 8000` the second window.
* Open a browser, and navigate to http://localhost:8000/chloropleth_map.html

#### Instructions to run the Tableau-based tool:
* Visit the Dropbox link in `link-to-tableau.txt`
* Download `CSE6242Project_Sastry.twbx`
* Open in Tableau Desktop Professional Edition (Tested on 2022.4.1)
* Navigate to "Dashboard"
