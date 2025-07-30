from __future__ import unicode_literals
import json
import zipfile
from django.http import JsonResponse, StreamingHttpResponse, Http404
from django.views.decorators.http import require_http_methods

import sys
import os
sys.path.append(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from smart_finance_main import api_DataGeneration


@require_http_methods(["POST"])
def RecreateTable(request):
    postBody = request.body
    postBody = b"{'is_recreate':1}"
    p = postBody.decode()
    p = eval(p)
    is_recreate = p['is_recreate']

    print("Rebuild table start")
    api_DataGeneration.api_user_table("Fake_registration")
    api_DataGeneration.api_store_table("Fake_registration")
    api_DataGeneration.api_card_table("Fake_registration")
    api_DataGeneration.api_trans_table("Fake_registration")
    print("Rebuild table end")

    return JsonResponse(
        {
            "code": 200,
            "data": "success"
        }
    )


def do_zip_compress(dirpath):
    print("Original folder path: " + dirpath)
    output_name = f"{dirpath}Fake_registration.zip"
    print(output_name)
    parent_name = os.path.dirname(dirpath)
    print("Compressed folder directory: ", parent_name)
    zip = zipfile.ZipFile(output_name, "w", zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk(dirpath):
        for file in files:
            if str(file).startswith("~$"):
                continue
            if str(file).endswith(".csv"):
                filepath = os.path.join(root, file)
                print("Compressed file path: " + filepath)
                writepath = os.path.relpath(filepath, parent_name)
                zip.write(filepath, writepath)
    zip.close()


@require_http_methods(["GET"])
def download(request):
    print("Start exporting data")
    path = os.path.dirname(os.path.abspath(__file__)) + r'/datas/'
    print(path)
    api_DataGeneration.api_export_to_csv("Fake_registration", path)

    print("Start packing data")
    do_zip_compress(path)

    print('Start downloading data')
    file_path = path + r'Fake_registration.zip'
    try:
        r = StreamingHttpResponse(open(file_path, "rb"))
        r["content_type"] = "application/octet-stream"
        r["Content-Disposition"] = "attachment;filename=RegisterFraud.zip"
        return r
    except Exception:
        raise Http404("Download error")
