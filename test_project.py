from  project import download_mp4,download_mp3
import pytest
import tkinter as tk
from pytest import *
import unittest

def main():
 test_download_mp4()
 test_download_mp3()


  
def test_download_mp4():
    with pytest.raises(TypeError)as e:
        assert download_mp4("rNDVID")
       
def test_download_mp3(): 
    with pytest.raises(TypeError)as e:
        assert download_mp3("rNDVID")


class TestFileDialog(unittest.TestCase):

    def test_dialog_closed(self):
        filename = ""
        
        
