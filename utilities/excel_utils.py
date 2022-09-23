# import pandas as pd
#
#
# def read_excel(file):
#     config = dict()
#     data = pd.read_excel(file).to_dict(orient="dict")
#     print(data)
#     for i in range(len(data["Data"])):
#         config[data["Data"][i]] = data["Value"][i]
#     return config
#
# if __name__ == '__main__':
#     r = read_excel(r'F:\workspace\Guvi_PythonSeleniumProject_1\config\data.xlsx')
#     print(r)
