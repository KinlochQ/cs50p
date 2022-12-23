from  project import download_mp4,download_mp3,select_path
import pytest
import tkinter as tk

def main():
 test_download_mp4()
 test_download_mp3()
 
def test_download_mp4():
    with pytest.raises(TypeError)as e:
        assert download_mp4("rNDVID")
       
def test_download_mp3(): 
    with pytest.raises(TypeError)as e:
        assert download_mp3("rNDVID")
             
 def test_select_path(mocked_filedialog, capsys):
    path_label = tk.Label(text="")
    select_path(path_label)
    assert path_label.cget("text") == "./downloads"       
        
        
        
        
        
        
if __name__ == "__main__":
    main()
