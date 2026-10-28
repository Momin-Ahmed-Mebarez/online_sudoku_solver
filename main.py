from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import time

from solver import start

if __name__ == '__main__':
    #
    #options = webdriver.EdgeOptions()
    #options.add_experimental_option("detach", True)
    
    #edgeBrowser = webdriver.Edge(options=options)
    edgeBrowser = webdriver.Edge()

    edgeBrowser.get('https://sudokubliss.com/expert')
    while(True):
        input("Start: ")
        time.sleep(0.5)
        input_fields = [edgeBrowser.find_element(By.ID,f"T{cell}") for cell in range(81)]
        #num_fields = [edgeBrowser.find_element(By.ID,f"Num{cell}") for cell in range(0,10)] Old way
    
        puzzle_string = ""
        #Adds the elements found in the cell to create the puzzle
        for field in input_fields:
            try:
                puzzle_string += field.find_elements(By.TAG_NAME,"div")[1].text
            except Exception as e:
                puzzle_string += "0"
    
        original,solution = start(puzzle_string)
        print(solution)
        #We creates changes so that only solved cells are clicked
        changes = solution != original
        for idx,element in enumerate(solution):
            if(changes[idx]):
                input_fields[idx].click()
                ActionChains(edgeBrowser).send_keys(int(solution[idx])).perform()