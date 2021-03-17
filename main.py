from os import error
from bs4 import BeautifulSoup
import requests
import win32clipboard
import keyboard
import time
from tkinter import *
from tkinter import ttk
import webbrowser
import win32gui, win32con

def search(word):
    try:
        source = requests.get(f'https://www.dictionary.com/browse/{word}?s=t')
        soup = BeautifulSoup(source.text, 'lxml')
        meaning = soup.find('span', class_='one-click-content')
        try:
            return meaning.text
        except:
            return 'Not Found'
    except:
        return 'Error'

def seeKeys():
    try:
        if keyboard.is_pressed('ctrl+q'):
            keyboard.press_and_release('ctrl+c')
            time.sleep(1)
            win32clipboard.OpenClipboard()
            words = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
            word.config(text=words)
            meaning.config(text=search(words))
            root.update()
            siteButton.place(x = word.winfo_reqwidth()+30, y = 55, height = 50, width = 100)
            root.geometry(f'500x{(meaning.winfo_reqheight()+135)}')
            root.deiconify()
        elif keyboard.is_pressed('ctrl+e'):
            root.withdraw()
    except Exception as e:
        print(e)
    root.after(10, seeKeys)

def searchButt():
    words = searchBar.get()
    word.config(text=words)
    meaning.config(text=search(words))
    root.update()
    siteButton.place(x = word.winfo_reqwidth()+30, y = 55, height = 50, width = 100)
    root.geometry(f'500x{(meaning.winfo_reqheight()+135)}')
    root.deiconify()

def siteButt():
    words = word.cget('text')
    url = f'https://www.dictionary.com/browse/{words}?s=t'
    webbrowser.open(url)
     
if __name__ == '__main__':
    the_program_to_hide = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)
    root = Tk()
    root.resizable(0,0)
    root.title('Ctrl+Dictionary')
    searchBar = ttk.Entry(root, text = 'Word')
    searchBar.place(x = 10, y = 10, height = 30, width = 370)
    searchButton = ttk.Button(root, text = 'Search!', command = searchButt)
    searchButton.place(x =390, y = 10, height = 30, width = 100)
    word = Label(root, text='Text:', font=("", 40))
    word.place(x = 10,y = 45)
    siteButton = ttk.Button(root, text='Look on\ndictionary.com', command = siteButt)
    siteButton.place(x = word.winfo_reqwidth()+30, y = 55, height = 50, width = 100)
    meaning = Label(root, text='the main body of matter in a manuscript, book, newspaper, etc., as distinguished from notes, appendixes, headings, illustrations, etc.', wraplength=480, font=('', 20))
    meaning.place(x = 10,y = 125)
    root.geometry(f'500x{(meaning.winfo_reqheight()+135)}')
    root.withdraw()
    seeKeys()
    root.mainloop()
    win32gui.ShowWindow(the_program_to_hide , win32con.SW_SHOW)