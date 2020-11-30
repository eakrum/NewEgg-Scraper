from utils import send_text, scanner
from dotenv import load_dotenv

load_dotenv() # Load env variables for script to run

# initiate scanner and scan newegg
scanner(
    {
        "Strix_RTX_3080": {
            "url": "https://www.newegg.com/asus-geforce-rtx-3080-rog-strix-rtx3080-o10g-gaming/p/N82E16814126457?Description=asus%20strix%203080&cm_re=asus_strix%203080-_-14-126-457-_-Product",
            "available": False
        },
        "PNY_RTX_3080": {
            "url": "https://www.newegg.com/pny-geforce-rtx-3080-vcg308010tfxmpb/p/N82E16814133810?Description=rtx%203080&cm_re=rtx_3080-_-14-133-810-_-Product&quicklink=true",
            "available": False
        },
        "EVGA_RTX_3080_FTW3": {
            "url": "https://www.newegg.com/evga-geforce-rtx-3080-10g-p5-3897-kr/p/N82E16814487518?Description=rtx%203080&cm_re=rtx_3080-_-14-487-518-_-Product",
            "available": False
        },
        "EVGA_RTX_3080_XC3": {
            "url": "https://www.newegg.com/evga-geforce-rtx-3080-10g-p5-3885-kr/p/N82E16814487520?Description=rtx%203080&cm_re=rtx_3080-_-14-487-520-_-Product",
            "available": False
        },
        "MSI_RTX_3080": {
            "url": "https://www.newegg.com/msi-geforce-rtx-3080-rtx-3080-gaming-x-trio-10g/p/N82E16814137597?Description=rtx%203080&cm_re=rtx_3080-_-14-137-597-_-Product",
            "available": False
        },
        "MSI_SUPRIM_RTX_3080": {
            "url": "https://www.newegg.com/msi-geforce-rtx-3080-rtx-3080-gaming-x-trio-10g/p/N82E16814137597?Description=rtx%203080&cm_re=rtx_3080-_-14-137-597-_-Product",
            "available": False
        },
        "AORUS_MASTER_RTX_3080": {
            "url": "https://www.newegg.com/msi-geforce-rtx-3080-rtx3080-suprim-x-10g/p/N82E16814137609?Description=rtx%203080&cm_re=rtx_3080-_-14-137-609-_-Product",
            "available": False
        },
        "AORUS_XTREME_RTX_3080": {
            "url": "https://www.newegg.com/gigabyte-geforce-rtx-3080-gv-n3080aorus-x-10gd/p/N82E16814932345?Description=rtx%203080&cm_re=rtx_3080-_-14-932-345-_-Product",
            "available": False
        },
        "EAGLE_RTX_3080": {
            "url": "https://www.newegg.com/gigabyte-geforce-rtx-3080-gv-n3080eagle-10gd/p/N82E16814932367?Description=rtx%203080&cm_re=rtx_3080-_-14-932-367-_-Product",
            "available": False
        },
        "VISION_RTX_3080": {
            "url": "https://www.newegg.com/gigabyte-geforce-rtx-3080-gv-n3080vision-oc-10gd/p/N82E16814932337?Description=rtx%203080&cm_re=rtx_3080-_-14-932-337-_-Product",
            "available": False
        },
    },
    "button", 
    "btn btn-primary btn-wide"
)