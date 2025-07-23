from __future__ import unicode_literals
import json
import zipfile
from django.http import JsonResponse, StreamingHttpResponse, Http404
from django.views.decorators.http import require_http_methods

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
from smart_finance_main import api_DataGeneration


@require_http_methods(["POST"])
def RecreateTable(request):
    postBody = request.body
    postBody = b"{'is_recreate':1}"
    p = postBody.decode()
    p = eval(p)
    is_recreate = p['is_recreate']

    print("重建表开始")
    api_DataGeneration.api_user_table("异常转账")
    api_DataGeneration.api_store_table("异常转账")
    api_DataGeneration.api_card_table("异常转账")
    api_DataGeneration.api_trans_table("异常转账")
    print("重建表结束")

    return JsonResponse(
        {
            "code": 200,
            "data": "success"
        }
    )


def do_zip_compress(dirpath):
    print("原始文件夹路径：" + dirpath)
    output_name = f"{dirpath}异常转账.zip"
    print(output_name)
    parent_name = os.path.dirname(dirpath)
    print("压缩文件夹目录：", parent_name)
    zip = zipfile.ZipFile(output_name, "w", zipfile.ZIP_DEFLATED)
    # 多层级压缩
    for root, dirs, files in os.walk(dirpath):
        for file in files:
            if str(file).startswith("~$"):
                continue
            if str(file).endswith(".csv"):
                filepath = os.path.join(root, file)
                print("压缩文件路径：" + filepath)
                writepath = os.path.relpath(filepath, parent_name)
                zip.write(filepath, writepath)
    zip.close()


@require_http_methods(["GET"])
def download(request):
    # 开始导出数据
    print("开始导出数据")
    path = os.path.dirname(os.path.abspath(__file__)) + r'/datas/'
    print(path)
    api_DataGeneration.api_export_to_csv("异常转账", path)

    # 开始打包数据
    print("开始打包数据")
    do_zip_compress(path)

    # 开始下载数据
    print('开始下载数据')
    file_path = path + r'异常转账.zip'
    try:
        r = StreamingHttpResponse(open(file_path, "rb"))
        r["content_type"] = "application/octet-stream"
        r["Content-Disposition"] = "attachment;filename=AbnormalTrans.zip"
        return r
    except Exception:
        raise Http404("Download error")
