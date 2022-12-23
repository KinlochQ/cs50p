from  testing1 import download_mp4,download_mp3 
import pytest


def main():
 test_download_mp4()

def test_download_mp4():
    with pytest.raises(TypeError)as e:
        assert download_mp4("rNDVID")
       
def test_download_mp3(): 
    with pytest.raises(TypeError)as e:
        assert download_mp3("rNDVID")
             
        
        
        https://www.youtube.com/watch?v=QdVa0DcNdGY
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    main()