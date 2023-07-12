import re
from rdkit import Chem
import json

path = 'Data/formula_data_set.json'

with open(path, 'r') as f:
        data = json.load(f)

def __input__() :
    formula = input('분자식을 입력해 주세요 :') #분자식 입력 받기
    return formula

def m_classify(x): # 분자식 분류
    element = {}
    result = re.findall('[A-Z][a-z]?\d*', x)

    for i in range(len(result)) :
        match = bool(re.search(r'\d', result[i-1]))
        if match == True :
            key = re.sub(r'\d', '', result[i-1]) 
            component = re.findall(r'\d+', result[i-1])[0]
        
        elif match == False :
            key = result[i-1]
            component = 1
        
        element[key] = int(component)

    return element



def r_classify(x): #시성식 분류 (숫자 전까지 분류 -> if숫자 있으면 곱하기) ()괄호 부분 무시
    elements = re.findall('[A-Z][a-z]?\d*', x)
    element_count = {}

    for element in elements:
        element_name = re.match('[A-Z][a-z]?', element).group()
        element_quantity = re.search('\d+', element)
        quantity = int(element_quantity.group()) if element_quantity else 1

        if element_name in element_count:
            element_count[element_name] += quantity
        else:
            element_count[element_name] = quantity

    return element_count


def get() :
    global ex_element

    ex_element = {}
    num = 1
    for i in range(1200) :
        if "Formula" in data[0][i] :
            s_1 = data[0][i]["Formula"]
            s_2 = r_classify(s_1) #변경

            if s_2 == control_element :

                ex_element[num] = s_1,s_2
                num = num + 1

                continue
            else :
                continue
        else :
            continue
    
    
    return ex_element
            


control_formula = __input__()

control_element = m_classify(control_formula)

a = get()

print(a)