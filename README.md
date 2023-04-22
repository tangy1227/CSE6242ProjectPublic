# CSE6242Project

#### Instructions to run the D3-based tool:

Install environments:
```bash
conda create --name 6242_env python=3.8
pip install -r requirements.txt
conda activate 6252_env
```

From the command line:
```bash
cd visualization/
python create_database.py
python app.py
python -m http.server 8000
```

#### Instructions to run the Tableau-based tool:
* Visit the Dropbox link in link-to-tableau.txt
* Download CSE6242Project_Sastry.twbx
* Open in Tableau Desktop Professional Edition (Tested on 2022.4.1)
* Navigate to "Dashboard"
