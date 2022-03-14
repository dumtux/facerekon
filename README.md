## Quickstart

```sh
sudo apt install python3 python3-pip python3-venv cmake
python3 -m venv myenv
source myenv/bin/activate
pip3 install -r requirements.txt
uvicorn facerekon.app:app --reload
```

Open [Spike page](http://localhost:8000/) in your browser for testing.
Open [API doc](http://localhost:8000/docs) in your browser for reading documentation.
