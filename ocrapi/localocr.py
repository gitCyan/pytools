from myapikey import appid
from myapikey import apikey
from myapikey import secretkey

# 百度tesseract-ocr使用
from aip import AipOcr
import cv2

""" API """
APP_ID = appid
API_KEY = apikey
SECRET_KEY = secretkey

# 初始化AipFace对象
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def img_to_img(image_path):
    image = get_file_content(image_path)
    results = client.general(image)["words_result"]
    img = cv2.imread(image_path)
    for result in results:
        text = result['words']
        location = result['location']
        print(text)
        #draw rectangle
        cv2.rectangle(img, (location['left'], location['top']),
                      (location["left"]+location["width"],location["top"]+location["height"]), (0,255,0), 2)
    cv2.imwrite('output_text_'+image_path, img)
    return

def img_to_str(image_path):
    """ 可选参数 """
    options = {}
    options["language_type"] = "CHN_ENG"  # 中英文混合
    options["detect_direction"] = "true"  # 检测朝向
    options["detect_language"] = "true"  # 是否检测语言
    options["probability"] = "false"  # 是否返回识别结果中每一行的置信度
    image = get_file_content(image_path)
    """ 带参数调用通用文字识别 """
    result = client.basicGeneral(get_file_content(filePath), options)
    # 格式化输出-提取需要的部分
    if 'words_result' in result:
        text = ('\n'.join([w['words'] for w in result['words_result']]))
    print(type(result), "和", type(text))
    """ save """
    fs = open("output_baidu_ocr.txt", 'w+')  # 将str,保存到txt
    fs.write(text)
    fs.close()
    return text

if __name__ == '__main__':
    filePath = '001.jpg'
    print(img_to_str(filePath))
    img_to_img(filePath)
    print("识别完成。")