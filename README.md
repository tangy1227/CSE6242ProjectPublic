# CSE6242Project

#### Instructions to run the D3-based tool:

Install environments:
```bash
conda create --name 6242_env python=3.8
pip install -r requirements.txt
conda activate 6242_env
```

From the command line:
```bash
cd CODE/visualization/
python create_database.py
```

Open two terminals and execute `python app.py` and `python -m http.server 8000` in each terminal.

Open a browser, and navigate to http://localhost:8000/chloropleth_map.html

#### Instructions to run the Tableau-based tool:
* Visit the Dropbox link in link-to-tableau.txt
* Download CSE6242Project_Sastry.twbx
* Open in Tableau Desktop Professional Edition (Tested on 2022.4.1)
* Navigate to "Dashboard"
