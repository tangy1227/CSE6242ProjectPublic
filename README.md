# Interactive, Spatiotemporal Visualization of Spotify Music Popularity
## Important Note
**NOTE:** This project originated from the private repository hosted at [original private repository URL](https://github.com/jerryuhoo/CSE6242Project).

## Instructions to run the D3-based tool:

### Download Spotify Dataset
* Visit https://drive.google.com/file/d/15ThtXZSPA49Y-jtjRzYFawzeLRTBwvAs/view?usp=sharing
* Download `data.csv` and place it in the `CODE/visualization/` directory. Please ensure that it keeps the correct name (data.csv), or change it after moving it into the 'CODE/visualiztion/' directory.

### Obtain API Access to Musixmatch Lyrical Database
This is not entirely required, as we have included our API key in this code release. However, each API key has an associated daily maximum limit on API calls, so it is possible that the tool will fail after some use, if using our API key. To obtain an API key:
* Visit https://developer.musixmatch.com/signup and sign up for an API key
* Update the `self.apikey` variable in `Musixmatch.__init__()` in `CODE/visualization/load_lyrics.py`

### Install required packages
* Mac/Linux users: Open a terminal window, and navigate to the top-level project directory. Windows users: Run commands in in Anaconda Prompt instead.
* Create a conda environment with all required packages by running: 
```bash
conda create --name 6242_env python=3.8
conda activate 6242_env
pip install -r requirements.txt
```
Note that an anaconda installation is a prerequisite here. If required, Anaconda can be obtained from https://www.anaconda.com/download/. Click the Download button corresponding to your operating system.

### Run the tool!
In the same terminal window, run:
```bash
cd CODE/visualization/
python create_database.py
python app.py
```
* Open a second terminal window, navigate to the top-level project directory, and run
```bash
cd CODE/visualization/
conda activate 6242_env
python -m http.server 8000
```

For Windows users, you must specify the full path of the `requirements.txt` and `CODE/visualization/` for the above to run as expected. You can get the full path by right-clicking on that file or directory and selecting 'Properties.' Copy the entire path in 'Location' to the very end and paste it into the anaconda window, then add the remainder (`\requirements.txt` and `\visualization\`, respectively) to that string to get the complete path. When using the second terminal to execute the latter half of the above commands, please use Anaconda Terminal there as well.

An example of a full Windows path for the `requirements.txt` will look something like this: `C:\Users\My_User\Downloads\CSE6242Project-main\CSE6242Project-main\requirements.txt`.

An example of a full Windows path for the `CODE/visualization/` will look something like this: `C:\Users\My_User\Downloads\CSE6242Project-main\CSE6242Project-main\CODE\visualization\`.

* Finally, open a browser, and navigate to http://localhost:8000/chloropleth_map.html

## Instructions to run the Tableau-based tool:
### Download tool and datasets
* Visit https://www.dropbox.com/s/vlwa2ryb1tcermk/CSE6242Project_Sastry.twbx?dl=0
* Download the packaged workbook `CSE6242Project_Sastry.twbx` (which includes the datasets it relies on)

### Install required packages
* Running this tool requires Tableau Desktop Professional Edition (Tested on 2022.4.1). Installation of this software was required for Homework 2 in CSE 6242 (Spring 2023). Please see the Homework 2 for Tableau setup instructions if required.

### Run the tool!
* Open `CSE6242Project_Sastry.twbx` in Tableau Desktop Professional Edition (Tested on 2022.4.1)
* Navigate to "Dashboard"
