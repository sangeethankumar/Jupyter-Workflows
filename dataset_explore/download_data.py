from dandi.download import download

def download_data(dandi_id):
    url = "https://api.dandiarchive.org/api/assets/" + dandi_id + "download/"
    download(url, '.')