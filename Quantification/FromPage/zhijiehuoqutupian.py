# http://www.galaxystatistics.com/excel/html/webPC62.html
import os

import requests



def get_k_jpg(sheet):
    # 获取最大行数和列数
    max_row = sheet.range('A1').end('down').row
    # max_col = sheet.range('A1').end('right').column
    for row_index in range(2, max_row + 1):
        row_data = sheet.range(f"A{row_index}:Z{row_index}").value
        get_img_add(row_data[1],row_data,sheet,row_index)


    # 遍历Sheet中的每个单元格
    # for row in sheet.iter_rows(min_row=1, max_row=sheet.used_range.last_cell.row, min_col=1,
    #                            max_col=sheet.used_range.last_cell.column):



def get_img_add(code,row,sheet,row_index):
    image_name = "./FromPage/K_jpg/" + code + ".jpg"

    with open(image_name, "wb") as out_file:
        image_url = "https://image.sinajs.cn/newchart/daily/n/"+ get_sz_hz(code) +".gif"
        response = requests.get(image_url, stream=True)

        out_file.write(response.content)

    # print(" index ----",row_index)
    cell_range = "S" + str(row_index)  # 指定单元格位置

    # 获取指定单元格的位置
    left = sheet.range(cell_range).left
    top = sheet.range(cell_range).top

    # 插入图片

    # 将图片缩小比例 放进表格
    # 缩小图片
    # new_width = 100  # 新的宽度
    # new_height = 80  # 新的高度
    # picture.width = new_width
    # picture.height = new_height
    abs_path = r"C:\Users\73699\PycharmProjects\pythonLearn\Quantification\FromPage\K_jpg\\" + code + ".jpg"
    sheet.pictures.add(abs_path, left=left,
                    top=top, width=75, height=15)

    # 删除图片
    os.remove(abs_path)

    # 插入 链接 直接跳转  -- 没必要，前面的更好




def get_sz_hz(code):
    url = None

    if str(code).startswith("00"):
       return "sz" + code

    if str(code).startswith("60"):
       return "sh" + code
        # print(url)
    return str(url)