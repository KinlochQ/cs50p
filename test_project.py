from  project import download_mp4,download_mp3 
import pytest


def main():
 test_download_mp4()
 test_download_mp3()
 
def test_download_mp4():
    with pytest.raises(TypeError)as e:
        assert download_mp4("rNDVID")
       
def test_download_mp3(): 
    with pytest.raises(TypeError)as e:
        assert download_mp3("rNDVID")
             
        
        
        
        
        
        
        
if __name__ == "__main__":
    main()
