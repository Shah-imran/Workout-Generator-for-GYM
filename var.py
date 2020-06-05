from json import load
import os
import sys
try:
    def resource_path(relative_path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)

    # icon path

    add_icon = resource_path("icons/add_circle-24px.svg")
    delete_icon = resource_path("icons/delete-24px.svg")
    edit_icon = resource_path("icons/edit-24px.svg")
    info_icon = resource_path("icons/info-24px.svg")
    search_icon = resource_path("icons/search-black-18dp.svg")
    print_icon = resource_path("icons/print-24px.svg")
    cancel_icon = resource_path("icons/clear-24px.svg")
    logout_icon = resource_path("icons/power_settings_new-24px.svg")
    admin_icon = resource_path("icons/admin_panel_settings-24px.svg")
    save_icon = resource_path("icons/save-24px.svg")
    move_up_icon = resource_path("icons/arrow_upward-24px.svg")
    move_down_icon = resource_path("icons/arrow_downward-24px.svg")
    about_icon = resource_path("icons/about.svg")
    # icon path

except Exception as e:
    print(e)

db_user = ""
db_pass = ""
db_ip = ""
db_port = int()
db_name = ""
muscle_groups = list()
admin_mode = False
workout_table = list()
set_count = 1
last_sel = "Set 1"

button_style = """QPushButton {
    color: #000;
    border: 1px solid #555;
    border-radius: 3px;
    border-style: Solid;
    background: qradialgradient(
        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,
        radius: 1.35, stop: 0 #FFF, stop: 1 #D3D3D3
        );
    padding: 5px 28px;
    }

QPushButton:hover {
    background: qradialgradient(
        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,
        radius: 1.35, stop: 0 #fff, stop: 1 #bbb
        );
    }

QPushButton:pressed {
    border-style: inset;
    background: qradialgradient(
        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,
        radius: 1.35, stop: 0 #fff, stop: 1 #ddd
        );
    }"""
try:
    with open('config.json') as json_file:
        data = load(json_file)
    config = data['config']
    db_user = config['db_user']
    db_pass = config['db_pass']
    db_ip = config['ip']
    db_port = config['port']
    db_name = config['db_name']
    admin_password = config['admin_password']
    printer_ip = config["printer_ip"]
    about = ""
    with open('about.txt', 'r', encoding='utf-8') as f:
        about = f.read()

    about += "\n\nDeveloped By - Shah Imran\nSkype_id - shah_imran_sust@outlook.com"
except Exception as e:
    print("Exeception occured at config loading:{}".format(e))
# pyinstaller --onedir --icon=icons/exe.ico --noconfirm main.py