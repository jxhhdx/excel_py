import xlwings as xw

# 显示excel窗口、不新建工作簿
app = xw.App(visible=True, add_book=False)

# <create> 新建一个工作簿
# workbook = app.books.add()

# <open>打开一个工作簿
workbook = app.books.open("d:\\example.xlsx")

# <operate>选中工作簿
worksheet = workbook.sheets['Sheet1']

# <operate>选中A1单元格，并赋值
worksheet.range('A1').value = '编号'

# <create>创建一个工作表
worksheet.sheets.add("产品统计表")

# <save>保存工作簿
workbook.save("d:\\example.xlsx")

# <operate>关闭工作簿
workbook.close()

# <operate>退出Excel
app.quit()


